import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMIES, SPAWN_TIME, C_MILITARY_GREEN, C_GRAY, \
    EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, C_BLACK
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.VideoManager import VideoManager
from code.Score import Score


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        self.entity_list.append(player)

        # Inicializa o gerenciador de vídeos e seta os paths dos videos e audios deles como um atributo da class (q serão usados)
        self.video_manager = VideoManager(self.window)

        self.intro_video = "./asset/intro_video.mp4"
        self.intro_audio = "./asset/intro_audio.mp3"

        self.success_video = "./asset/success_video.mp4"
        self.success_audio = "./asset/success_audio.mp4"

        self.failure_video = "./asset/failure_video.mp4"
        self.failure_audio = "./asset/failure_audio.mp4"

        # Usa um timer para criar os inimigos baseado na constante SPAWN_TIME
        pygame.time.set_timer(EVENT_ENEMIES, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 16s

    def run(self, player_score: list[int]):

        # Carregar e reproduzir música de fundo
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        # Exibição do vídeo de introdução
        self.video_manager.play_video(self.intro_video, self.intro_audio)

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                if isinstance(ent, (Player, Enemy)):
                    ent.render(self.window)
                else:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if ent.name == 'Player':
                    self.level_text(14, f'Player - Health: {ent.health} | Score: {ent.score}', C_MILITARY_GREEN, (10, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMIES:
                    choice = random.choice(('Tree', 'Wind', 'Dog')) #falta add 'Bird'
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        player = self.get_player()
                        player_score[0] = player.score

                        # Vídeo final de sucesso ou falha
                        if self.check_meat_bread_bar():
                            self.video_manager.play_video(self.success_video, self.success_audio)
                        else:
                            self.video_manager.play_video(self.failure_video, self.failure_audio)

                        # Após o sucesso ou falha, salva o score
                        if self.check_meat_bread_bar():
                            score_handler = Score(self.window)
                            score_handler.save(self.game_mode, player_score)  # Salva o score com o método save
                        return self.check_meat_bread_bar()

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    # O jogador morreu, falha no nível
                    self.video_manager.play_video(self.failure_video, self.failure_audio)
                    return False

            # Desenha a barra de MeatBreads
            self.draw_meat_bread_bar()

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Colisões e verificação de saúde
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Orbitron", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def draw_meat_bread_bar(self):
        """Desenha a barra de MeatBreads no canto superior esquerdo."""
        player = self.get_player()
        meat_bread_bar = player.meat_bread_bar
        meat_bread_target = player.meat_bread_target

        # Definir as posições da barra e o tamanho dos itens
        bar_width = 300
        bar_height = 20
        bar_x = 10
        bar_y = 40

        # Calcular a proporção com base nos MeatBreads coletados
        meat_bread_width = bar_width / meat_bread_target  # Barra dividida igualmente pelo número alvo de MeatBreads

        # Desenha o fundo da barra
        pygame.draw.rect(self.window, C_BLACK, (bar_x, bar_y, bar_width, bar_height))

        # Desenha a parte preenchida da barra
        pygame.draw.rect(self.window, C_GRAY, (bar_x, bar_y, meat_bread_bar * meat_bread_width, bar_height))

        # Desenha os contadores de MeatBreads
        self.level_text(14, f'MeatBreads: {meat_bread_bar}/{meat_bread_target}', C_WHITE, (bar_x + bar_width + 10, bar_y + 5))

    def check_meat_bread_bar(self):
        """Verifica se o jogador completou a barra de MeatBreads (3) para concluir a fase."""
        player = self.get_player()
        return player.meat_bread_bar >= 3  # Verifica se o jogador coletou 3 MeatBreads

    def get_player(self):
        """Retorna o jogador da lista de entidades."""
        for ent in self.entity_list:
            if isinstance(ent, Player):
                return ent
        return None

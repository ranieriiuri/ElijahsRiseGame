import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMIES, SPAWN_TIME, C_MILITARY_GREEN, C_GRAY, \
    EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, C_BLACK, EVENT_MB, MB_SPAWN_TIME
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.MeatBread import MeatBread
from code.Player import Player
from code.TransitionManager import TransitionManager
from code.Tree import Tree
from code.VideoManager import VideoManager
from code.Score import Score
from code.Wind import Wind

# OBS:  falta verificar pq p score das meat breads não está sendo adicionado ao Player e implementar Como voltar ao menu após salvar o score !!!

# Func global
def load_and_scale(path, scale_factor):
    img = pygame.image.load(path).convert_alpha()
    w, h = img.get_width(), img.get_height()
    return pygame.transform.scale(img, (int(w * scale_factor), int(h * scale_factor)))


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
        self.entity_list.append(player) #--> Add o Player ao jogo assim q inicia a fase

        # Ímagem meat breads escalado pro tam de ícone
        self.meat_bread_icon = load_and_scale("./asset/mb_image.png", 0.015) # usando uma função global para redimensionar o ícone

        # Inicializa o gerenciador de vídeos e seta os paths dos videos e audios deles como um atributo da class (q serão usados)
        self.video_manager = VideoManager(self.window)

        self.intro_video = "./asset/intro_video.mp4"
        self.intro_audio = "./asset/intro_audio.mp3"

        self.success_video = "./asset/success_video.mp4"
        self.success_audio = "./asset/success_audio.mp3"

        self.failure_video = "./asset/failure_video.mp4"
        self.failure_audio = "./asset/failure_audio.mp3"

        # Usa um timer para criar os inimigos baseado na constante SPAWN_TIME
        pygame.time.set_timer(EVENT_ENEMIES, SPAWN_TIME)
        pygame.time.set_timer(EVENT_MB, MB_SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 16s

    def run(self, player_score: list[int]):

        # Exibição do vídeo de introdução
        self.video_manager.play_video(self.intro_video, self.intro_audio)

        pygame.mixer.init()
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)


        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            for ent in sorted(self.entity_list, key=lambda e: getattr(e, 'z_index', 0)):
                if hasattr(ent, 'update'):
                    ent.update() # para verificar o update da meat bread

                ent.render(self.window)
                ent.move()

                if ent.name == 'Player':
                    self.level_text(14, f'Player - Health: {ent.health} | Score: {ent.score}', C_MILITARY_GREEN, (10, 25))

            for event in pygame.event.get():
                player = self.get_player()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # paramos nas entidades inimigas
                if event.type == EVENT_ENEMIES:
                    choice = random.choice(('Dog', 'Tree')) # faltam 'Bird', 'Wind'
                    self.entity_list.append(EntityFactory.get_entity(choice))

                # criando as meat breads baseadas no timer q baseia um spawn time na const 'EVENT_MB'
                elif event.type == EVENT_MB:
                    self.entity_list.append(EntityFactory.get_entity('MeatBread'))

                # verificando as hipoteses de falha ou sucesso do P1
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        self.video_manager.play_video(self.failure_video, self.failure_audio)
                        TransitionManager.fade_out(self.window, duration=800)
                        return False

                # Verificar constantemente se o player atingiu o objetivo
                if player is not None and player.meat_bread_bar >= player.meat_bread_target:
                    print("Barra de MeatBreads cheia! Fase concluída com sucesso.")

                    player_score[0] = player.score
                    self.video_manager.play_video(self.success_video, self.success_audio)
                    TransitionManager.fade_out(self.window, duration=800)
                    Score(self.window).save(self.game_mode, player_score)

                    return True  # Sai do nível

                # Caso o player morra antes do tempo acabar
                if player is None:
                    self.video_manager.play_video(self.failure_video, self.failure_audio)
                    TransitionManager.fade_out(self.window, duration=800)
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
        """Desenha os ícones de MeatBreads coletados no canto superior esquerdo."""
        player = self.get_player()
        meat_bread_bar = player.meat_bread_bar
        meat_bread_target = player.meat_bread_target

        # Definir as posições da barra e o tamanho dos slots
        bar_x = 15
        bar_y = 30
        icon_size = 32  # Tamanho dos ícones
        spacing = 12  # Espaço entre os ícones

        # Desenha os slots vazios
        for i in range(meat_bread_target):
            slot_x = bar_x + i * (icon_size + spacing)
            pygame.draw.rect(self.window, C_GRAY, (slot_x, bar_y, icon_size, icon_size), 2)  # Borda do slot

        # Desenha os MeatBreads coletados
        for i in range(meat_bread_bar):
            icon_x = bar_x + i * (icon_size + spacing)
            self.window.blit(self.meat_bread_icon, (icon_x, bar_y))

        # Exibe o contador numérico ao lado da barra
        self.level_text(16, f'MeatBreads: {meat_bread_bar}/{meat_bread_target}', C_MILITARY_GREEN,
                        (bar_x + (meat_bread_target * (icon_size + spacing)) + 20, bar_y + 6))

    def check_meat_bread_bar(self):
        """Verifica se o jogador completou a barra de MeatBreads (3) para concluir a fase."""
        player = self.get_player()
        return player.meat_bread_bar >= player.meat_bread_target  # Verifica se o jogador coletou 3 MeatBreads

    def get_player(self):
        """Retorna o jogador da lista de entidades."""
        for ent in self.entity_list:
            if isinstance(ent, Player):
                return ent
        return None


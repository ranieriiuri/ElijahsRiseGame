import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.VideoManager import VideoManager


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        # Inicializa o gerenciador de vídeos
        self.video_manager = VideoManager(self.window)

        # Variáveis de vídeo do patrocinador
        self.sponsor_video = "./asset/sponsor.mp4"
        self.sponsor_audio = "./asset/sponsor_audio.mp3"  # Arquivo de áudio extraído
    def run(self):

        # Vídeo do patrocinador
        self.video_manager.play_video(self.sponsor_video, self.sponsor_audio)

        while True:
            for event in pygame.event.get():
                # Verifica o evento de fechamento da janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Verifica pressionamento da tecla para minimizar a tela
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_MINUS:  # Se pressionar "-", minimiza a tela
                        pygame.display.iconify()

                # Verifique se o jogador deseja sair da aplicação
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Se pressionar "Q", fecha o jogo (em caso de teste)
                        pygame.quit()
                        sys.exit()

            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run() # chama o método que seta o fundo do menu com a música, suas opções e etc

            if menu_return in MENU_OPTION[0]:
                player_score = [0] # lista com um único valor (referente ao P1)
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score) # chama o level.run passando a lista passada acima

                if level_return: #se o nivel foi concluído
                    score.save(menu_return, player_score) # pela escolha do menu (nesse caso, apenas teremos [0] = Star game, por enquanto), salva o score
                else:
                    pass

            elif menu_return == MENU_OPTION[1]: #se opção 2 do menu, mostra a lista de scores
                score.show()

            elif menu_return == MENU_OPTION[2]: #se opção 3, é quit

                pygame.quit()
                sys.exit()
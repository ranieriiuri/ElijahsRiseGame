import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_MILITARY_GREEN, C_GRAY, C_BLACK, WIN_HEIGHT, C_GOLD


class Menu:
    def __init__(self, window):
        self.window = window
        #traz a imagem do menu
        self.surf = pygame.image.load('./asset/MenuBg.jpeg').convert_alpha()
        # Redimensiona a imagem para se ajustar à tela
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        # Define o retângulo da imagem
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0 # padrão

        # carrega a musica
        pygame.mixer_music.load('./asset/Menu.mp3')

        # toca indefinidamente com '-1'
        pygame.mixer_music.play(-1)
        while True:
            # seta a imagem carregada acima pro menu e desenha o nome do jogo
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Elijah", C_GOLD, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Rises", C_GOLD, ((WIN_WIDTH / 2), 120))

            # setando cores e dimensões conforme escolhemos pelas posições do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_MILITARY_GREEN, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_BLACK, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

           # laço q verifica o uso do "x" para fechar o jogo, as opções escolhidas e, caso ENTER, seta a opção como escolhida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                # assimila cada tecla pra cima + enter ou pra baixo + enter como a escolha conforme opção
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # se apertar ENTER, essa é a opção escolhida
                        return MENU_OPTION[menu_option]

    #metodo q constroi as características dos textos do menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Orbitron", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

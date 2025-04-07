import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_MILITARY_GREEN, C_GRAY, C_BLACK, WIN_HEIGHT, C_GOLD, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        #traz a imagem do menu
        self.surf = pygame.image.load('./asset/MenuBg.jpeg').convert_alpha()
        # Redimensiona a imagem para se ajustar à tela
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        # Define o retângulo da imagem
        self.rect = self.surf.get_rect(left=0, top=0)
        self.brightness = 0  # Controle do brilho
        self.brightness_direction = 1  # Direção da oscilação

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # Atualiza o brilho do título "Elijah Rises"
            self.brightness += self.brightness_direction * 0.5
            if self.brightness >= 50 or self.brightness <= 0:
                self.brightness_direction *= -1
            dynamic_gold = (max(C_GOLD[0] - self.brightness, 0), max(C_GOLD[1] - self.brightness, 0), C_GOLD[2])

            # Exibe o título com efeito de brilho
            self.menu_text(70, "Elijah Rises", dynamic_gold, ((WIN_WIDTH - 260), 70))
            self.menu_text(18, "A journey of faith n' bravery", C_WHITE, ((WIN_WIDTH - 260), 105))

            # Renderiza as opções do menu
            for i in range(len(MENU_OPTION)):
                size = 20 if i != menu_option else 30  # Aumenta a fonte se for a opção selecionada
                color = C_WHITE if i == menu_option else C_BLACK
                self.menu_text(size, MENU_OPTION[i], color, ((WIN_WIDTH - 260), 200 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Carrega a fonte MedievalSharp diretamente do arquivo
        text_font: Font = pygame.font.Font("./asset/MedievalSharp.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


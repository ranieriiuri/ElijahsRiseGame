import pygame
import random
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity

class Wind(Entity):
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface, rows: int = 1, cols: int = 1):
        # Redimensiona o sprite sheet
        scale_factor = 0.38 #38% do tam original
        new_width = int(sprite_sheet.get_width() * scale_factor)
        new_height = int(sprite_sheet.get_height() * scale_factor)
        scaled_sheet = pygame.transform.scale(sprite_sheet, (new_width, new_height))

        super().__init__(name, position, scaled_sheet, rows, cols)

        self.z_index = 3 # a frente de todas as outras entities em profundidade de tela
        self.vertical_velocity = random.choice([-1, 1]) # var p controlar a velocidade randomica no eixo y
        self.speed = ENTITY_SPEED[self.name]

    def move(self):
        """Movimenta o vento para a esquerda com flutuação vertical aleatória."""
        # movimento contínuo para a esquerda, baseado na const definida no arq 'Const'
        self.rect.centerx -= self.speed

        # movimento vertical leve e errático
        self.rect.centery += self.vertical_velocity * 6

        # inverte direção vertical se encostar no topo ou na base
        if self.rect.top <= 0 or self.rect.bottom >= WIN_HEIGHT:
            self.vertical_velocity *= -1

        # chance de mudar levemente a direção vertical (mais natural)
        if random.randint(0, 100) < 3: # 3% de chance de mudar a direção no eixo y
            self.vertical_velocity = random.choice([-1, 0, 1])

    def render(self, screen):
        self.update_animation()
        screen.blit(self.surf, self.rect)

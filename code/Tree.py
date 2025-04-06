import os
import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Tree(Entity):
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface, rows: int = 1, cols: int = 1):

        # Escala fixa
        scale_factor = 0.38
        new_width = int(sprite_sheet.get_width() * scale_factor)
        new_height = int(sprite_sheet.get_height() * scale_factor)
        scaled_sheet = pygame.transform.scale(sprite_sheet, (new_width, new_height))


        super().__init__(name, position, scaled_sheet, rows, cols)
        self.z_index = 0 # mantém a Tree sempre em segundo pĺano em relação às outras entidades quando houver colisão sem danos (entre as entidades, exceto a Player)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def render(self, screen):
        self.update_animation()  # Atualiza o frame atual da animação
        screen.blit(self.surf, self.rect)  # Renderiza na tela
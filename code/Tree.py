import os
import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Tree(Entity):
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface, rows: int = 1, cols: int = 1):
        super().__init__(name, position, sprite_sheet, rows, cols)
        self.z_index = 1 # mantém a Tree sempre em segundo pĺano em relação às outras entidades quando houver colisão sem danos (entre as entidades, exceto a Player)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def update(self):
        """ Atualiza a posição e a animação da árvore chamando os métodos construídos na classe mãe """
        self.move()
        self.update_animation()
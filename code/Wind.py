import pygame
import random
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Wind(Entity):
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface, rows: int = 1, cols: int = 1):
        super().__init__(name, position, sprite_sheet, rows, cols)
        self.z_index = 2  # Adiciona à camada do meio, à frente da Tree (que tem z_index 1)

    def move(self):
        """Movimenta o vento para a esquerda e aleatoriamente no eixo Y."""
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # Movimenta aleatoriamente no eixo Y
        self.rect.centery += random.choice([-1, 0, 1])  # Movimentos de -1, 0 ou 1 no eixo Y

        # Garante que o vento não ultrapasse a borda esquerda da tela
        # if self.rect.right < 0:
        #    self.rect.left = 800  # Reinicia a posição se sair da tela

    def update(self):
        """Atualiza a posição e a animação do vento."""
        self.move()
        self.update_animation()
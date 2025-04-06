import random
import pygame
import math

class EntityBehavior:
    def __init__(self, entity, base_y=None):
        self.entity = entity
        self.base_y = base_y if base_y is not None else entity.rect.centery
        self.is_jumping = False
        self.jump_offset = 0
        self.jump_height = 20
        self.jump_speed = 2

    # metodos do Dog
    def jump(self, probability: float = 0.05):
        """Inicia pulo com certa chance"""
        if not self.is_jumping and random.random() < probability:
            self.is_jumping = True
            self.jump_offset = 0

    def update_jump(self):
        """Atualiza a posição vertical da entidade se estiver pulando"""
        if self.is_jumping:
            if self.jump_offset < self.jump_height:
                self.jump_offset += self.jump_speed
                self.entity.rect.centery -= self.jump_speed
            else:
                self.jump_offset -= self.jump_speed
                self.entity.rect.centery += self.jump_speed
                if self.jump_offset <= 0:
                    self.entity.rect.centery = self.base_y
                    self.is_jumping = False

    # métodos das meat breads
    @staticmethod
    def float_motion(entity, amplitude=5, frequency=0.05):
        """Aplica um movimento senoidal vertical (flutuação)."""
        offset = amplitude * math.sin(pygame.time.get_ticks() * frequency)
        entity.rect.centery = entity.original_y + offset
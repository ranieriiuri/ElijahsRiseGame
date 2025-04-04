import pygame

from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, image_path: str):
        super().__init__(name, position)
        self.surf = pygame.image.load(image_path).convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)  # reposiciona o rect corretamente
        self.speed = ENTITY_SPEED.get(name, 1)
        self.z_index = -1

    def move(self):
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

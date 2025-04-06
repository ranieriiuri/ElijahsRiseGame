import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, image_path: str):
        super().__init__(name, position)

        # Carrega e redimensiona a imagem para caber na tela
        raw_image = pygame.image.load(image_path).convert_alpha()
        self.surf = pygame.transform.scale(raw_image, (WIN_WIDTH, WIN_HEIGHT))

        self.rect = self.surf.get_rect(topleft=position)
        self.speed = ENTITY_SPEED.get(name, 1)
        self.z_index = -1  # entidades mais ao fundo (em termos de profundidade)

    def move(self):
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

    def render(self, screen):
        screen.blit(self.surf, self.rect)
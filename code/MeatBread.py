import pygame
from code.Entity import Entity

class MeatBread(Entity):
    def __init__(self, x, y, image_path, value=1):
        super().__init__(x, y)
        self.image = pygame.image.load(image_path).convert_alpha()  # Carrega a imagem fixa
        self.rect = self.image.get_rect(topleft=(x, y))  # Define posição inicial
        self.value = value  # Quantidade a ser adicionada à barra do player
        self.blink_timer = 20  # Tempo de piscar antes de sumir
        self.collected = False  # Indica se já foi coletado

    def update(self):
        if self.collected:
            self.blink_timer -= 1
            if self.blink_timer <= 0:
                self.health = 0  # Remove a entidade do jogo

    def collect(self, player):
        """Realiza a coleta da MeatBread. Chama o método para aumentar a barra de MeatBreads do jogador."""
        if not self.collected:
            player.collect_meat_bread()  # Notifica o jogador que uma MeatBread foi coletada
            self.collected = True  # Marca a MeatBread como coletada

    def draw(self, surface):
        if not self.collected or self.blink_timer % 4 < 2:  # Efeito de piscar antes de sumir
            surface.blit(self.image, self.rect)

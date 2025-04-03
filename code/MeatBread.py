import pygame
from code.Entity import Entity

class MeatBread(Entity):
    def __init__(self, name, position, sprite_sheet, value=1):
        # Como a MeatBread usa uma sprite sheet, passamos rows=1 e cols=1 se for imagem estática
        super().__init__(name, position, sprite_sheet, rows=1, cols=1)

        self.value = value  # Quantidade a ser adicionada à barra do player
        self.blink_timer = 20  # Tempo de piscar antes de sumir
        self.collected = False  # Indica se já foi coletada

    def update(self):
        """Gerencia a lógica de desaparecimento após a coleta."""
        if self.collected:
            self.blink_timer -= 1
            if self.blink_timer <= 0:
                self.health = 0  # Remove a entidade do jogo
        else:
            self.update_animation()  # Mantém a animação rodando normalmente antes da coleta

    def collect(self, player):
        """Realiza a coleta da MeatBread e avisa o jogador."""
        if not self.collected:
            player.collect_meat_bread()  # Notifica o jogador
            self.collected = True  # Marca como coletada

    def move(self):
        """MeatBread não se move, então o método está presente apenas para cumprir a exigência da Entity."""
        pass

    def render(self, screen):
        """Renderiza a MeatBread na tela. Se coletada, pisca antes de sumir."""
        if not self.collected or self.blink_timer % 4 < 2:  # Efeito de piscar antes de desaparecer
            super().render(screen)  # Usa a renderização da Entity

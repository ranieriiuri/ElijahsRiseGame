import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity
from code.EntityBehavior import EntityBehavior  # ← se ainda não estiver importado

class MeatBread(Entity):
    def __init__(self, name, position, sprite_sheet, rows: int = 1, cols: int = 1):

        scale_factor = 0.03  # Ajusta em porcentagem o tamanho da sprite_sheet em relação ao original
        new_width = int(sprite_sheet.get_width() * scale_factor)
        new_height = int(sprite_sheet.get_height() * scale_factor)
        scaled_sheet = pygame.transform.scale(sprite_sheet, (new_width, new_height))

        super().__init__(name, position, scaled_sheet, rows, cols)

        self.z_index = 1

        self.blink_timer = 20
        self.collected = False

        self.original_y = self.rect.centery  # ← Guarda posição original pro movimento de flutuar

    def update(self):
        if self.collected:
            self.blink_timer -= 1
            if self.blink_timer <= 0:
                self.health = 0
        else:
            self.update_animation()

    def collect(self, player):
        if not self.collected:
            player.collect_meat_bread()
            self.collected = True

    def move(self):
        """Aplica movimento de flutuar se ainda não foi coletada."""
        self.rect.centerx -= ENTITY_SPEED[self.name]
        #if not self.collected:
        #    EntityBehavior.float_motion(self)

    def render(self, screen):
        if not self.collected or self.blink_timer % 4 < 2:
            screen.blit(self.surf, self.rect)  # Desenha normalmente quando o blink_timer acabou

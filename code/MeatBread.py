from code.Entity import Entity
from code.EntityBehavior import EntityBehavior  # ← se ainda não estiver importado

class MeatBread(Entity):
    def __init__(self, name, position, sprite_sheet, value=1):
        super().__init__(name, position, sprite_sheet, rows=1, cols=1)

        self.value = value
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
        if not self.collected:
            EntityBehavior.float_motion(self)

    def render(self, screen):
        if not self.collected or self.blink_timer % 4 < 2:
            super().render(screen)

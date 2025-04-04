import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface, rows: int = 1, cols: int = 1):
        # Redimensiona o sprite sheet antes de passar para a classe mãe
        scale_factor = 0.2  # Ajuste esse valor como quiser (30% do tamanho original)
        new_width = int(sprite_sheet.get_width() * scale_factor)
        new_height = int(sprite_sheet.get_height() * scale_factor)
        scaled_sheet = pygame.transform.scale(sprite_sheet, (new_width, new_height))

        super().__init__(name, position, scaled_sheet, rows, cols)

        self.speed = ENTITY_SPEED[self.name]
        self.blink_timer = 0
        self.meat_bread_bar = 0
        self.meat_bread_target = 3
        self.z_index = 0

    def move(self):
        pressed_key = pygame.key.get_pressed() #obtém todas as teclas pressionadas no momento

        #se a tecla pra cima do player em questão estiver pressionada e o topo da dimensão total do player for maior q 0 (garante estar dentro da tela definida), então move o player pra cima, diminuindo sua posição no eixo y (já q zero é em cima-esquerda da tela)

        # Movimenta o player conforme a tecla pressionada, sem sair da tela
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= self.speed
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += self.speed
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += self.speed

        # Atualiza a animação (chama o método da classe mãe)
        self.update_animation()

#TESTING EFFECTS AROUND
    def take_damage(self, damage):
        self.health -= damage
        self.blink_timer = 20  # Define um tempo para piscar

    def collect_meat_bread(self):
        """Este método será chamado quando o jogador coletar uma MeatBread."""
        if self.meat_bread_bar < self.meat_bread_target:
            self.meat_bread_bar += 1
            if self.meat_bread_bar >= self.meat_bread_target:
                return True  # Retorna True quando a meta de MeatBreads é alcançada
        return False

    def reset(self):
        """Reseta o estado do jogador."""
        self.meat_bread_bar = 0  # Reseta o contador de MeatBreads coletados

    # a player tem render pq tem a construcao de piscar quando houver dano
    def render(self, screen):
        if self.blink_timer > 0:
            if self.blink_timer % 2 == 0:  # Pisca ao sofrer dano
                screen.blit(self.surf, self.rect)  # Desenha a imagem atual (self.surf)
            self.blink_timer -= 1  # Decrementa o blink_timer ao renderizar
        else:
            screen.blit(self.surf, self.rect)  # Desenha normalmente quando o blink_timer acabou

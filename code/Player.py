#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
#from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface):
        super().__init__(name, position, sprite_sheet)
        # self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.speed = ENTITY_SPEED[self.name] #setando velocidade padrão do player
        self.blink_timer = 0


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
        self.blink_timer = 40  # Define um tempo para piscar

    # a player tem render pq tem a construcao de piscar quando houver dano
    def render(self, screen):
        if self.blink_timer > 0:
            if self.blink_timer % 2 == 0:  # Pisca ao sofrer dano
                screen.blit(self.surf, self.rect)  # Desenha a imagem atual (self.surf)
            self.blink_timer -= 1  # Decrementa o blink_timer ao renderizar
        else:
            screen.blit(self.surf, self.rect)  # Desenha normalmente quando o blink_timer acabou

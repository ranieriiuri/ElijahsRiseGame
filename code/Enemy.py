#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random
from code.Const import ENTITY_SPEED
from code.Entity import Entity

class Enemy(Entity):
    """ Classe única para inimigos (pássaro e cachorro) """
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface, movement_type: str, rows: int = 1, cols: int = 1):
        """
        :param name: Nome do inimigo ("passaro" ou "cachorro")
        :param position: Posição inicial (x, y)
        :param movement_type: Tipo de movimento ("ground" para chão, "air" para voar)

        * Lembrando que, as variáveis com valores padrões (opcionais) vêm sempre depois dos obrigatórios no python !
        """
        super().__init__(name, position, sprite_sheet, rows, cols)
        # o entity.render(screen) deve ser chamado no laço principal do jogo, para renderizar a construção das entidades na tela
        self.movement_type = movement_type
        self.z_index = 2 if movement_type == "air" else 3  # Aéreo fica atrás do terrestre

    def move(self):
        """ Movimentação personalizada para cada tipo de inimigo """
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.movement_type == "air":
            # Pássaro voa reto
            pass
        elif self.movement_type == "ground":
            # Cachorro pode dar pequenos pulos
            if random.random() < 0.01:  # 1% de chance de pular
                self.rect.centery -= 5 # ainda falta rever isto

    def take_damage(self, damage):
        self.health -= damage

    def update(self):
        """ Atualiza o estado do inimigo, incluindo a animação. Puxando os métodos q implementam essa lógica da classe mãe (Entity)."""
        self.move()
        self.update_animation()

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random
from code.Const import ENTITY_SPEED
from code.Entity import Entity

class Enemy(Entity):
    """ Classe única para inimigos (pássaro e cachorro) """
    def __init__(self, name: str, position: tuple, movement_type: str):
        """
        :param name: Nome do inimigo ("passaro" ou "cachorro")
        :param position: Posição inicial (x, y)
        :param movement_type: Tipo de movimento ("ground" para chão, "air" para voar)
        """
        super().__init__(name, position)
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

    def render(self, screen):
        screen.blit(self.surf, self.rect)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random
from code.Const import ENTITY_SPEED
from code.Entity import Entity
from code.EntityBehavior import EntityBehavior


class Enemy(Entity):
    """ Classe única para inimigos (pássaro e cachorro) """
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface, movement_type: str, rows: int = 1, cols: int = 1):

        # Escala fixa
        scale_factor = 0.26 if name == "Dog" else 0.13  # Ajuste o fator conforme quiser / primeiro valor = Dog - segundo = Bird
        new_width = int(sprite_sheet.get_width() * scale_factor)
        new_height = int(sprite_sheet.get_height() * scale_factor)
        scaled_sheet = pygame.transform.scale(sprite_sheet, (new_width, new_height))

        # Chama a superclasse com o sprite já escalado
        super().__init__(name, position, scaled_sheet, rows, cols)

        # o entity.render(screen) deve ser chamado no laço principal do jogo, para renderizar a construção das entidades na tela
        self.movement_type = movement_type
        self.z_index = 2 if movement_type == "air" else 1  # Aéreo fica atrás do terrestre

        # Comportamento de pulo apenas se for terrestre
        self.behavior = EntityBehavior(self, base_y=position[1]) if movement_type == "ground" else None

    def move(self):
        """ Movimentação personalizada para cada tipo de inimigo """
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.movement_type == "air":
            # Pássaro voa reto
            pass
        # se a opção e Entity for o Dog, ele tem comportamento de pular randomicamente (vindo da classe EntityBehavior)
        elif self.movement_type == "ground" and self.behavior:
            self.behavior.jump()
            self.behavior.update_jump()

    # Não usaremos o take_damage em obstáculos na fase demo!
    #def take_damage(self, damage):
    #    self.health -= damage

    def render(self, screen):
        self.update_animation()  # Atualiza o frame atual da animação
        screen.blit(self.surf, self.rect)  # Renderiza na tela
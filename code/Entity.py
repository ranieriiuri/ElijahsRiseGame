#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface = None):
        self.name = name
        self.sprite_sheet = sprite_sheet #carrega a SS diretamente
        self.frame_width = 64  #largura padrão (q é setada na var abaixo) p os quadros da sprite sheet
        self.frame_height = 64  #altura padrão (q é setada na var abaixo) p os quadros da sprite sheet
        self.rect = pygame.Rect(position[0], position[1], self.frame_width, self.frame_height)
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

        self.frames = []  # Lista para armazenar os quadros da animação
        self.current_frame = 0  # Controle do quadro atual
        self.animation_speed = 0.1  # Velocidade da animação (ajustável)

        self.load_frames() #metodo p carregar os quadros da sprite sheet

        self.surf = self.frames[0]  # O primeiro quadro da animação

    def load_frames(self):
        """Carrega os quadros da sprite sheet e os armazena em uma lista."""
        total_frames = self.sprite_sheet.get_width() // self.frame_width  # Número de quadros na sprite sheet
        for i in range(total_frames):
            frame = self.get_sprite(i)
            self.frames.append(frame)

    def get_sprite(self, frame_index):
        """Corta a sprite sheet para pegar um quadro específico."""
        x = frame_index * self.frame_width  # Posição X do quadro
        y = 0  # Supondo que todos os quadros estão em uma linha
        return self.sprite_sheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height))

    def update_animation(self):
        """Atualiza o quadro atual da animação."""
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.frames):
            self.current_frame = 0  # Reseta para o primeiro quadro

        self.surf = self.frames[int(self.current_frame)]  # Define a imagem do objeto com o quadro atual

    @abstractmethod
    def move(self):
        pass

    def render(self, screen):
        """Desenha a entidade na tela."""
        screen.blit(self.surf, self.rect)

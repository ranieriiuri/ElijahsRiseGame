import os
import pygame

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, EXPLOSION_FRAMES, EXPLOSION_SOUND
#from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Bird(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def render(self, screen):
            screen.blit(self.surf, self.rect)
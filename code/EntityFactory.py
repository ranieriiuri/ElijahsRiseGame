#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player
from code.Tree import Tree
from code.Wind import Wind


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg2{i}', (WIN_WIDTH, 0)))
                    list_bg.append(Background(f'Level1Bg3{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT / 2 - 30))
            case 'Tree':
                return Tree('Dog', (WIN_WIDTH + 10, WIN_HEIGHT - 40))
            case 'Wind':
                return Wind('Wind', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40))) #falta definir o movemento randomico do wind
            case 'Bird':
                return Enemy('Bird', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT / 3)), 'air') #Bird voa acima das árvores
            case 'Dog':
                return Enemy('Dog', (WIN_WIDTH + 10, WIN_HEIGHT - 40), 'ground')  # Dog corre no chão

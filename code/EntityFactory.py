#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
#from code.Enemy import Enemy
from code.Player import Player
from code.Dog import Dog
from code.Bird import Bird
from code.Tree import Tree
from code.Wind import Wind


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg2{i}', (WIN_WIDTH, 0)))
                    list_bg.append(Background(f'Level1Bg3{i}', (WIN_WIDTH, 0)))
                return list_bg
            #case 'Level2Bg':
            #    list_bg = []
            #    for i in range(5):  # level2bg images number
            #        list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
            #        list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
            #    return list_bg
            case 'Player':
                #lembrando q o constructor do player requer um nome e uma posição em tupla. Nos players definimos com constantes e os 2 iniciando em posições diferentes
                return Player('Player', (10, WIN_HEIGHT / 2 - 30))
            #case 'Player2':
            #    return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            #Já nos inimigos usamos a func 'randint' p gerá-los em posiçṍes iniciais randômicas (deixando o jogo mais dinâmico)
            case 'Tree':
                return Tree('Tree', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Wind':
                return Wind('Wind', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Bird':
                return Bird('Bird', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Dog':
                return Dog('Dog', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
import random
import pygame
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player
from code.Tree import Tree
from code.Wind import Wind

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):

        # Vars q carregam a sprite sheet uma vez e passam para as entidades na construção abaixo
        player_sprite_sheet = pygame.image.load('./assets/player_sprite_sheet.png').convert_alpha()
        bird_sprite_sheet = pygame.image.load('./assets/bird_sprite_sheet.png').convert_alpha()
        dog_sprite_sheet = pygame.image.load('./assets/dog_sprite_sheet.png').convert_alpha()
        wind_sprite_sheet = pygame.image.load('./assets/wind_sprite_sheet.png').convert_alpha()
        tree_sprite_sheet = pygame.image.load('./assets/tree_sprite_sheet.png').convert_alpha()
        mb_image = pygame.image.load('./asset/mb_image.png').convert_alpha()

        match entity_name:
            case 'Level':
                list_bg = []
                # 3 Bg diferentes, com suas camadas (nesse caso, assumindo que serão 7 de cada), ao terminar 1, carregar o outro em loop
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg2{i}', (WIN_WIDTH, 0)))
                    list_bg.append(Background(f'Level1Bg3{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT / 2 - 30), player_sprite_sheet, mb_image)  # Exemplo com bird
            case 'Tree':
                return Tree('Tree', (WIN_WIDTH + 10, WIN_HEIGHT - 40), tree_sprite_sheet)
            case 'Wind':
                return Wind('Wind', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), wind_sprite_sheet)
            case 'Bird':
                return Enemy('Bird', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT / 3)), bird_sprite_sheet, 'air')  # Passa sprite_sheet para o Bird
            case 'Dog':
                return Enemy('Dog', (WIN_WIDTH + 10, WIN_HEIGHT - 40), dog_sprite_sheet, 'ground')  # Passa sprite_sheet para o Dog

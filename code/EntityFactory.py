import random
import pygame
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT, BG_IMAGE_PATHS
from code.Enemy import Enemy
from code.MeatBread import MeatBread
from code.Player import Player
from code.Tree import Tree
from code.Wind import Wind

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        # Vars q carregam a sprite sheet uma vez e passam para as entidades na construção abaixo
        try:
            player_sprite_sheet = pygame.image.load('./asset/player_sprite_sheet.png').convert_alpha()
            # bird_sprite_sheet = pygame.image.load('./assets/bird_sprite_sheet.png').convert_alpha()
            dog_sprite_sheet = pygame.image.load('./asset/dog_sprite_sheet.png').convert_alpha()
            wind_sprite_sheet = pygame.image.load('./asset/wind_sprite_sheet.png').convert_alpha()
            tree_sprite_sheet = pygame.image.load('./asset/tree_sprite_sheet.png').convert_alpha()
            mb_image = pygame.image.load('./asset/mb_image.png').convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar sprite sheet: {e}")
            return None

        match entity_name:
            case 'Level1' | 'Level1Bg':
                list_bg = []
                for i, path in enumerate(BG_IMAGE_PATHS):
                    name = f'Level1Bg{i}'
                    list_bg.append(Background(name, (0, 0), path))
                    list_bg.append(Background(name, (WIN_WIDTH, 0), path))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT / 2 - 30), player_sprite_sheet, 8, 5)
            case 'Tree':
                return Tree('Tree', (WIN_WIDTH + 10, WIN_HEIGHT - 40), tree_sprite_sheet, 3, 5)
            case 'Wind':
                return Wind('Wind', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), wind_sprite_sheet, 2, 2)
            case 'Dog':
                return Enemy('Dog', (WIN_WIDTH + 10, WIN_HEIGHT - 40), dog_sprite_sheet, 'ground', 2, 3)
            # >> falta implementar o case do "Bird" <<
            case 'MeatBread':
                return MeatBread('MeatBread', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), mb_image) # usará no lugar da sprite sheet uma imagem estática, então, é só não passar 'rows' e 'cols', aí usa o padrão (1), ou seja, estática mesmo!



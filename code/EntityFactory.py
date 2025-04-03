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

        # Debug: Verifica se as imagens foram carregadas corretamente
        print(f"DEBUG: player_sprite_sheet -> {player_sprite_sheet}")
        print(f"DEBUG: dog_sprite_sheet -> {dog_sprite_sheet}")
        print(f"DEBUG: wind_sprite_sheet -> {wind_sprite_sheet}")
        print(f"DEBUG: tree_sprite_sheet -> {tree_sprite_sheet}")
        print(f"DEBUG: mb_image -> {mb_image}")

        match entity_name:
            case 'Level1' | 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT / 2 - 30), player_sprite_sheet, mb_image)
            case 'Tree':
                return Tree('Tree', (WIN_WIDTH + 10, WIN_HEIGHT - 40), tree_sprite_sheet)
            case 'Wind':
                return Wind('Wind', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), wind_sprite_sheet)
            case 'Dog':
                return Enemy('Dog', (WIN_WIDTH + 10, WIN_HEIGHT - 40), dog_sprite_sheet, 'ground')


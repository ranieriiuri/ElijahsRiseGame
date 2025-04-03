from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple, sprite_sheet: pygame.Surface = None, rows: int = 1, cols: int = 1):
        # os params de construção "sprite_sheet", "rows" e "cols" usam valores padrão, o q os torna opcionais p classes filhas que não os use
        self.name = name
        self.sprite_sheet = sprite_sheet #recebe a localização do arquivo sprite sheet (caso a class tenha)
        self.rows = rows  # Número de linhas na sprite sheet
        self.cols = cols  # Número de colunas na sprite sheet

        # os métodos em no param "sprite_sheet" vêm do pygame.Surface e pegam a largura e altura em pixels de uma imagem
        # tbm dividem esses valores pelas cols e rows passadas como param da class. caso a sprite sheet não seja fornecida, o valor será 64 pixels (um valor padrão).

        # Verifica se a sprite_sheet foi carregada corretamente
        if self.sprite_sheet is not None and isinstance(self.sprite_sheet, pygame.Surface):
            print(f"DEBUG: sprite_sheet = {self.sprite_sheet}") #debug lines
            print(f"DEBUG: rows = {self.rows}, cols = {self.cols}") #debug lines
            self.frame_width = self.sprite_sheet.get_width() // self.cols
            self.frame_height = self.sprite_sheet.get_height() // self.rows
        else:
            print(f"Erro: sprite_sheet inválida para {self.name}: {self.sprite_sheet}")
            self.frame_width = 64
            self.frame_height = 64

        # essa var seta os valores de altura e largura nas posicoes do "Rect"
        self.rect = pygame.Rect(position[0], position[1], self.frame_width, self.frame_height)

        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

        self.frames = [] # será usada nos metodos abaixo p armazanar os frames pegos
        self.current_frame = 0 # tbm p os métodos, frame inicial
        self.animation_speed = 0.1 # velocidade da mudança de frames (pode ser ajustada)

        # se a class tiver sprite sheet, chama o load_frames, q chama os outros métodos da animação
        if self.sprite_sheet:
            self.load_frames()

        self.surf = self.frames[0] if self.frames else None # seta um valor  0 na lista de frames se tiver, senão seta 'None'

    def load_frames(self):
        """Carrega os quadros da sprite sheet e os armazena em uma lista."""
        for row in range(self.rows):
            for col in range(self.cols):
                frame = self.get_sprite(row, col)
                self.frames.append(frame)

    def get_sprite(self, row_index, col_index):
        """Corta a sprite sheet para pegar um quadro específico."""
        x = col_index * self.frame_width  # Posição X na sprite sheet
        y = row_index * self.frame_height  # Posição Y na sprite sheet
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

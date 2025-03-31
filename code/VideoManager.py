import cv2
import pygame
import numpy as np
from code.Const import WIN_WIDTH, WIN_HEIGHT



class VideoManager:
    def __init__(self, window):
        self.window = window

    def play_video(self, video_path):
        # Abrindo o vídeo com OpenCV
        cap = cv2.VideoCapture(video_path)

        # Verificando se o vídeo foi carregado corretamente
        if not cap.isOpened():
            print("Erro ao carregar o vídeo.")
            return

        # Obtendo as propriedades do vídeo (como tamanho)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Calcula a escala de redimensionamento para manter a proporção do vídeo
        scale_width = WIN_WIDTH / width
        scale_height = WIN_HEIGHT / height
        scale = min(scale_width, scale_height)  # Usa o fator de escala menor para não distorcer o vídeo

        # Redimensiona as dimensões do vídeo para caber dentro da tela do jogo
        new_width = int(width * scale)
        new_height = int(height * scale)

        # Cria a superfície para desenhar o vídeo redimensionado
        video_surface = pygame.Surface((new_width, new_height))
        # Rodando o vídeo frame por frame
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convertendo a imagem de BGR (OpenCV) para RGB (Pygame)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convertendo o frame para um formato que o Pygame entende
            frame_surface = pygame.surfarray.make_surface(frame_rgb)

            # Atualizando a tela do Pygame com o novo frame
            self.window.blit(frame_surface, (0, 0))
            pygame.display.update()

            # Controlando o tempo de exibição (FPS)
            pygame.time.Clock().tick(30)

        # Fechando o vídeo
        cap.release()


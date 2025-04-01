import cv2
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT

class VideoManager:
    def __init__(self, window):
        self.window = window

    def play_video(self, video_path, audio_path):
        # Abrindo o vídeo com OpenCV
        cap = cv2.VideoCapture(video_path)

        # Verificando se o vídeo foi carregado corretamente
        if not cap.isOpened():
            print(f"Erro ao carregar o vídeo: {video_path}.")
            return

        # Obtendo as propriedades do vídeo (largura e altura)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Calcula a escala de redimensionamento para manter a proporção do vídeo
        scale_width = WIN_WIDTH / width
        scale_height = WIN_HEIGHT / height
        scale = min(scale_width, scale_height)  # Usa o menor fator para evitar distorção

        # Redimensiona as dimensões do vídeo para caber dentro da tela do jogo
        new_width = int(width * scale)
        new_height = int(height * scale)

        # Centraliza o vídeo na tela do Pygame
        x_offset = (WIN_WIDTH - new_width) // 2
        y_offset = (WIN_HEIGHT - new_height) // 2

        # Carregar e tocar o áudio (extraído para arquivo .mp3)
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play(-1)  # Toca o áudio indefinidamente

        # Criando o clock do Pygame para controlar FPS
        clock = pygame.time.Clock()

        # Loop para exibir o vídeo frame por frame
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break  # Sai do loop quando o vídeo termina

            # Redimensionando o frame para se ajustar à tela do jogo
            frame = cv2.resize(frame, (new_width, new_height))

            # Convertendo de BGR (OpenCV) para RGB (Pygame)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convertendo o frame para um formato compatível com o Pygame
            frame_surface = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))

            # Atualizando a tela do Pygame com o novo frame
            self.window.fill((0, 0, 0))  # Preenche o fundo para evitar artefatos visuais
            self.window.blit(frame_surface, (x_offset, y_offset))
            pygame.display.update()

            # Controlando o tempo de exibição (FPS)
            clock.tick(30)

        # Fechando o vídeo
        cap.release()
        pygame.mixer.music.stop()   # para audio após o video

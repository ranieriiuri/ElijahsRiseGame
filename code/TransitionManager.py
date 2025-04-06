import pygame

class TransitionManager:
    @staticmethod
    def fade_out(window, duration=2500):
        fade_surface = pygame.Surface(window.get_size()).convert_alpha()
        fade_surface.fill((0, 0, 0, 0))

        start_time = pygame.time.get_ticks()
        clock = pygame.time.Clock()

        while True:
            now = pygame.time.get_ticks()
            elapsed = now - start_time

            alpha = min(255, int(255 * (elapsed / duration)))
            fade_surface.fill((0, 0, 0, alpha))
            window.blit(fade_surface, (0, 0))
            pygame.display.update()

            if elapsed >= duration:
                break

            clock.tick(60)

    @staticmethod
    def fade_in(window, duration=2500):
        fade_surface = pygame.Surface(window.get_size()).convert_alpha()
        fade_surface.fill((0, 0, 0, 255))

        start_time = pygame.time.get_ticks()
        clock = pygame.time.Clock()

        while True:
            now = pygame.time.get_ticks()
            elapsed = now - start_time

            alpha = max(0, 255 - int(255 * (elapsed / duration)))
            fade_surface.fill((0, 0, 0, alpha))
            window.blit(fade_surface, (0, 0))
            pygame.display.update()

            if elapsed >= duration:
                break

            clock.tick(60)

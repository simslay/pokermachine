import os
import pygame


class PygamePage:
    def __init__(self):
        window_width = 1000
        window_height = 569

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()

        pygame.display.set_caption("Pokermachine")
        table_img = pygame.image.load('images/800px-Poker_Table.svg.png')
        table_rect = table_img.get_rect()
        table_rect.center = (window_width//2, window_height//2)
        # clock = pygame.time.Clock()

        screen = pygame.display.set_mode((window_width, window_height))

        end = False

        while not end:
            screen.fill((220, 220, 220))
            screen.blit(table_img, table_rect)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    end = True
            # pygame.display.flip() # mostly equivalent to pygame.display.update()
            pygame.display.update()
        pygame.quit()

        # while 1:
        #     pygame.display.update()
        #     clock.tick(60)

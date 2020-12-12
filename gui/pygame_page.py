import os
import pygame


class PygamePage:
    def __init__(self):
        window_width = 800
        window_height = 600

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()

        pygame.display.set_caption("Pokermachine")
        table_img = pygame.image.load('images/600px-Poker_Table.svg.png')
        table_rect = table_img.get_rect()
        table_rect.center = (window_width//2, 250)
        # clock = pygame.time.Clock()

        screen = pygame.display.set_mode((window_width, window_height))

        south_cards = pygame.image.load('images/600px-2Cards_South.svg.png')
        north_cards = pygame.image.load('images/600px-2Cards_North.svg.png')
        south_east_cards = pygame.image.load('images/600px-2Cards_South-East.svg.png')
        south_west_cards = pygame.image.load('images/600px-2Cards_South-West.svg.png')
        north_east_cards = pygame.image.load('images/600px-2Cards_North-East.svg.png')
        north_west_cards = pygame.image.load('images/600px-2Cards_North-West.svg.png')

        end = False

        while not end:
            screen.fill((220, 220, 220))
            screen.blit(table_img, table_rect)
            screen.blit(south_cards, (window_width//2-53//2, window_height//2+32))
            screen.blit(north_cards, (window_width//2-53//2, 117))
            screen.blit(south_east_cards, (window_width-217, window_height//2-6))
            screen.blit(south_west_cards, (163, window_height//2-6))
            screen.blit(north_east_cards, (window_width-217, 144))
            screen.blit(north_west_cards, (166, 144))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    end = True
            # pygame.display.flip() # mostly equivalent to pygame.display.update()
            pygame.display.update()
        pygame.quit()

        # while 1:
        #     pygame.display.update()
        #     clock.tick(60)

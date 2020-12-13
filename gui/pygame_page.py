import os
import pygame


class PygamePage:
    def __init__(self, game_info_q):
        window_width = 800
        window_height = 700
        font_color = (255, 255, 255)
        font_background = (0, 0, 0)
        self.game = game_info_q.get()
        self.player1 = self.game.state.players[0]
        self.player2 = self.game.state.players[1]
        self.player3 = None
        self.player4 = None
        self.player5 = None

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()

        font = pygame.font.Font(None, 24)
        chips_font = pygame.font.Font(None, 20)
        button_font = pygame.font.Font(None, 50)

        pygame.display.set_caption("Pokermachine")
        table_img = pygame.image.load('images/600px-Poker_Table.svg.png')
        table_rect = table_img.get_rect()
        table_rect.center = (window_width//2, 300)
        # clock = pygame.time.Clock()

        screen = pygame.display.set_mode((window_width, window_height))

        south_table_cards = pygame.image.load('images/600px-2Cards_South.svg.png')
        north_table_cards = pygame.image.load('images/600px-2Cards_North.svg.png')
        south_table_east_cards = pygame.image.load('images/600px-2Cards_South-East.svg.png')
        south_west_table_cards = pygame.image.load('images/600px-2Cards_South-West.svg.png')
        north_east_table_cards = pygame.image.load('images/600px-2Cards_North-East.svg.png')
        north_west_table_cards = pygame.image.load('images/600px-2Cards_North-West.svg.png')

        south_card1 = pygame.image.load('images/cards/' + str(self.player1.cards[0]) + '.png')
        south_card1 = pygame.transform.scale(south_card1, (691//10, 1056//10))
        south_card2 = pygame.image.load('images/cards/' + str(self.player1.cards[1]) + '.png')
        south_card2 = pygame.transform.scale(south_card2, (691 // 10, 1056 // 10))
        p1_t = font.render(self.player1.name, True, font_color, font_background)
        p1_t_rect = p1_t.get_rect()
        p1_t_rect.x, p1_t_rect.y = window_width//2-53//2, window_height//2+32+70-18
        ch1_t = chips_font.render(str(self.game.starting_chips) + " chips", True, font_color, font_background)
        ch1_t_rect = ch1_t.get_rect()
        ch1_t_rect.x, ch1_t_rect.y = window_width//2-53//2, window_height//2+32+70+1056//10

        south_west_card1 = pygame.image.load('images/cards/' + str(self.player2.cards[0]) + '.png')
        south_west_card1 = pygame.transform.scale(south_west_card1, (691 // 10, 1056 // 10))
        south_west_card2 = pygame.image.load('images/cards/' + str(self.player2.cards[1]) + '.png')
        south_west_card2 = pygame.transform.scale(south_west_card2, (691 // 10, 1056 // 10))
        p2_t = font.render(self.player2.name, True, font_color, font_background)
        p2_t_rect = p2_t.get_rect()
        p2_t_rect.x, p2_t_rect.y = 40, window_height//2-6-18
        ch2_t = chips_font.render(str(self.game.starting_chips) + " chips", True, font_color, font_background)
        ch2_t_rect = ch2_t.get_rect()
        ch2_t_rect.x, ch2_t_rect.y = 40, window_height//2-6+1056//10

        north_west_card1 = None
        north_west_card2 = None
        p3_t = None
        p3_t_rect = None
        ch3_t = None
        ch3_t_rect = None

        if len(self.game.state.players) > 2:
            self.player3 = self.game.state.players[2]
            north_west_card1 = pygame.image.load('images/cards/' + str(self.player3.cards[0]) + '.png')
            north_west_card1 = pygame.transform.scale(north_west_card1, (691 // 10, 1056 // 10))
            north_west_card2 = pygame.image.load('images/cards/' + str(self.player3.cards[1]) + '.png')
            north_west_card2 = pygame.transform.scale(north_west_card2, (691 // 10, 1056 // 10))
            p3_t = font.render(self.player3.name, True, font_color, font_background)
            p3_t_rect = p3_t.get_rect()
            p3_t_rect.x, p3_t_rect.y = 40, 144-1056//10+45-18+50
            ch3_t = chips_font.render(str(self.player3.chips) + " chips", True, font_color, font_background)
            ch3_t_rect = ch3_t.get_rect()
            ch3_t_rect.x, ch3_t_rect.y = 40, 144+45+50

        north_card1 = None
        north_card2 = None
        p4_t = None
        p4_t_rect = None
        ch4_t = None
        ch4_t_rect = None

        if len(self.game.state.players) > 3:
            self.player4 = self.game.state.players[3]
            north_card1 = pygame.image.load('images/cards/' + str(self.player4.cards[0]) + '.png')
            north_card1 = pygame.transform.scale(north_card1, (691 // 10, 1056 // 10))
            north_card2 = pygame.image.load('images/cards/' + str(self.player4.cards[1]) + '.png')
            north_card2 = pygame.transform.scale(north_card2, (691 // 10, 1056 // 10))
            p4_t = font.render(self.player4.name, True, font_color, font_background)
            p4_t_rect = p4_t.get_rect()
            p4_t_rect.x, p4_t_rect.y = window_width//2-53//2, 2
            ch4_t = chips_font.render(str(self.player4.chips) + " chips", True, font_color, font_background)
            ch4_t_rect = ch4_t.get_rect()
            ch4_t_rect.x, ch4_t_rect.y = window_width//2-53//2, 2+1056//10+18

        north_east_card1 = None
        north_east_card2 = None
        p5_t = None
        p5_t_rect = None
        ch5_t = None
        ch5_t_rect = None

        if len(self.game.state.players) > 4:
            self.player5 = self.game.state.players[4]
            north_east_card1 = pygame.image.load('images/cards/' + str(self.player5.cards[0]) + '.png')
            north_east_card1 = pygame.transform.scale(north_east_card1, (691 // 10, 1056 // 10))
            north_east_card2 = pygame.image.load('images/cards/' + str(self.player5.cards[1]) + '.png')
            north_east_card2 = pygame.transform.scale(north_east_card2, (691 // 10, 1056 // 10))
            p5_t = font.render(self.player5.name, True, font_color, font_background)
            p5_t_rect = p5_t.get_rect()
            p5_t_rect.x, p5_t_rect.y = window_width-65-691//10, 144-1056//10+45-18+50
            ch5_t = chips_font.render(str(self.player4.chips) + " chips", True, font_color, font_background)
            ch5_t_rect = ch5_t.get_rect()
            ch5_t_rect.x, ch5_t_rect.y = window_width-65-691//10, 144+45+50

        red = (200, 0, 0)
        size = (200, 100)

        rect_border = pygame.Surface(size)
        pygame.draw.rect(rect_border, red, rect_border.get_rect(), 10)

        rect_filled = pygame.Surface(size)
        pygame.draw.rect(rect_filled, red, rect_filled.get_rect())

        fold_button_t = button_font.render("Fold", True, font_color, font_background)
        fold_button_t_rect = fold_button_t.get_rect()
        fold_button_t_rect.x, fold_button_t_rect.y = 200//2, window_height-100+100//2

        check_button_t = button_font.render("Check", True, font_color, font_background)
        check_button_t_rect = check_button_t.get_rect()
        check_button_t_rect.x, check_button_t_rect.y = 200+140//2, window_height-100+100//2

        raise_button_t = button_font.render("Raise", True, font_color, font_background)
        raise_button_t_rect = raise_button_t.get_rect()
        raise_button_t_rect.x, raise_button_t_rect.y = 200+180+200//2, window_height-100+100//2

        end = False

        while not end:
            screen.fill((220, 220, 220))
            screen.blit(table_img, table_rect)

            screen.blit(rect_filled, (0, window_height-100))
            screen.blit(rect_border, (0, window_height-100))
            screen.blit(fold_button_t, fold_button_t_rect)

            screen.blit(rect_filled, (200, window_height-100))
            screen.blit(rect_border, (200, window_height-100))
            screen.blit(check_button_t, check_button_t_rect)

            screen.blit(rect_filled, (400, window_height-100))
            screen.blit(rect_border, (400, window_height-100))
            screen.blit(raise_button_t, raise_button_t_rect)

            screen.blit(south_table_cards, (window_width//2-53//2, window_height//2+32))
            screen.blit(south_card1, (window_width//2-53//2, window_height//2+32+70))
            screen.blit(south_card2, (window_width//2, window_height//2+32+70))
            screen.blit(p1_t, p1_t_rect)
            screen.blit(ch1_t, ch1_t_rect)

            screen.blit(south_west_table_cards, (163, window_height//2-6))
            screen.blit(south_west_card1, (40, window_height//2-6))
            screen.blit(south_west_card2, (60, window_height//2-6))
            screen.blit(p2_t, p2_t_rect)
            screen.blit(ch2_t, ch2_t_rect)

            if len(self.game.state.players) > 2:
                screen.blit(north_west_table_cards, (166, 144+50))
                screen.blit(north_west_card1, (40, 144-1056//10+45+50))
                screen.blit(north_west_card2, (60, 144-1056//10+45+50))
                screen.blit(p3_t, p3_t_rect)
                screen.blit(ch3_t, ch3_t_rect)

            if len(self.game.state.players) > 3:
                screen.blit(north_table_cards, (window_width//2-53//2, 117+30))
                screen.blit(north_card1, (window_width//2-53//2, 10+10))
                screen.blit(north_card2, (window_width//2, 10+10))
                screen.blit(p4_t, p4_t_rect)
                screen.blit(ch4_t, ch4_t_rect)

            if len(self.game.state.players) > 4:
                screen.blit(north_east_table_cards, (window_width - 217, 144+50))
                screen.blit(north_east_card1, (window_width-65-691//10, 144-1056//10+45+50))
                screen.blit(north_east_card2, (window_width-45-691//10, 144-1056//10+45+50))
                screen.blit(p5_t, p5_t_rect)
                screen.blit(ch5_t, ch5_t_rect)

            if len(self.game.state.players) > 5:
                screen.blit(south_table_east_cards, (window_width-217, window_height//2-6))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    end = True
            # pygame.display.flip() # mostly equivalent to pygame.display.update()
            pygame.display.update()
        pygame.quit()

        # while 1:
        #     pygame.display.update()
        #     clock.tick(60)

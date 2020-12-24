import os
import pygame
from gui.input_box import InputBox


class PygamePage:
    def __init__(self, n, game, player_name):
        print("Initialize game page")
        self.window_width = 800
        self.window_height = 700
        window_width = self.window_width
        window_height = self.window_height
        self.font_color = (255, 255, 255)
        self.font_background = (0, 0, 0)
        self.n = n
        self.game = game
        print("Players:", str(self.game.state.players))
        self.player1 = self.game.state.players_not_out[0]
        self.player2 = self.game.state.players_not_out[1]
        self.player3 = None
        self.player4 = None
        self.player5 = None
        self.player_name = player_name
        self.player = game.get_player(player_name)
        self.actions_available = None

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()

        font_color = self.font_color
        font_background = self.font_background

        font = pygame.font.Font(None, 24)
        self.chips_font = pygame.font.Font(None, 20)
        button_font = pygame.font.Font(None, 50)

        pygame.display.set_caption("Pokermachine")
        # clock = pygame.time.Clock()

        screen = pygame.display.set_mode((window_width, window_height))
        self.screen = screen

        self.table_img = pygame.image.load('images/600px-Poker_Table.svg.png')
        self.table_rect = self.table_img.get_rect()
        self.table_rect.center = (window_width // 2, 300)

        self.south_table_cards = pygame.image.load('images/600px-2Cards_South.svg.png')
        self.north_table_cards = pygame.image.load('images/600px-2Cards_North.svg.png')
        self.south_east_table_cards = pygame.image.load('images/600px-2Cards_South-East.svg.png')
        self.south_west_table_cards = pygame.image.load('images/600px-2Cards_South-West.svg.png')
        self.north_east_table_cards = pygame.image.load('images/600px-2Cards_North-East.svg.png')
        self.north_west_table_cards = pygame.image.load('images/600px-2Cards_North-West.svg.png')
        self.button_img = pygame.image.load('images/600px-Button.svg.png')
        self.one_chip_img = pygame.image.load('images/600px-1chip.svg.png')
        self.two_chips_img = pygame.image.load('images/600px-2chips.svg.png')

        self.south_card1 = pygame.image.load('images/cards/' + str(self.player1.cards[0]) + '.png')
        self.south_card1 = pygame.transform.scale(self.south_card1, (691//10, 1056//10))
        self.south_card2 = pygame.image.load('images/cards/' + str(self.player1.cards[1]) + '.png')
        self.south_card2 = pygame.transform.scale(self.south_card2, (691 // 10, 1056 // 10))
        self.p1_t = font.render(self.player1.name, True, font_color, font_background)
        self.p1_t_rect = self.p1_t.get_rect()
        self.p1_t_rect.x, self.p1_t_rect.y = window_width//2-53//2, window_height//2+32+70-18
        self.ch1_t = self.chips_font.render(str(self.player1.stake) + " chips", True, font_color, font_background)
        self.ch1_t_rect = self.ch1_t.get_rect()
        self.ch1_t_rect.x, self.ch1_t_rect.y = window_width//2-53//2, window_height//2+32+70+1056//10

        self.south_west_card1 = pygame.image.load('images/cards/' + str(self.player2.cards[0]) + '.png')
        self.south_west_card1 = pygame.transform.scale(self.south_west_card1, (691 // 10, 1056 // 10))
        self.south_west_card2 = pygame.image.load('images/cards/' + str(self.player2.cards[1]) + '.png')
        self.south_west_card2 = pygame.transform.scale(self.south_west_card2, (691 // 10, 1056 // 10))
        self.p2_t = font.render(self.player2.name, True, font_color, font_background)
        self.p2_t_rect = self.p2_t.get_rect()
        self.p2_t_rect.x, self.p2_t_rect.y = 40, window_height//2-6-18
        self.ch2_t = self.chips_font.render(str(self.player2.stake) + " chips", True, font_color, font_background)
        self.ch2_t_rect = self.ch2_t.get_rect()
        self.ch2_t_rect.x, self.ch2_t_rect.y = 40, window_height//2-6+1056//10

        self.north_west_card1 = None
        self.north_west_card2 = None
        self.p3_t = None
        self.p3_t_rect = None
        self.ch3_t = None
        self.ch3_t_rect = None

        if len(self.game.state.players) > 2:
            self.player3 = self.game.state.players[2]
            self.north_west_card1 = pygame.image.load('images/cards/' + str(self.player3.cards[0]) + '.png')
            self.north_west_card1 = pygame.transform.scale(self.north_west_card1, (691 // 10, 1056 // 10))
            self.north_west_card2 = pygame.image.load('images/cards/' + str(self.player3.cards[1]) + '.png')
            self.north_west_card2 = pygame.transform.scale(self.north_west_card2, (691 // 10, 1056 // 10))
            self.p3_t = font.render(self.player3.name, True, font_color, font_background)
            self.p3_t_rect = self.p3_t.get_rect()
            self.p3_t_rect.x, self.p3_t_rect.y = 40, 144-1056//10+45-18+50
            self.ch3_t = self.chips_font.render(str(self.player3.stake) + " chips", True, font_color, font_background)
            self.ch3_t_rect = self.ch3_t.get_rect()
            self.ch3_t_rect.x, self.ch3_t_rect.y = 40, 144+45+50

        self.north_card1 = None
        self.north_card2 = None
        self.p4_t = None
        self.p4_t_rect = None
        self.ch4_t = None
        self.ch4_t_rect = None

        if len(self.game.state.players) > 3:
            self.player4 = self.game.state.players[3]
            self.north_card1 = pygame.image.load('images/cards/' + str(self.player4.cards[0]) + '.png')
            self.north_card1 = pygame.transform.scale(self.north_card1, (691 // 10, 1056 // 10))
            self.north_card2 = pygame.image.load('images/cards/' + str(self.player4.cards[1]) + '.png')
            self.north_card2 = pygame.transform.scale(self.north_card2, (691 // 10, 1056 // 10))
            self.p4_t = font.render(self.player4.name, True, font_color, font_background)
            self.p4_t_rect = self.p4_t.get_rect()
            self.p4_t_rect.x, self.p4_t_rect.y = window_width//2-53//2, 2
            self.ch4_t = self.chips_font.render(str(self.player4.stake) + " chips", True, font_color, font_background)
            self.ch4_t_rect = self.ch4_t.get_rect()
            self.ch4_t_rect.x, self.ch4_t_rect.y = window_width//2-53//2, 2+1056//10+18

        self.north_east_card1 = None
        self.north_east_card2 = None
        self.p5_t = None
        self.p5_t_rect = None
        self.ch5_t = None
        self.ch5_t_rect = None

        if len(self.game.state.players) > 4:
            self.player5 = self.game.state.players[4]
            self.north_east_card1 = pygame.image.load('images/cards/' + str(self.player5.cards[0]) + '.png')
            self.north_east_card1 = pygame.transform.scale(self.north_east_card1, (691 // 10, 1056 // 10))
            self.north_east_card2 = pygame.image.load('images/cards/' + str(self.player5.cards[1]) + '.png')
            self.north_east_card2 = pygame.transform.scale(self.north_east_card2, (691 // 10, 1056 // 10))
            self.p5_t = font.render(self.player5.name, True, font_color, font_background)
            self.p5_t_rect = self.p5_t.get_rect()
            self.p5_t_rect.x, self.p5_t_rect.y = window_width-65-691//10, 144-1056//10+45-18+50
            self.ch5_t = self.chips_font.render(str(self.player5.stake) + " chips", True, font_color, font_background)
            self.ch5_t_rect = self.ch5_t.get_rect()
            self.ch5_t_rect.x, self.ch5_t_rect.y = window_width-65-691//10, 144+45+50

        self.fold_button_t = button_font.render("Fold", True, font_color, font_background)
        self.fold_button_t_rect = self.fold_button_t.get_rect()
        self.fold_button_t_rect.x, self.fold_button_t_rect.y = 200//2, window_height-100+100//2

        self.check_button_t = button_font.render("Check", True, font_color, font_background)
        self.check_button_t_rect = self.check_button_t.get_rect()
        self.check_button_t_rect.x, self.check_button_t_rect.y = 170+200//2, window_height-100+100//2

        self.call_button_t = button_font.render("Call", True, font_color, font_background)
        self.call_button_t_rect = self.call_button_t.get_rect()
        self.call_button_t_rect.x, self.call_button_t_rect.y = 205+200//2, window_height-100+100//2

        self.bet_button_t = button_font.render("Bet", True, font_color, font_background)
        self.bet_button_t_rect = self.bet_button_t.get_rect()
        self.bet_button_t_rect.x, self.bet_button_t_rect.y = 200+220+200//2, window_height-100+100//2

        self.raise_button_t = button_font.render("Raise", True, font_color, font_background)
        self.raise_button_t_rect = self.raise_button_t.get_rect()
        self.raise_button_t_rect.x, self.raise_button_t_rect.y = 200+180+200//2, window_height-100+100//2

        self.rect_border = None
        self.rect_filled = None

        self.update_screen()

    def update_screen(self):
        screen = self.screen
        clock = pygame.time.Clock()
        raise_input_box = InputBox(600, self.window_height - 50, 50, 32)
        fold_available = False
        check_available = False
        call_available = False
        bet_available = False
        raise_available = False
        run = True

        while run:
            screen.fill((220, 220, 220))
            screen.blit(self.table_img, self.table_rect)

            game = self.n.send("get/")
            player = game.get_player(self.player_name)

            if game.state.player_count == 2:
                if game.state.dealer_index == 0:
                    screen.blit(self.one_chip_img,
                                (self.window_width // 2 - 53 // 2 + 30, self.window_height // 2 - 10))
                    screen.blit(self.two_chips_img, (163 + 40, self.window_height // 2 - 30))
                    screen.blit(self.button_img, (self.window_width // 2 - 53 // 2 - 10, self.window_height // 2 - 10))
                else:
                    screen.blit(self.one_chip_img, (163 + 45 + 15, self.window_height // 2 - 5))
                    screen.blit(self.two_chips_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                    screen.blit(self.button_img, (163 + 45 - 20, self.window_height // 2 - 40))

            if game.state.player_count == 3:
                if game.state.dealer_index == 0:
                    screen.blit(self.one_chip_img, (163 + 45, self.window_height // 2 - 25))
                    screen.blit(self.two_chips_img, (166 + 50, 144 + 50 + 30))
                    screen.blit(self.button_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                elif game.state.dealer_index == 1:
                    screen.blit(self.one_chip_img, (166 + 50, 144 + 50 + 30))
                    screen.blit(self.two_chips_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                    screen.blit(self.button_img, (163 + 45, self.window_height // 2 - 25))
                else:
                    screen.blit(self.one_chip_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                    screen.blit(self.two_chips_img, (163 + 45, self.window_height // 2 - 25))
                    screen.blit(self.button_img, (166 + 50, 144 + 50 + 30))

            if game.state.player_count == 4:
                if game.state.dealer_index == 0:
                    screen.blit(self.one_chip_img, (163 + 45, self.window_height // 2 - 25))
                    screen.blit(self.two_chips_img, (166 + 50, 144 + 50 + 30))
                    screen.blit(self.button_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                elif game.state.dealer_index == 1:
                    screen.blit(self.one_chip_img, (166 + 50, 144 + 50 + 30))
                    screen.blit(self.two_chips_img, (self.window_width // 2 - 53 // 2, 117 + 105))
                    screen.blit(self.button_img, (163 + 45, self.window_height // 2 - 25))
                elif game.state.dealer_index == 2:
                    screen.blit(self.one_chip_img, (self.window_width // 2 - 53 // 2, 117 + 105))
                    screen.blit(self.two_chips_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                    screen.blit(self.button_img, (166 + 50, 144 + 50 + 30))
                else:
                    screen.blit(self.one_chip_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                    screen.blit(self.two_chips_img, (163 + 45, self.window_height // 2 - 25))
                    screen.blit(self.button_img, (self.window_width // 2 - 53 // 2, 117 + 105))

            if game.state.player_count == 5:
                if game.state.dealer_index == 0:
                    screen.blit(self.one_chip_img, (163 + 45, self.window_height // 2 - 25))
                    screen.blit(self.two_chips_img, (166 + 50, 144 + 50 + 30))
                    screen.blit(self.button_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                elif game.state.dealer_index == 1:
                    screen.blit(self.one_chip_img, (166 + 50, 144 + 50 + 30))
                    screen.blit(self.two_chips_img, (self.window_width // 2 - 53 // 2, 117 + 105))
                    screen.blit(self.button_img, (163 + 45, self.window_height // 2 - 25))
                elif game.state.dealer_index == 2:
                    screen.blit(self.one_chip_img, (self.window_width // 2 - 53 // 2, 117 + 105))
                    screen.blit(self.two_chips_img, (self.window_width - 217 - 35, 144 + 50 + 40))
                    screen.blit(self.button_img, (166 + 50, 144 + 50 + 30))
                elif game.state.dealer_index == 3:
                    screen.blit(self.one_chip_img, (self.window_width - 217 - 35, 144 + 50 + 40))
                    screen.blit(self.two_chips_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                    screen.blit(self.button_img, (self.window_width // 2 - 53 // 2, 117 + 105))
                elif game.state.dealer_index == 4:
                    screen.blit(self.one_chip_img, (self.window_width // 2 - 53 // 2, self.window_height // 2 - 10))
                    screen.blit(self.two_chips_img, (163 + 45, self.window_height // 2 - 25))
                    screen.blit(self.button_img, (self.window_width - 217 - 35, 144 + 50 + 40))

            if game.state.current_player == player and not player.action_done:
                red = (200, 0, 0)
                size = (200, 100)

                self.rect_border = pygame.Surface(size)
                pygame.draw.rect(self.rect_border, red, self.rect_border.get_rect(), 10)

                self.rect_filled = pygame.Surface(size)
                pygame.draw.rect(self.rect_filled, red, self.rect_filled.get_rect())

                screen.blit(self.rect_filled, (0, self.window_height - 100))
                screen.blit(self.rect_border, (0, self.window_height - 100))
                screen.blit(self.fold_button_t, self.fold_button_t_rect)
                fold_available = True

                if game.state.current_bet == player.bet:
                    screen.blit(self.rect_filled, (200, self.window_height - 100))
                    screen.blit(self.rect_border, (200, self.window_height - 100))
                    screen.blit(self.check_button_t, self.check_button_t_rect)
                    check_available = True
                else:
                    screen.blit(self.rect_filled, (200, self.window_height - 100))
                    screen.blit(self.rect_border, (200, self.window_height - 100))
                    screen.blit(self.call_button_t, self.call_button_t_rect)
                    call_available = True

                if game.state.current_bet == 0:
                    screen.blit(self.rect_filled, (400, self.window_height - 100))
                    screen.blit(self.rect_border, (400, self.window_height - 100))
                    screen.blit(self.bet_button_t, self.bet_button_t_rect)
                    bet_available = True
                else:
                    screen.blit(self.rect_filled, (400, self.window_height - 100))
                    screen.blit(self.rect_border, (400, self.window_height - 100))
                    screen.blit(self.raise_button_t, self.raise_button_t_rect)
                    raise_available = True

                self.actions_available = True
            else:
                self.actions_available = False

            # if player.action_done:
            #     print("You've made your action")

            self.ch1_t = self.chips_font.render(
                str(game.state.players_not_out[0].stake) + " chips", True, self.font_color, self.font_background)
            self.ch2_t = self.chips_font.render(
                str(game.state.players_not_out[1].stake) + " chips", True, self.font_color, self.font_background)

            screen.blit(self.south_table_cards, (self.window_width // 2 - 53 // 2, self.window_height // 2 + 32))
            screen.blit(self.south_card1, (self.window_width // 2 - 53 // 2, self.window_height // 2 + 32 + 70))
            screen.blit(self.south_card2, (self.window_width // 2, self.window_height // 2 + 32 + 70))
            screen.blit(self.p1_t, self.p1_t_rect)
            screen.blit(self.ch1_t, self.ch1_t_rect)

            screen.blit(self.south_west_table_cards, (163, self.window_height // 2 - 6))
            screen.blit(self.south_west_card1, (40, self.window_height // 2 - 6))
            screen.blit(self.south_west_card2, (60, self.window_height // 2 - 6))
            screen.blit(self.p2_t, self.p2_t_rect)
            screen.blit(self.ch2_t, self.ch2_t_rect)

            if len(game.state.players) > 2:
                screen.blit(self.north_west_table_cards, (166, 144 + 50))
                screen.blit(self.north_west_card1, (40, 144 - 1056 // 10 + 45 + 50))
                screen.blit(self.north_west_card2, (60, 144 - 1056 // 10 + 45 + 50))
                screen.blit(self.p3_t, self.p3_t_rect)
                screen.blit(self.ch3_t, self.ch3_t_rect)

            if len(game.state.players) > 3:
                screen.blit(self.north_table_cards, (self.window_width // 2 - 53 // 2, 117 + 50))
                screen.blit(self.north_card1, (self.window_width // 2 - 53 // 2, 10 + 10))
                screen.blit(self.north_card2, (self.window_width // 2, 10 + 10))
                screen.blit(self.p4_t, self.p4_t_rect)
                screen.blit(self.ch4_t, self.ch4_t_rect)

            if len(game.state.players) > 4:
                screen.blit(self.north_east_table_cards, (self.window_width - 217, 144 + 50))
                screen.blit(self.north_east_card1, (self.window_width - 65 - 691 // 10, 144 - 1056 // 10 + 45 + 50))
                screen.blit(self.north_east_card2, (self.window_width - 45 - 691 // 10, 144 - 1056 // 10 + 45 + 50))
                screen.blit(self.p5_t, self.p5_t_rect)
                screen.blit(self.ch5_t, self.ch5_t_rect)

            if len(game.state.players) > 5:
                screen.blit(self.south_east_table_cards, (self.window_width - 217, self.window_height // 2 - 6))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    # if event.key == pygame.K_RETURN:
                    #     self.game.state.deal_flop()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if raise_available:
                    raise_input_box.handle_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.actions_available:
                        x, y = event.pos
                        if 0 < x < 200 and self.window_height > y > self.window_height - 100:
                            if fold_available:
                                print("Clicked on fold")
                                self.n.send("action/fold/" + self.player_name)
                                fold_available = False
                        if 200 < x < 400 and self.window_height > y > self.window_height - 100:
                            if call_available:
                                print("Clicked on call")
                                self.n.send("action/call/" + self.player_name)
                                call_available = False
                            elif check_available:
                                print("Clicked on check")
                                self.n.send("action/check/" + self.player_name)
                                check_available = False
                        if 400 < x < 600 and self.window_height > y > self.window_height - 100:
                            if bet_available:
                                print('Clicked on bet')
                                self.n.send("action/bet/" + self.player_name)
                                bet_available = False
                            elif raise_available:
                                print('Clicked on raise')
                                self.n.send("action/raise/" + self.player_name)
                                raise_available = False

            if raise_available:
                raise_input_box.update()
                raise_input_box.draw(screen)

            # pygame.display.flip()  # mostly equivalent to pygame.display.update()
            pygame.display.update()
            clock.tick(30)
        pygame.quit()

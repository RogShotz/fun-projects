class Skyjo:
    player_count = -1
    players = -1
    round_number = 1
    starting_player = -1
    turn = 1

    # bot_pos is always 1, other players are registered in a clockwise fashion
    def __init__(self, player_count: int):
        self.player_count = player_count

    def init_game(self):
        self.players = [{'Score': 0, 'Cards': [-1]*12} for i in range(self.player_count)]

    def start_round(self):

        i = 0
        while i < self.player_count:
            plr_num = input('Input Player #:\n')
            try:
                plr_num = int(plr_num) - 1
            except:
                print(f'Player number {plr_num}, was not valid')
                continue
            plr_start_card = print(f'Player_{plr_num} Starting Cards {{Card_Index Card_Value}} \n')
            # loop twice to get both starting card values
            j = 0
            while j < 2:
                card_i, card_val = self.input_card()
                if card_i == - 1:
                    continue
                
                self.players[plr_num]['Cards'][card_i-1] = [card_val]
                j += 1
        
            print(self)
            i += 1
        
        if self.starting_player == -1:
            self.game_starting_player() # if for some reason you don't want to start first round with highest player

        while True:
            self.start_turn()
        return
    
    def start_turn(self):   #TODO: Make turns
        if self.turn == 1:
            pass
        return

    def end_round(self):
        self.round_number += 1

    def game_starting_player(self):
        response = ''
        game_starting_plr = -1
        while response != 'y' and response != 'Y':
            game_starting_plr = input('Starting from the bot/assisted player position 1 and incrementing clockwise, which player starts this game?\n')
            try:
                game_starting_plr = int(game_starting_plr) - 1
            except:
                print(f'Player number {game_starting_plr}, was not valid')
                continue

            response = input(f'Player: {game_starting_plr + 1} is the starting player of the game? (y/n)\n')
        self.starting_player = game_starting_plr
    
    def start_game(self):
        self.init_game()
        print(f'Starting {self.player_count} Player Game...\n')
        self.start_round()

    # Index starts at 1 for the first card
    def input_card(self):   #TODO: Make input sanitization so that you can rewrite mis-inputted cards with proper prompts and it keeps asking till all cards needed to start are consumed
        card = input(f'Input Card: ').split()
        try:
            card_i = int(card[0])
            card_val = int(card[1])
            if card_i < 1 or card_i > 12:
                print(f'Index of {card_i}, was not valid')
                return -1, -1
            if card_val < -2 or card_val > 12:
                print(f'Value of {card_i}, was not valid')
                return -1, -1
            
            return card_i, card_val
        except:
            print(f'Input: {card} was incorrect, follow the format:\n\'card_index card_value\'')
            return -1, -1

    def __str__(self):
        players_f_str = ''
        for i, player in enumerate(self.players):
            players_f_str += f'Player_{i+1}{' (you)' if i == 0 else ''}:\nScore: {player['Score']}\nCards: {player['Cards']}\n\n'

        players_f_str = players_f_str[:-2] # removes last two \n's
        return f"player_count = {self.player_count}\n\n{players_f_str}"


game = Skyjo(4)
game.start_game()

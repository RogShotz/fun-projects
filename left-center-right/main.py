import random
import time



PLAYERS_NUM = 6
SIMULATED_GAMES = 1_000_00

def give_player_money(players_arr, direction, i):
    """
    Give money to the player in the specified direction.
    
    :param players_arr: list of players
    :param direction: 'left' or 'right'
    :param i: index of the current player
    """
    if direction == 'left':
        players_arr[i]['money'] -= 1
        players_arr[i % PLAYERS_NUM]['money'] += 1
    elif direction == 'right':
        players_arr[i]['money'] -= 1
        players_arr[(i + 1) % PLAYERS_NUM]['money'] += 1

    return players_arr

def run_game(): # Setting up players
    players = []
    for i in range(PLAYERS_NUM):
        players.append({'name': f'Player {i + 1}', 'money': 3})


    # Game logic
    turn_pos = 0
    while True:
        # Players rolls dice for how much money they have
        if players[turn_pos]['money'] > 0:
            for i in range(min(players[turn_pos]['money'], 1)):
                roll = random.randrange(1, 7)
                # Do nothing
                if roll <= 3:
                    pass
                # Give the player to the left money
                elif roll == 4:
                    players = give_player_money(players, 'left', turn_pos)
                # Put money in the center
                elif roll == 5:
                # Give the player to the right money
                    players[turn_pos]['money'] -= 1
                elif roll == 6:
                    players = give_player_money(players, 'right', turn_pos)

        active_players = 0
        for i in range(PLAYERS_NUM):
            if players[i]['money'] > 0:
                active_players += 1
            if active_players == 2:
                break
        if active_players < 2:
            break
        active_players = 0
        turn_pos = (turn_pos + 1) % PLAYERS_NUM

    # Validator, for checking if the end game state is correct

    winners = 0
    winner_index = -1
    for i in range(PLAYERS_NUM):
        if players[i]['money'] > 0:
            winners += 1
            winner_index = i
        if winners < 0:
            print('ERROR: Negative money found!')

    if winners > 1:
        print('ERROR: More than one winner found!')

    return winner_index

wins_arr = {}
for i in range(PLAYERS_NUM):
    wins_arr[f'Player {i}'] = {'wins': 0}

time_started = time.perf_counter()  # Start measuring time
for i in range(SIMULATED_GAMES):
    result = run_game()
    wins_arr[f'Player {result}']['wins'] += 1

time_ended = time.perf_counter()  # End measuring time

print(f"Simulation took {time_ended - time_started:.2f} seconds.")
print(wins_arr)

for i in range(PLAYERS_NUM):
    print(f"Player {i} win chance is {wins_arr[f'Player {i}']['wins'] / SIMULATED_GAMES:.2%}")

# Debugging prints

# for i in range(PLAYERS_NUM):
#     print(f"{players[i]['name']} has {players[i]['money']} money.")


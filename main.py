import random
import copy

class BattleSet:
    def __init__(self):
        self.name = "Any Battle Set"
        self.bonus = -1.0
        self.cards = []


class BattleCard:
    def __init__(self):
        self.name = "Any Card"
        self.battle_set = BattleSet()
        self.battle_lines = []
        self.stealable = False
        self.score = -1.0

    def __str__(self):
        my_str = "name: % s" % self.name
        return my_str


class Player:
    def __init__(self):
        self.name = "Default player"
        self.current_score = -1.0
        self.inventory = []
        self.strategy = None  # Indicates current strategy of the player

    def __str__(self):
        my_str = "name: % s" % self.name
        return my_str

    def update_score(self):
        """
        Calculate a player's score based on its current inventory
        :return:
        """


class BattleGame:
    def __init__(self):
        self.field = []  # Contains the cards in play on the field
        self.current_turn = None
        self.players = []  # Ordered list of players in the game
        # self.turn_order = []  # TODO implement if you want to have a specified turn order
        self.battle_stats = None  # TODO Object that contains information about the game

    # shimazu
    # battleset
    # kumamoto
    # [[0, 0]
    #     , [1]
    #     , [2]
    #     , [s5]
    #  ]
    #
    # chosokabe
    # battleset
    # muragame
    # [[0, 0]
    #     , [2]
    #  matsuyama
    #  [[0]
    #  , [s4]
    #  , [s4]
    #  ]

def create_card_objects():
    exit()

def create_battle_set_objects():
    exit()

def create_game():
    my_battle_game = BattleGame()

    # Construct all BattleSet objects
    my_battle_sets = {}
    shimazu_battle_set = BattleSet()
    shimazu_battle_set.name = "shimazu"
    shimazu_battle_set.bonus = 0.0
    my_battle_sets["shimazu"] = shimazu_battle_set

    chosokabe_battle_set = BattleSet()
    chosokabe_battle_set.name = "Chosokabe"
    chosokabe_battle_set.bonus = 1.0
    my_battle_sets["chosokabe"] = chosokabe_battle_set

    # Create all the card objects
    my_card1 = BattleCard()
    my_card1.name = "kumamoto"
    my_card1.score = 3.0
    my_card1.stealable = False
    my_card1.battle_set = my_battle_sets["shimazu"]
    my_card1.battle_lines.append([0, 0])
    my_card1.battle_lines.append([1])
    my_card1.battle_lines.append([2])
    my_card1.battle_lines.append(["s4"])
    my_battle_game.field.append(my_card1)
    my_battle_sets["shimazu"].cards.append(my_card1)

    my_card2 = BattleCard()
    my_card2.name = "muragame"
    my_card2.score = 1.0
    my_card2.stealable = True
    my_card2.battle_set = my_battle_sets["chosokabe"]
    my_card2.battle_lines.append([0, 0])
    my_card2.battle_lines.append([2])
    my_battle_game.field.append(my_card2)
    my_battle_sets["chosokabe"].cards.append(my_card2)

    my_card3 = BattleCard()
    my_card3.name = "matsuyama"
    my_card3.score = 2.0
    my_card3.stealable = True
    my_card3.battle_set = my_battle_sets["chosokabe"]
    my_card3.battle_lines.append([0])
    my_card3.battle_lines.append(["s4"])
    my_card3.battle_lines.append(["s4"])
    my_battle_game.field.append(my_card3)
    my_battle_sets["chosokabe"].cards.append(my_card3)

    print(my_battle_game.field)
    for i in my_battle_game.field:
        print(i)

    # Create player(s)
    player1 = Player()
    player1.name = "Player 1"
    player1.current_score = 0.0
    my_battle_game.players.append(player1)

    player2 = Player()
    player2.name = "Player 2"
    player2.current_score = 0.0
    my_battle_game.players.append(player2)

    return my_battle_game

def print_field(game):
    print("Current Field:")
    for i in game.field:
        print(i)


def get_available_battle_lines(game, player):
    # Are there any viable battle lines given the current roll

    available_battle_lines = []
    for card in game.field:
        for bl in card.battle_lines:
            available_battle_lines.append({"name": card.name,
                                           "card": card,
                                           "bl": bl,
                                           "score": card.score,
                                           "bs_bonus": card.battle_set.bonus,
                                           "orgin": "field"})
    for pl in game.players:
        if player == pl:
            continue  # Not yourself
        for card in pl.inventory:
            if card.stealable:
                for bl in card.battle_lines:
                    available_battle_lines.append({"name": card.name,
                                                   "card": card,
                                                   "bl": bl,
                                                   "score": card.score,
                                                   "bs_bonus": card.battle_set.bonus,
                                                   "orgin": pl})
                # Adding additional battle line because we are stealing from a player
                available_battle_lines.append({"name": card.name,
                                               "card": card,
                                               "bl": [0],
                                               "score": card.score,
                                               "bs_bonus": card.battle_set.bonus,
                                               "orgin": pl})
    print("Available Battle Lines:")
    for i in available_battle_lines:
        print(i)

    return available_battle_lines


def is_viable_bl_swords(players_roll, bl_object):
    # Is swordline
    bl_swords = int(bl_object[0][1:])
    player_swords = 0
    for i in players_roll:
        if i == 3:
            player_swords += 1
        if i == 4:
            player_swords += 2
        if i == 5:
            player_swords += 3

    return player_swords >= bl_swords


def is_viable_bl_hash(players_roll, bl_object):
    bl_hash = {}
    players_hash = {}
    for i in bl_object:
        if i not in bl_hash:
            bl_hash[i] = 0
        bl_hash[i] += 1
    for i in players_roll:
        if i not in players_hash:
            players_hash[i] = 0
        players_hash[i] += 1

    win_count = 0
    for i in bl_hash:
        if i in players_hash and i in bl_hash:
            if players_hash[i] >= bl_hash[i]:
                win_count += 1

    return win_count >= len(bl_hash)


def is_sword_bl(bl_object):
    return str(bl_object[0])[0] == "s"

def is_viable_bl(players_roll, bl_object):
    if is_sword_bl(bl_object):
        return is_viable_bl_swords(players_roll, bl_object)
    else:
        return is_viable_bl_hash(players_roll, bl_object)


def get_viable_battle_lines(players_roll, available_battle_lines):
    print(players_roll)
    print(available_battle_lines)

    viable_battle_lines = []

    for bl in available_battle_lines:
        bl_object = bl["bl"]
        if is_viable_bl(players_roll, bl_object):
            viable_battle_lines.append(bl)

    return viable_battle_lines

def select_battle_line(players_roll, viable_battles_lines, strategy=None):
    # Strategy adds more complexity to selecting a battle line
    return viable_battles_lines[0]


def update_players_dice(player_roll, selected_battle_line):
    print("player_roll: ", player_roll)
    print("selected_battle_line: ", selected_battle_line)
    if is_sword_bl(selected_battle_line):
        bl_swords = int(selected_battle_line[0][1:])
        player_roll.sort(reverse=True)
        i = 0
        while bl_swords > 0:
            if player_roll[i] == 3:
                bl_swords -= 1
            if player_roll[i] == 4:
                bl_swords -= 2
            if player_roll[i] == 5:
                bl_swords -= 3
            i += 1
        return len(player_roll) - i
    else:
        return len(player_roll)-len(selected_battle_line)


def finish_card(players_roll, selected_battle_line):
    players_dice = len(players_roll)

    # Remove selected battle line
    card_battle_lines = copy.deepcopy(selected_battle_line["card"].battle_lines)  # Do this so we don't damage our original card
    card_battle_lines.remove(selected_battle_line["bl"])
    if len(card_battle_lines) == 0:
        return True
    players_dice = update_players_dice(players_roll, selected_battle_line["bl"])

    while players_dice > 0:
        players_roll = battleline_roll(players_dice)
        card_battle_lines_bl = []
        for x in card_battle_lines:
            card_battle_lines_bl.append({"bl": x})
        viable_battles_lines = get_viable_battle_lines(players_roll, card_battle_lines_bl)
        if len(viable_battles_lines) == 0:
            players_dice -= 1
            continue

        selected_battle_line = select_battle_line(players_roll, viable_battles_lines)

        # Remove selected battle line
        card_battle_lines.remove(selected_battle_line["bl"])
        if len(card_battle_lines) == 0:
            return True
        players_dice = update_players_dice(players_roll, selected_battle_line["bl"])

    return False


# get a random dice roll given a number of dice
def battleline_roll(num_dice):
    roll = []
    for i in range(0, num_dice):
        roll.append(random.randint(0, 5))
    return roll;


def play_game(game):

    GAME_DICE = 7

    print_field(game)

    turns = 0

    while len(game.field) > 0:
        for player in game.players:
            turns += 1
            print("Its % s turn!" % player)
            players_dice = GAME_DICE

            # Roll the dice
            print("Its % s roll:" % player)
            players_roll = battleline_roll(players_dice)
            print(players_roll)

            # See which battle the player can choose from
            available_battle_lines = get_available_battle_lines(game, player)
            viable_battles_lines = get_viable_battle_lines(players_roll, available_battle_lines)
            selected_battle_line = select_battle_line(players_roll, viable_battles_lines)

            # End first dice roll (maybe functionalize later)

            if finish_card(players_roll, selected_battle_line):
                # Got card remove from field
                if selected_battle_line["orgin"] == "field":
                    game.field.remove(selected_battle_line['card'])
                else:
                    selected_battle_line['origin'].inventory.remove(selected_battle_line['card'])
                player.inventory.append(selected_battle_line['card'])
            else:
                continue

            print("selected_battle_line:", selected_battle_line)
            # TODO finish card run
            # If
            # TODO Need to be able to move a given card into an inventory (AXIOM OF CHOICE)

            # TODO Have to update if battle set made update cards to be not stealable
            print("Its % s inventory:" % player)
            for i in player.inventory:
                print(i)

            print_field(game)

            if len(game.field) <= 0:
                break

            # TODO Update player score
            player.update_score()
            print(player.current_score)
    
    # TODO Calculate scores at end
    print("Game over!")
    for p in game.players:
        print("Its % s inventory:" % p)
        for i in p.inventory:
            print(i)

    print(turns)


def run_age_of_war(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Welcome to Age of War')  # Press Ctrl+F8 to toggle the breakpoint.

    # Load all game objects, cards, players, fields, etc.


    # Create the game
    my_game = create_game()

    # Play the game
    play_game(my_game)

    # Figure out who wins

    # Close game


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Read command line parameters
    comamnd_line_params = {}

    run_age_of_war(comamnd_line_params)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

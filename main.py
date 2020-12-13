import random


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


def create_game():
    my_battle_game = BattleGame()

    # Construct all BattleSet objects
    my_battle_sets = {}
    shimatzu_battle_set = BattleSet()
    shimatzu_battle_set.name = "Shimatzu"
    shimatzu_battle_set.bonus = 0.0
    my_battle_sets["shimatzu"] = shimatzu_battle_set

    chosokabe_battle_set = BattleSet()
    chosokabe_battle_set.name = "Chosokabe"
    chosokabe_battle_set.bonus = 1.0
    my_battle_sets["chosokabe"] = chosokabe_battle_set

    # Create all the card objects
    my_card1 = BattleCard()
    my_card1.name = "kumamoto"
    my_card1.score = 3.0
    my_card1.stealable = False
    my_card1.battle_set = my_battle_sets["shimatzu"]
    my_card1.battle_lines.append([0, 0])
    my_card1.battle_lines.append([1])
    my_card1.battle_lines.append([2])
    my_card1.battle_lines.append(["s4"])
    my_battle_game.field.append(my_card1)
    my_battle_sets["shimatzu"].cards.append(my_card1)

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
                                           "bl": bl,
                                           "score": card.score,
                                           "bs_bonus": card.battle_set.bonus})
    for pl in game.players:
        if player == pl:
            continue  # Not yourself
        for card in pl.inventory:
            if card.stealable:
                for bl in card.battle_lines:
                    available_battle_lines.append({"name": card.name,
                                                   "bl": bl,
                                                   "score": card.score,
                                                   "bs_bonus": card.battle_set.bonus})
    print("Available Battle Lines:")
    for i in available_battle_lines:
        print(i)

    return available_battle_lines

def play_game(game):

    # get a random dice roll given a number of dice
    def battleline_roll(num_dice):
        roll = []
        for i in range(0, num_dice):
            roll.append(random.randint(0, 5))
        return roll;

    GAME_DICE = 7

    print_field(game)

    while len(game.field) > 0:
        for player in game.players:
            print("Its % s turn!" % player)
            players_dice = GAME_DICE

            # Roll the dice
            print("Its % s roll:" % player)
            players_roll = battleline_roll(players_dice)
            print(players_roll)

            # See which battle the player can choose from
            available_battle_lines = get_available_battle_lines(game, player)




            # TODO pick a viable battle line (this chooses a card for you)
            # TODO finish card run

            # TODO Need to be able to move a given card into an inventory (AXIOM OF CHOICE)
            player.inventory.append(game.field.pop())
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

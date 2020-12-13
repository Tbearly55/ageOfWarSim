
import main as main


def test_is_viable_bl_swords1():
    test_player_roll = [1,2,3]
    test_bl_object = ["s4"]

    assert main.is_viable_bl_swords(test_player_roll, test_bl_object) == False


def test_is_viable_bl_swords2():
    test_player_roll = [4,4]
    test_bl_object = ["s4"]

    assert main.is_viable_bl_swords(test_player_roll, test_bl_object) == True


def test_is_viable_bl_hash1():
    test_player_roll = [0,0]
    test_bl_object = [0,0,1]

    assert main.is_viable_bl_hash(test_player_roll, test_bl_object) == False


def test_is_viable_bl_hash2():
    test_player_roll = [0,0,1,2,3,4]
    test_bl_object = [0,0]

    assert main.is_viable_bl_hash(test_player_roll, test_bl_object) == True


def test_is_viable_bl_hash3():
    test_player_roll = [0,0,1,2,3,4]
    test_bl_object = [0,0, 1, 1]

    assert main.is_viable_bl_hash(test_player_roll, test_bl_object) == False

def test_update_players_dice1():
    test_player_roll = [4,4,4,4]
    test_bl_object = ["s4"]

    assert main.update_players_dice(test_player_roll, test_bl_object) == 2


def test_update_players_dice2():
    test_player_roll = [4,4,4,4,4]
    test_bl_object = ["s10"]

    assert main.update_players_dice(test_player_roll, test_bl_object) == 0


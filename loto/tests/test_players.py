def test_player_not_win(user_player):
    assert user_player.win() is False


def test_player_win(winner):
    assert winner.win() is True


def test_player_lose(winner):
    winner.action = True
    assert winner.lose(3) is True

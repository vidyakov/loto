from random import shuffle, sample
from tabulate import tabulate

from .players import ComputerPlayer, UserPlayer
from .exceptions import GameEnd


class Bag:
    def __init__(self):
        self._barrels = [i for i in range(1, 91)]
        shuffle(self._barrels)

    def pop(self):
        return self._barrels.pop()

    def __len__(self):
        return len(self._barrels)


class Card:
    def __init__(self):
        self._values = sample([i for i in range(1, 91)], 15) + [0] * 6
        shuffle(self._values)

    def cross(self, value):
        value_index = self._values.index(value)
        self._values[value_index] = -1

    def is_all_crossed(self):
        for element in self._values:
            if element not in (-1, 0):
                return False
        return True

    def __contains__(self, item):
        return item in self._values

    def __str__(self):
        card = []
        for element in self._values:
            if element == 0:
                card.append(' ')
            elif element == -1:
                card.append('-')
            else:
                card.append(element)
        return tabulate([card[:7], card[7:14], card[14:]], tablefmt="grid")


class Game:
    def __init__(self, types):
        self._bag = Bag()
        self._user_players = []
        self._computer_players = []
        self._barrel = None

        for number, player_type in enumerate(types, 1):
            if player_type == 'u':
                self._user_players.append(
                    UserPlayer(input(f'Enter name of player #{number}: '), Card())
                )
            else:
                self._computer_players.append(ComputerPlayer(number, Card()))

    def _show_users_cards(self):
        for player in self._user_players + self._computer_players:
            print(player)

    def _make_users_step(self):
        for player in self._user_players:
            player.action = input(f'{player.name}: ')
            if player.lose(self._barrel):
                print(f'{player.name} lose :(')
                self._user_players.remove(player)
            else:
                player.step(self._barrel)
                if player.win():
                    raise GameEnd(f'{player.name} win!')

    def _make_computers_step(self):
        for computer in self._computer_players:
            computer.step(self._barrel)
            if computer.win():
                raise GameEnd(f'{computer.name} win!')

    def _step(self):
        self._show_users_cards()
        self._barrel = self._bag.pop()
        print(f'\nBarrel: {self._barrel}\nLeft: {len(self._bag)}\n')
        self._make_users_step()
        self._make_computers_step()

    def run(self):
        try:
            while True:
                if len(self._user_players + self._computer_players) > 1:
                    self._step()
                else:
                    raise GameEnd('Left one person')
        except (KeyboardInterrupt, EOFError):
            pass
        except GameEnd as end_error:
            print(end_error.text)
        finally:
            print('bye bye')

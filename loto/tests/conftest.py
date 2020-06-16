from random import randint

from pytest import fixture

from classes.game import Bag, Card
from classes.players import UserPlayer


@fixture(scope='module')
def bag():
    return Bag()


@fixture(scope='module')
def simple_card():
    return Card()


@fixture(scope='module')
def crossed_card():
    new_card = Card()
    new_card._values = [randint(-1, 0) for _ in range(21)]
    return new_card


@fixture(scope='module')
def user_player(simple_card):
    return UserPlayer('nastya', simple_card)


@fixture(scope='module')
def winner(crossed_card):
    return UserPlayer('sasha', crossed_card)

def test_bag_magic_len(bag):
    assert len(bag) == len(bag._barrels)


def test_bag_pop(bag):
    assert bag._barrels[-1] == bag.pop()


def test_card_valid_quantity_of_elements(simple_card):
    assert len([el for el in simple_card._values if el > 0]) == 15


def test_card_is_not_crossed(simple_card):
    assert simple_card.is_all_crossed() is False


def test_card_is_crossed(crossed_card):
    assert crossed_card.is_all_crossed() is True

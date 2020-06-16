class PlayerMixin:
    def __init__(self, name, card):
        self.name = name
        self.card = card

    def win(self):
        return self.card.is_all_crossed()

    def __str__(self):
        return f'\t{self.name}\n{self.card}'


class UserPlayer(PlayerMixin):
    def __init__(self, *args):
        super().__init__(*args)
        self.action = None

    def lose(self, barrel):
        if self.action:
            return barrel not in self.card
        return barrel in self.card

    def step(self, barrel):
        if self.action:
            self.card.cross(barrel)


class ComputerPlayer(PlayerMixin):
    def __init__(self, number, *args):
        super().__init__(f'Player #{number}', *args)

    def step(self, barrel):
        if barrel in self.card:
            self.card.cross(barrel)

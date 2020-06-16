class GameEnd(Exception):
    def __init__(self, text=''):
        super().__init__()
        self.text = text

import argparse

from classes import Game


parser = argparse.ArgumentParser(prog='Loto')
parser.add_argument(
    'first_user', nargs=1, choices=('c', 'u'), metavar='',
    action='store'
)
parser.add_argument(
    'users', nargs='+', choices=('c', 'u'),
    action='store', help='Type (computer or user) and quantity (quantity of letters)'
)


if __name__ == '__main__':
    args = parser.parse_args()
    Game(args.first_user + args.users).run()

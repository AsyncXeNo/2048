from utils.logger import Logger
from game.square import Square


class Tile(object):
    def __init__(self, square:Square, value:int):
        self.logger = Logger("game/tile")

        self.square = square
        self.value = value

    def get_square(self):
        return self.square

    def set_square(self, square:Square):
        self.square.clear()
        self.square = square
        self.square.set_tile(self)

    def double(self):
        self.value *= 2
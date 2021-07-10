import random

from utils.logger import Logger
from game.tile import Tile


class Square(object):
    def __init__(self, x:int, y:int):
        self.logger = Logger("game/square")

        self.x = x
        self.y = y
        self.tile = None


    # info

    def get_pos(self):
        return (self.x, self.y)

    def clear(self):
        self.tile = None

    def new_tile(self):
        self.tile = Tile(random.choice([2, 4]))

    def set_tile(self, tile:Tile):
        self.tile = tile
        self.tile.set_square(self)

    def get_tile(self):
        return self.tile

    def is_empty(self):
        return self.tile == None
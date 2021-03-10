from ursina import *
from lvls.lvl0 import Level0


class Carbanak:
    def __init__(self):
        self.app = Ursina()

        self.getLevels()
        self.level = self.levels['lvl0']()

        self.app.run()

    def getLevels(self):
        self.levels = {
            'lvl0': Level0
        }

    def input(self, key):
        if key == 'a':
            self.level.unLoad()
            if self.level.next:
                self.level = self.levels[self.level.next]


if __name__ == '__main__':
    app = Carbanak()

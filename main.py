from ursina import *
from lvls.lvl0.lvl0 import Level0


class Carbanak(Ursina):
    def __init__(self):
        super().__init__()

        self.getLevels()
        self.level = self.levels['lvl0'](lang='fr')

        self.run()

    def getLevels(self):
        self.levels = {
            'lvl0': Level0
        }

    def input(self, key):
        if key == 'a':
            self.level.unLoad()
            try:
                self.level = self.levels[self.level.next](lang='en')
            except Exception:
                print(f'No level after {self.level.name}')

    def update(self):
        print('ok')
        if self.level:
            self.level.update()


if __name__ == '__main__':
    app = Carbanak()

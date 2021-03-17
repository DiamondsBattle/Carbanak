from ursina import *
from lvls.lvl0.lvl0 import Level0


class Carbanak(Ursina):
    def __init__(self):
        super().__init__()

        self.levels = self.getLevels()
        self.level = self.levels['lvl0'](lang='en')

        self.run()

    def getLevels(self):
        return {
            'lvl0': Level0
        }

    @super.input()
    def input(self, key):
        if key == 'x':
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

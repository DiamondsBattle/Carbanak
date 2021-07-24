from ursina import *
from lvls.lvl0.lvl0 import Level0


class Carbanak(Entity):
    def __init__(self):
        super().__init__(
            eternal=True,
        )

        self.configs = {
            'lang': 'en'
        }

        self.levels = self.getLevels()
        self.level = self.levels['lvl0'](lang=self.configs['lang'])

    def getLevels(self):
        return {
            'lvl0': Level0
        }

    def input(self, key):
        if key == 'x':
            self.level.unLoad()
            try:
                self.level = self.levels[self.level.next](lang=self.configs['lang'])
            except Exception:
                print(f'No level after {self.level.name}')

    def update(self):
        if self.level:
            self.level.update()


if __name__ == '__main__':
    env = Ursina()
    app = Carbanak()
    env.run()

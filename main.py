from ursina import *
from prefabs.screen import Screen


class Carbanak:
    def __init__(self):
        self.app = Ursina()

        self.postInit()

    def postInit(self):
        self.app.run()


if __name__ == '__main__':
    app = Carbanak()

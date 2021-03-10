from prefabs.level import Level
from prefabs.screen import Screen
from ursina import *


class Level0(Level):
    def __init__(self):
        super().__init__(
            name='level0',
            description='prologue',
            next='level1'
        )

        self.entities = {
            'screen': Screen()
        }

        for e in self.entities:
            try:
                self.entities[e].enabled = False
            except Exception:
                print(f'Error : {e} is not a valid Entity')

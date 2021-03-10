from prefabs.level import Level

from prefabs.screen import Screen
from prefabs.halo import Halo

from ursina import invoke
from json import loads


class Level0(Level):
    def __init__(self, **kwargs):
        super().__init__(
            name='level0',
            description='prologue',
            next='level1',
            **kwargs,
        )
        with open('lvls/lvl0/text.json', 'r') as f:
            self.text = loads(f.read())

        self.entities = {
            'screen': Screen(),
            'halo': Halo(),
        }

        for i in self.entities:
            self.entities[i].enabled = False

        invoke(setattr, self.entities['screen'], 'enabled', True, delay=3)

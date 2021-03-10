from prefabs.level import Level

from prefabs.screen import Screen
from prefabs.halo import Halo
from prefabs.script import Script

from ursina import invoke, window, Vec2
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
            data = loads(f.read())
        self.script = data[self.lang]

        self.entities = {
            'screen': Screen(),
            'halo': Halo(),
            'script': Script(
                script=self.script,
                position=Vec2(0, -.5),
                origin=(0, -.5)
            )
        }

        for i in self.entities:
            self.entities[i].enabled = False

        self.entities['script'].enabled = True

        invoke(setattr, self.entities['screen'], 'enabled', True, delay=3)

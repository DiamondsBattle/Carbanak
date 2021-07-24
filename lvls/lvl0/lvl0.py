from prefabs.level import Level

from prefabs.screen import Screen
from prefabs.halo import Halo
from prefabs.script import Script
from prefabs.application import *

from ursina import invoke, window, Vec2, Func
from json import loads


class Level0(Level):
    def __init__(self, **kwargs):
        super().__init__(
            name='level0',
            description='prologue',
            next='level1',
            **kwargs,
        )
        with open('lvls/lvl0/text.json', 'r', encoding='utf-8') as f:
            data = loads(f.read())
        self.script = data[self.lang]

        self.entities = {
            'screen': Screen(),
            'halo': Halo(),
            'script': Script(
                script=self.script,
                position=window.bottom,
                origin=(0, -.5)
            ),
            'bulb': Application(icon='bulb',
                                name='Bulb',
                                data='',
                                description='')
        }

        for i in self.entities:
            self.entities[i].enabled = False

        self.entities['script'].enabled = True

        self.appear(self.entities['screen'], 10)
        self.appear(self.entities['bulb'], 35)

        # self.entities['screen'].color = color.black
        # invoke(setattr, self.entities['screen'], 'enabled', True, delay=10)
        # invoke(self.entities['screen'].animate, 'color', color.white, delay=10, duration=1.5)
        #
        # invoke(self.entities['screen'].animate, 'color', color.white, delay=10, duration=1.5)
        # invoke(setattr, self.entities['bulb'], 'enabled', True, delay=35)
        # invoke(self.entities['bulb'].animate, 'color', color.white, delay=10, duration=1.5)

    def appear(self, e: Entity, d: int):
        if isinstance(e, Application):
            old_color = [e.ent_icon.color, e.ent_text.color]
            e.color = color.black
            invoke(setattr, e.ent_icon, 'enabled', True, delay=d)
            invoke(e.ent_icon.animate, 'color', old_color[0], delay=d, duration=1.5)

            invoke(setattr, e.ent_text, 'enabled', True, delay=d)
            invoke(e.ent_text.animate, 'color', old_color[1], delay=d, duration=1.5)
        else:
            old_color = e.color
            e.color = color.black
            invoke(setattr, e, 'enabled', True, delay=d)
            invoke(e.animate, 'color', old_color, delay=d, duration=1.5)

    def update(self):
        print(self.entities['screen'].color)

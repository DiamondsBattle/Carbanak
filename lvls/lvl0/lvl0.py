from prefabs.level import Level

from prefabs.screen import Screen
from prefabs.halo import Halo
from prefabs.script import Script
from prefabs.application import *
from prefabs.handbook import HandBook

from ursina import invoke, window
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
        self.script = data[self.lang]['dial']

        self.entities = {
            'screen': Screen(),
            'halo': Halo(),
            'script': Script(
                script=self.script,
                position=window.bottom,
                origin=(0, -.5)
            ),
            'bulb': Bulb(),
            'citadel': Citadel(),
            'thor': Thor(),
            'firecat': Firecat(),
            'wow_text': WowText(),
            'ice_wall': IceWall(),
            'handbook': HandBook(
                title='HandBook',
                cont='Your handbook is the only place where you\'ll'
                     ' find every useful data on your progression. '
                     'It also contains your achievements and keeps '
                     'track of your save files, enabling you to '
                     'create and delete them.'
            ),
        }

        for i in self.entities:
            self.entities[i].enabled = False

        self.entities['script'].enabled = True

        self.appear(self.entities['handbook'], 0)
        self.appear(self.entities['screen'], 12.5) # 12.5
        self.appear(self.entities['bulb'], 30)
        self.appear(self.entities['citadel'], 35)
        self.appear(self.entities['thor'], 40)
        self.appear(self.entities['firecat'], 45)
        self.appear(self.entities['wow_text'], 50)
        self.appear(self.entities['ice_wall'], 55)

    def appear(self, e: Entity, d):
        if isinstance(e, Application):
            e.ent_icon.color[3] = 0
            e.ent_text.color[3] = 0
            e.ent_icon.fade_in(duration=1, delay=d+.2)
            e.ent_text.fade_in(duration=1, delay=d)
            invoke(setattr, e, 'enabled', True, delay=d)

            halo = Halo(
                position=e.ent_icon.position,
                enabled=False,
            )
            invoke(setattr, halo, 'enabled', True, delay=d)
            halo.fade_in(duration=1, delay=d+.7)
            invoke(destroy, halo, delay=d+5.5)
        else:
            invoke(setattr, e, 'enabled', True, delay=d)
            e.color[3] = 0
            e.fade_in(duration=1.5, delay=d)

    def update(self):
        pass

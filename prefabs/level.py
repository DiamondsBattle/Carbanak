from ursina import *
from prefabs.application import Application


class Level:
    def __init__(self, name, description, lang, next=None):
        self.name = name
        self.description = description
        self.next = next
        self.lang = lang

        self.entities = {}

    def unLoad(self):
        for e in self.entities:
            if isinstance(e, Entity):
                destroy(self.entities[e])
            elif isinstance(e, Application):
                e.destroy()

    def update(self):
        pass

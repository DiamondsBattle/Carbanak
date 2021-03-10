from ursina import *


class Level:
    def __init__(self, name, description, lang, next=None):
        self.name = name
        self.description = description
        self.next = next
        self.lang = lang

        self.entities = {}

    def unLoad(self):
        for e in self.entities:
            destroy(self.entities[e])

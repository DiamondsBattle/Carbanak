from ursina import *


class Level:
    def __init__(self, name, description, next=None):
        self.name = name
        self.description = description
        self.next = next

        self.entities = {}

    def unLoad(self):
        for i, e in self.entities:
            destroy(e)

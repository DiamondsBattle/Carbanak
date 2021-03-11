from ursina import *


class Application:
    def __init__(self, name, description, icon, data):
        self.name = name
        self.description = description
        self.icon = icon
        self.data = data

        self.ent_icon = Button(
            model='quad',
            texture=self.icon,
            scale=Vec2(.15, .1),
            always_on_top=True,
            color=color.white
        )
        self.ent_text = Text(
            # parent=self.ent_icon,
            text=self.name,
            origin=(0, 0),
            position=self.ent_icon.position,
            y=(self.ent_icon.y - .8),
            always_on_top=True,
            color=color.black,
        )

    @property
    def enabled(self):
        return self.enabled

    @enabled.setter
    def enabled(self, value):
        self.ent_icon.enabled = value


class Bulb(Application):
    def __init__(self):
        super().__init__(
            name='Bulb',
            description='Bulb is used to reverse engineer a malware to optain information on it',
            icon='bulb',
            data='None'
        )

from ursina import *


class Application:
    def __init__(self, name, description, icon, data):
        self.name = name
        self.description = description
        self.icon = icon
        self.data = data

        standard_positions = {
            'Bulb': Vec3(-.65, .28, 0),
            'Citadel': Vec3(-.65, .03, 0),
            'Thor': Vec3(-.65, -.24, 0),
            'Firecat': Vec3(-.38, .28, 0),
            'Wow Text 3': Vec3(-.38, .03, 0),
            'IceWall': Vec3(-.38, -.24, 0)
        }

        self.ent_icon = Icon(
            texture=self.icon,
            position=standard_positions[self.name]
        )
        self.ent_text = Text(
            text=self.name,
            origin=(0, 0),
            position=self.ent_icon.position,
            y=(self.ent_icon.y - .07),
            always_on_top=True,
            color=color.black,
        )

    @property
    def enabled(self):
        return self.ent_icon.enabled

    @enabled.setter
    def enabled(self, value):
        self.ent_icon.enabled = value
        self.ent_text.enabled = value

    @property
    def color(self):
        return self.ent_icon.color

    @color.setter
    def color(self, value):
        self.ent_icon.color = value
        self.ent_text.color = value

    def animate(self, **kwargs):
        self.ent_icon.animate(**kwargs)
        self.ent_text.animate(**kwargs)

    def destroy(self):
        destroy(self.ent_icon)
        destroy(self.ent_text)
        del self


class Icon(Button):
    def __init__(self, **kwargs):
        super().__init__(
            scale=Vec2(.15, .1),
            model='quad',
            always_on_top=True,
            color=color.white,
            on_click=self.click,
            **kwargs
        )

    def update(self):
        if self.hovered:
            self.hover()
        elif self.color[3] != .66:
            self.color = Vec4(1, 1, 1, self.color[3])
        else:
            self.color = color.white

    def hover(self):
        self.color = color.white66

    def click(self):
        self.color = color.blue


class Bulb(Application):
    def __init__(self):
        super().__init__(
            name='Bulb',
            description='Software allowing reverse engineering of a malware to gather upon data on it\'s origin, makers, path and procedure',
            icon='bulb',
            data='None',
        )

class Citadel(Application):
    def __init__(self):
        super().__init__(
            name='Citadel',
            description='Software allowing a complete computer scan for Malwares',
            icon='citadel',
            data='None',
        )

class Thor(Application):
    def __init__(self):
        super().__init__(
            name='Thor',
            description='Software allowing to go on the DarkNet',
            icon='thor',
            data='None',
        )

class Firecat(Application):
    def __init__(self):
        super().__init__(
            name='Firecat',
            description='Software allowing to go on Internet',
            icon='firecat2',
            data='None',
        )

class WowText(Application):
    def __init__(self):
        super().__init__(
            name='Wow Text 3',
            description='Software allowing to write code',
            icon='wow_text',
            data='None',
        )

class IceWall(Application):
    def __init__(self):
        super().__init__(
            name='IceWall',
            description='Software allowing you to secure a network',
            icon='icewall3',
            data='None',
        )

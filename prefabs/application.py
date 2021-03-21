from ursina import *


class Application:
    def __init__(self, name, description, icon, data):
        self.name = name
        self.description = description
        self.icon = icon
        self.data = data

        self.ent_icon = Icon(
            texture=self.icon,
        )
        self.ent_text = Text(
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
        self.ent_text.enabled = value
        print(self.ent_icon.enabled)

    def destroy(self):
        destroy(self.ent_icon)
        destroy(self.ent_text)
        del self


class Icon(Button):
    def __init__(self, **kwargs):
        super().__init__(
            scale=Vec2(.15, .1),
            always_on_top=True,
            model='quad',
            color=color.white,
            # on_click=self.click,
            **kwargs
        )
        self._on_click = self.click

    def update(self):
        pass
        # if self.hovered:
        #     self.on_hover()
        # else:
        #     self.color = color.white

    def hover(self):
        self.color = color.white33

    def click(self):
        print('ok')
        self.color = color.blue


class Bulb(Application):
    def __init__(self):
        super().__init__(
            name='Bulb',
            description='Bulb is used to reverse engineer a malware to obtain information on it',
            icon='bulb',
            data='None'
        )

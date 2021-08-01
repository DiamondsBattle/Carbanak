from ursina import Entity, Vec3, Vec2, Text, camera, color
import textwrap


class HandBook(Entity):
    def __init__(self, title, cont):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture='notepad_still',
            scale=Vec3(0.4, 0.6, 0),
            position=Vec3(.65, -.28, 0),
        )
        self.title = ''
        self.content = ''
        self.title_ent = Text(
            title,
            scale=Vec3(2.5, 2.5, 0),
            color=color.black,
            always_on_top=True,
            origin=Vec2(0, 0)
        )
        self.cont_ent = Text(
            cont,
            color=color.black,
            origin=Vec2(-.05, 0),
            always_on_top=True
        )
        wrapper = textwrap.TextWrapper(25)
        t = wrapper.wrap(self.cont_ent.text)
        t = ''.join([i + '\n' for i in t])
        self.cont_ent.text = t


    def update(self):
        self.title_ent.position = self.position + Vec3(.02, .205, 0)
        self.cont_ent.position = self.position + Vec3(0, .03, 0)

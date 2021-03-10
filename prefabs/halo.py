from ursina import Entity, camera, Vec3


class Halo(Entity):
    def __init__(self, delay=5, **kwargs):
        super().__init__(
            model='quad',
            texture='halo',
            scale=Vec3(.15, .1, 0),
            always_on_top=True,
            parent=camera.ui,
            **kwargs)
        self.delay = delay

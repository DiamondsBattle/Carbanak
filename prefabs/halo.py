from ursina import Entity, camera, Vec3


class Halo(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            texture='halo',
            model='quad',
            scale=.16,
            always_on_top=True,
            parent=camera.ui,
            **kwargs)
        self.y -= .015

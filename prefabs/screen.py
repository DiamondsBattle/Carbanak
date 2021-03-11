from ursina import *


class Screen(Entity):
    def __init__(self, **kwargs):
        self.scale_xy = (
            (window.fullscreen_size[0] / window.fullscreen_size[1]),
            0.95,
        )
        super().__init__(
            texture='screen_main',
            model='quad',
            scale=self.scale_xy,
            parent=camera.ui,
            y=.025,
            **kwargs
        )

from ursina import *


class Script(Text):
    def __init__(self, script, **kwargs):
        super().__init__(**kwargs)
        self.script = script
        self.current = 0
        self.n = 0
        self.speed = .05

        self.changeScript()

    def changeScript(self):
        self.n = 0
        for i in self.script:
            self.n += 1
            if self.n == self.current + 1:
                self.text = i
                invoke(self.changeScript, delay=((len(self.text) * .05) + 3))
                self.appear(speed=self.speed)

        if self.n < self.current + 1:
            destroy(self)
        self.current += 1


if __name__ == '__main__':
    app = Ursina()

    script = ['This is A',
              'This is B',
              'This is C']
    s = Script(script=script)

    app.run()
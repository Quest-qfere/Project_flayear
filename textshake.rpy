init python:
    import random

    class ShakeText(renpy.Displayable):
        def __init__(self, child):
            super(ShakeText, self).__init__()
            self.child = child
            self.x = 0
            self.y = 0

        def render(self, width, height, st, at):
            render = renpy.render(self.child, width, height, st, at)
            w, h = render.get_size()

            if st < 2.0:
                self.x = random.randint(-2, 2)
                self.y = random.randint(-2, 2)
                renpy.redraw(self, 0)
                
            surf = renpy.Render(w, h)
            surf.blit(render, (self.x, self.y))
            return surf

    def shaky(tag, argument, contents):
        return [
            (renpy.TEXT_DISPLAYABLE, ShakeText(renpy.text.text.Text(''.join(text for _, text in contents))))
        ]

    config.custom_text_tags["shaky"] = shaky
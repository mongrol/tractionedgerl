import sys
try:
    from sdl2 import *
    import sdl2.ext as sdl2ext
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

    #create renderer System
class Renderer(sdl2ext.TextureSpriteRenderer):
    def __init__(self, context):
        super(Renderer, self).__init__(context)

    def render(self, components):
        #fills background first
        super(Renderer, self).render(components)

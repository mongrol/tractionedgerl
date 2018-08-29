#import pysdl2
import sys
try:
    from sdl2 import *
    import sdl2.ext as sdl2ext
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

import components
import systems

class Creature(sdl2ext.Entity):
    def __init__(self, world, sprite, x=0, y=0):
        self.position = components.Position(x,y)
        self.sprite = sprite
        self.sprite.position = x,y

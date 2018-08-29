#!/usr/bin/python
#Copyright 2013 Steven Hamilton
#Licensed under GPLv3

#import pysdl2
import sys
try:
    from sdl2 import *
    import sdl2.ext as sdl2ext
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

import systems
import entities

WHITE = sdl2ext.Color(255, 255, 255)

def run():
    # init sdl and get window up
    sdl2ext.init()
    window = sdl2ext.Window("Traction Edge RL", size=(800, 600))
    window.show()

    #create hardware accelerated context for drawing on
    context = sdl2ext.RenderContext(window, index=-1, flags=SDL_RENDERER_ACCELERATED)
    #create our custom renderer with the context
    renderer = systems.Renderer(context)

    # init world
    world = sdl2ext.World()
    world.add_system(renderer)

    # create our sprites
    factory = sdl2ext.SpriteFactory(sprite_type=sdl2ext.TEXTURE, renderer=context)
    sp_player = factory.from_color(WHITE, size=(32,32))

    #create player
    player = entities.Creature(world, sp_player, 100, 400)


    #main loop
    running = True
    while running:
        events = sdl2ext.get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
                break
        SDL_Delay(10)
        world.process()
    return 

#Enter main run routine
if __name__ == "__main__":
    sys.exit(run())



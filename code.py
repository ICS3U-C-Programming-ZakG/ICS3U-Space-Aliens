#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 31, 2023
# This program is the Space Aliens program on the PyBadge.

import stage
import ugame

def game_scene():

    # this is the main game game_scene

    # import background and assign to a variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # grid for image background
    background = stage.Grid(image_bank_background, 10, 8)

    # display images and set refresh rate to 60 hertz
    game = stage.Stage(ugame.display, 60)

    # put image of background into a list assigned to game
    game.layers = [background]

    # display background
    game.render_block()

    # game loop
    while True:

        # placeholder
        pass

if __name__ == "__main__":
    game_scene()

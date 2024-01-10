#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 31, 2023
# This program is the Space Aliens program on the PyBadge.

import stage
import ugame

import constants

def game_scene():

    # this is the main game game_scene

    # import background and assign to a variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # import image for sprite and assign
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # grid for image background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # create a single sprite,  get fifth image, and place in middle of the screen
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - constants.SPRITE_SIZE)

    # display images and set refresh rate to 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)

    # put image of background and ship into a list assigned to game
    game.layers = [ship] + [background]

    # display background
    game.render_block()

    # game loop
    while True:

        # get user button input
        keys = ugame.buttons.get_pressed()

        # check what button is being pressed then do action corresponding to that input
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        
        # check if right button is pressed
        if keys & ugame.K_RIGHT:

            # check if ship is within boundaries
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:

                # move ship 1 pixel right
                ship.move(ship.x + 1, ship.y)
            
            else:
                # prevent ship from passing boundary, the screen
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        # check if left button is pressed
        if keys & ugame.K_LEFT:

            # check if ship is within boundaries
            if ship.x >= 0:

                # move ship 1 pixel left
                ship.move(ship.x - 1, ship.y)
            
            # else stay at x = 0 to not pass boundary
            else:
                ship.move(0, ship.y)

        # check if the up button is being pressed
        if keys & ugame.K_UP:

            # check if ship is in boundaries
            if ship.y >= 0:

                # move ship up 1 pixel
                ship.move(ship.x, ship.y - 1)
            
            # prevent ship from getting out of the boundaries
            else:
                ship.move(ship.x, 0)
        
        # check if down button is being pressed
        if keys & ugame.K_DOWN:

            # check if ship is in boundaries
            if ship.y <= constants.SCREEN_Y - constants.SPRITE_SIZE:

                # move ship 1 pixel down
                ship.move(ship.x, ship.y + 1)
            
            # prevent ship from getting out of bounds
            else:
                ship.move(ship.x, constants.SCREEN_Y - constants.SPRITE_SIZE)

        # update game logic

        # redraw sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()

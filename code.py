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

    # import image for sprite and assign
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # grid for image background
    background = stage.Grid(image_bank_background, 10, 8)

    # create a single sprite,  get fifth image, and place in middle fo the screen
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # display images and set refresh rate to 60 hertz
    game = stage.Stage(ugame.display, 60)

    # put image of background and ship into a list assigned to game
    game.layers = [ship] + [background]

    # display background
    game.render_block()

    # game loop
    while True:

        # get user input
        keys = ugame.buttons.get_pressed()

        # check what button is being pressed then do action corresponding to that input
        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        
        # check for movement if so move one pixel to corresponding button direction
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)

        # update game logic

        # redraw sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()

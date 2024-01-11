#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 31, 2023
# This program is the Space Aliens program on the PyBadge.

import stage
import ugame
import time
import random

import constants

# this is the splash scene for the menu
def splash_scene():

    # create coin sound
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio

    # stop all audio
    sound.stop()

    # make sure mute is false
    sound.mute(False)

    # play coin sound
    sound.play(coin_sound)

    # import background and assign to a variable
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # grid for image background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

     # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white
    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white
    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white
    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # display images and set refresh rate to 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)

    # put image of background into a list assigned to game
    game.layers =  [background]

    # display background
    game.render_block()

    # game loop
    while True:

        # wait 2 seconds
        time.sleep(2.0)

        # call menu scene function
        menu_scene()

# this is the menu scene function
def menu_scene():

    # import background and assign to a variable
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # create text list
    text = []

    # create first text and customize
    text1 = stage.Text(width = 29, height = 12, font = None, palette = constants.RED_PALETTE, buffer = None)

    # move text
    text1.move(38, 10)

    # assign a text to variable
    text1.text("Space Aliens")

    # add text to text list
    text.append(text1)

    # create first text and customize
    text2 = stage.Text(width = 29, height = 12, font = None, palette = constants.RED_PALETTE, buffer = None)

    # move text
    text2.move(40, 110)

    # assign a text to variable
    text2.text("PRESS START")

    # add text to text list
    text.append(text2)

    # grid for image background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # display images and set refresh rate to 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)

    # put image of background and text into a list assigned to game
    game.layers = text + [background]

    # display background
    game.render_block()

    # game loop
    while True:

        # get user button input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START:
            game_scene()

        game.tick()

# this is the main game game_scene
def game_scene():

    # import background and assign to a variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # import image for sprite and assign
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # button state information
    a_button = constants.BUTTON_STATE["button_up"]
    b_button = constants.BUTTON_STATE["button_up"]
    start_button = constants.BUTTON_STATE["button_up"]
    select_button = constants.BUTTON_STATE["button_up"]

    # getting sound from library and assigning to variable
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio

    # stop all sound
    sound.stop()

    # make sure audio isn't muted
    sound.mute(False)

    # grid for image background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # for loop for x location
    for x_location in range(constants.SCREEN_GRID_X):

        # for loop for y location
        for y_location in range(constants.SCREEN_GRID_Y):

            # pick random tile 1-3
            tile_picked = random.randint(1,3)

            # place random tile in the location of x and y
            background.tile(x_location, y_location, tile_picked)

    # create a single sprite,  get fifth image, and place in middle of the screen
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - constants.SPRITE_SIZE)

    # create alien and assign location and image to it
    alien = stage.Sprite(image_bank_sprites, 9, int(constants.SCREEN_X/2 - constants.SPRITE_SIZE/2), 16)

    # display images and set refresh rate to 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)

    # put image of background and ship into a list assigned to game
    game.layers = [ship] + [alien] + [background]

    # display background
    game.render_block()

    # game loop
    while True:

        # get user button input
        keys = ugame.buttons.get_pressed()

        # check if B button is being pressed
        if keys & ugame.K_X:
            pass

        # check if pressed to fire
        if keys & ugame.K_O != 0:
            
            # check if sate is up
            if a_button == constants.BUTTON_STATE["button_up"]:

                # change to just pressed
                a_button = constants.BUTTON_STATE["button_just_pressed"]

            # else if check if it was just pressed
            elif a_button == constants.BUTTON_STATE["button_just_pressed"]:

                # change state to still pressed
                a_button = constants.BUTTON_STATE["button_still_pressed"]
        else:

            # check if state is still pressed
            if a_button == constants.BUTTON_STATE["button_still_pressed"]:
                
                # change state to button released
                a_button = constants.BUTTON_STATE["button_released"]
            else:

                # else change state to button back up again
                a_button = constants.BUTTON_STATE["button_up"]

            
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        
        # check if right button is pressed
        if keys & ugame.K_RIGHT:

            # check if ship is within boundaries
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:

                # move ship 1 pixel right
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            
            else:
                # prevent ship from passing boundary, the screen
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        # check if left button is pressed
        if keys & ugame.K_LEFT:

            # check if ship is within boundaries
            if ship.x >= 0:

                # move ship 1 pixel left
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            
            # else stay at x = 0 to not pass boundary
            else:
                ship.move(0, ship.y)

        # check if the up button is being pressed
        if keys & ugame.K_UP:

            # check if ship is in boundaries
            if ship.y >= 0:

                # move ship up 1 pixel
                ship.move(ship.x, ship.y - constants.SPRITE_MOVEMENT_SPEED)
            
            # prevent ship from getting out of the boundaries
            else:
                ship.move(ship.x, 0)
        
        # check if down button is being pressed
        if keys & ugame.K_DOWN:

            # check if ship is in boundaries
            if ship.y <= constants.SCREEN_Y - constants.SPRITE_SIZE:

                # move ship 1 pixel down
                ship.move(ship.x, ship.y + constants.SPRITE_MOVEMENT_SPEED)
            
            # prevent ship from getting out of bounds
            else:
                ship.move(ship.x, constants.SCREEN_Y - constants.SPRITE_SIZE)

        # update game logic
        

        # play sound if A button was just pressed
        if a_button == constants.BUTTON_STATE["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw sprites
        game.render_sprites([ship] + [alien])
        game.tick()

if __name__ == "__main__":
    splash_scene()

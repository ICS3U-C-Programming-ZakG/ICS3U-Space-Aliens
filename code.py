#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 31, 2023
# This program is the Space Aliens program on the PyBadge.

import stage
import ugame

import constants

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
    game_scene()

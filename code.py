#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 31, 2023
# This program is the Space Aliens program on the PyBadge.

import stage
import ugame
import time
import random
import supervisor

import constants

# this is the splash scene for the menu
def splash_scene():

    # create chime sound
    chime_sound = open("chime.wav", 'rb')
    sound = ugame.audio

    # stop all audio
    sound.stop()

    # make sure mute is false
    sound.mute(False)

    # play chime sound
    sound.play(chime_sound)

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
    text1 = stage.Text(width = 60, height = 40, font = None, palette = constants.RED_PALETTE, buffer = None)

    # move text
    text1.move(38, 10)

    # assign a text to variable
    text1.text("Space Aliens")

    # add text to text list
    text.append(text1)

    # create first text and customize
    text2 = stage.Text(width = 40, height = 20, font = None, palette = constants.RED_PALETTE, buffer = None)

    # move text
    text2.move(40, 110)

    # assign a text to variable
    text2.text("PRESS START")

    # add text to text list
    text.append(text2)

    # create first text and customize
    text3 = stage.Text(width = 22, height = 12, font = None, palette = constants.RED_PALETTE, buffer = None)

    # move text
    text3.move(24, 90)

    # assign a text to variable
    text3.text("SELECT for Info")

    # add text to text list
    text.append(text3)

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

        # check if START has been pressed
        if keys & ugame.K_START:

            # call game scene
            game_scene()

        # check if SELECT has been pressed
        if keys & ugame.K_SELECT:

            # call game scene
            instructions_scene()


        game.tick()

def instructions_scene():

    # import background and assign to a variable
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # create text list
    text = []

    # create first text and customize
    text1 = stage.Text(width = 60, height = 40, font = None, palette = constants.RED_PALETTE, buffer = None)

    # move text
    text1.move(0, 0)

    # assign a text to variable
    text1.text("Use the D-pad to\n" "move. Your ship cant\n" "hit the aliens or\n" "you will lose a life.\n" "Three losses and you\n" "lose. Press A to\n" "shoot and B for a\n" "speed boost.")

    # add text to text list
    text.append(text1)

    # create first text and customize
    text2 = stage.Text(width = 60, height = 40, font = None, palette = constants.RED_PALETTE, buffer = None)

    # move text
    text2.move(4, 110)

    # assign a text to variable
    text2.text("B to Return to Menu")

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

        # check if B has been pressed
        if keys & ugame.K_X:

            # call menu scene
            menu_scene()

# this is the main game game_scene
def game_scene():

    # initialize score
    score = 0

    # scale text size
    score_text = stage.Text(width = 29, height = 14)

    # clear score
    score_text.clear()

    # set cursor to top left
    score_text.cursor(0,0)

    # move slightly down and to the side
    score_text.move(1,1)

    # set score to whatever the value is
    score_text.text("Score: {0}".format(score))

    # initialize lives
    lives = 3

    # scale text size
    lives_text = stage.Text(width = 29, height = 14)

    # clear lives
    lives_text.clear()

    # set cursor to top left
    lives_text.cursor(80, 0)

    # move slightly down and to the side
    lives_text.move(1,1)

    # set lives to whatever the value is
    lives_text.text("Lives: {lives}")

    # function to show alien
    def show_alien():

        # loop while alien number in range of amount of aliens
        for alien_number in range(len(aliens)):

            # check if alien position is less than zero aka in storing area
            if aliens[alien_number].x < 0:

                # move alien to random part at top of screen
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                                         constants.SCREEN_X - constants.SPRITE_SIZE),
                                                         constants.OFF_TOP_SCREEN)

                # break out of loop
                break

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
    background_sound = open("news_x.wav", 'rb')
    cannon_sound = open("cannon_x.wav", 'rb')
    boom_sound = open("boom_x.wav", 'rb')
    hit_sound = open("baseball_hit.wav", 'rb')
    win_sound = open("applause_y.wav", 'rb')
    sound = ugame.audio

    # stop all sound
    sound.stop()

    # make sure audio isn't muted
    sound.mute(False)

    # play background sound
    sound.play(background_sound)

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

    # create list for aliens
    aliens = []

    # loop while in range of total number of aliens
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):

        # assign image to alien and move to off screen storing location
        a_single_alien = stage.Sprite(image_bank_sprites, 9,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)

        # append aliens to list
        aliens.append(a_single_alien)

    # call function to show alien
    show_alien()


    # create list for laser
    lasers = []

    # for loop while laser number is in range of number of total lasers
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):

        # assign image and location to laser
        a_single_laser = stage.Sprite(image_bank_sprites, 10,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)

        # append laser to list
        lasers.append(a_single_laser)

    # display images and set refresh rate to 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)

    # put images into a list assigned to game
    game.layers = [lives_text] + [score_text] + aliens + lasers + [ship] + [background]

    # display background
    game.render_block()


    # game loop
    while True:

        # get user button input
        keys = ugame.buttons.get_pressed()

        # check if B button is being pressed
        if keys & ugame.K_X:

            # check if sate is up
            if b_button == constants.BUTTON_STATE["button_up"]:

                # change to just pressed
                b_button = constants.BUTTON_STATE["button_just_pressed"]

            # else if check if it was just pressed
            elif b_button == constants.BUTTON_STATE["button_just_pressed"]:

                # change state to still pressed
                b_button = constants.BUTTON_STATE["button_still_pressed"]

                # speed boost for ship
                constants.SHIP_SPEED += 2
        else:

            # check if state is still pressed
            if b_button == constants.BUTTON_STATE["button_still_pressed"]:

                # change state to button released
                b_button = constants.BUTTON_STATE["button_released"]

                # speed boost for ship
                constants.SHIP_SPEED -= 2
            else:

                # else change state to button back up again
                b_button = constants.BUTTON_STATE["button_up"]

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

        # check if START button was pressed
        if keys & ugame.K_START:
            
            # unmute audio
            sound.mute(False)

        # check if SELECT is pressed
        if keys & ugame.K_SELECT:

            # mute all sound
            sound.mute(True)

        # check if right button is pressed
        if keys & ugame.K_RIGHT:

            # check if ship is within boundaries
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:

                # move ship 1 pixel right
                ship.move(ship.x + constants.SHIP_SPEED, ship.y)
            
            else:
                # wrap around screen
                ship.move(0, ship.y)

        # check if left button is pressed
        if keys & ugame.K_LEFT:

            # check if ship is within boundaries
            if ship.x >= 0:

                # move ship 1 pixel left
                ship.move(ship.x - constants.SHIP_SPEED, ship.y)
            
            # wrap around screen
            else:
                ship.move(160, ship.y)

        # check if the up button is being pressed
        if keys & ugame.K_UP:

            # check if ship is in boundaries
            if ship.y >= 0:

                # move ship up 1 pixel
                ship.move(ship.x, ship.y - constants.SHIP_SPEED)
            
            # prevent ship from getting out of the boundaries
            else:
                ship.move(ship.x, 0)
        
        # check if down button is being pressed
        if keys & ugame.K_DOWN:

            # check if ship is in boundaries
            if ship.y <= constants.SCREEN_Y - constants.SPRITE_SIZE:

                # move ship 1 pixel down
                ship.move(ship.x, ship.y + constants.SHIP_SPEED)
            
            # prevent ship from getting out of bounds
            else:
                ship.move(ship.x, constants.SCREEN_Y - constants.SPRITE_SIZE)

        # play sound and shoot if A button was just pressed
        if a_button == constants.BUTTON_STATE["button_just_pressed"]:
            
            # fire laser
            for laser_number in range(len(lasers)):

                # check if laser is less than 0
                if lasers[laser_number].x < 0:

                    # move laser to where ship is
                    lasers[laser_number].move(ship.x, ship.y)
            
                    # play cannon sound
                    sound.play(cannon_sound)

                    # break out of loop
                    break

        # for loop while laser number in range of amount of lasers
        for laser_number in range(len(lasers)):

            # check if laser number position is above 0
            if lasers[laser_number].x > 0:

                # move laser
                lasers[laser_number].move(lasers[laser_number].x,
                                          lasers[laser_number].y -
                                          constants.LASER_SPEED)

                # check if laser y position is off the screen
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:

                    # move laser to off screen storing location
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # for loop while alien number in range of amount of aliens
        for alien_number in range(len(aliens)):

            # check if alien x position is larger than 0
            if aliens[alien_number].x > 0:

                # move alien down
                aliens[alien_number].move(aliens[alien_number].x,
                                          aliens[alien_number].y +
                                          constants.ALIEN_SPEED)

                # check if alien is off screen
                if aliens[alien_number]. y > constants.SCREEN_Y:

                    # move alien to off screen storing location
                    aliens[alien_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)

                    # call function to show alien
                    show_alien()

                    # subtract one from score
                    score -= 1

                    # check if score falls under 0
                    if score < 0:

                        # keep score 0
                        score = 0
    
                    # clear score text
                    score_text.clear()

                    # reposition in top left of screen
                    score_text.cursor(0,0)
                    score_text.move(1,1)

                    # display score
                    score_text.text("Score: {0}".format(score))

            # loop through lasers
            for laser_number in range(len(lasers)):

                # check if laser is on screen
                if lasers[laser_number].x > 0:

                    # loop through aliens
                    for alien_number in range(len(aliens)):

                        # check if alien is on screen
                        if aliens[alien_number].x > 0:

                            # set bounding box and size them down to fit image sizes
                            if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                             lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                             aliens[alien_number].x + 1, aliens[alien_number].y,
                                             aliens[alien_number].x + 15, aliens[alien_number].y + 15):

                                # you hit an alien, move them off screen to staging
                                aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                                lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

                                # stop all sound
                                sound.stop()

                                # play boom sound
                                sound.play(boom_sound)

                                # call function to show aliens
                                show_alien()
                                show_alien()

                                # add one to score
                                score = score + 1

                                # clear text
                                score_text.clear()

                                # position score in top left
                                score_text.cursor(0,0)
                                score_text.move(1,1)

                                # display text
                                score_text.text("Score: {0}".format(score))

            # check if alien hits ship
            for alien_number in range(len(aliens)):

                # check if alien is on screen
                if aliens[alien_number].x > 0:

                    # check if alien hits ship bounding box
                    if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                     aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                     ship.x, ship.y,
                                     ship.x + 15, ship.y + 15):

                        # alien has hit ship, stop sound
                        sound.stop()

                        # play hit sound
                        sound.play(hit_sound)

                        # subtract one from lives
                        lives = lives - 1

                        # clear lives text
                        lives_text.clear()

                        # reposition in top right of screen
                        lives_text.cursor(80, 0)
                        lives_text.move(1, 1)

                        # display lives
                        lives_text.text("Lives: {lives}")

                        # check if lives falls under 0
                        if lives == 0:

                            # wait 3 seconds
                            time.sleep(3.0)

                            # pass score to game over scene function
                            game_over_scene(score)

        # if player gets 50 points they win
        if score == 30:

            # stop sound
            sound.stop()

            # make sure audio isn't muted
            sound.mute(False)

            # play applause sound
            sound.play(win_sound)

            # call you win scene
            game_scene_two(score, lives)

        # redraw sprites
        game.render_sprites(aliens + lasers + [ship])
        game.tick()

# this is the main game game_scene
def game_scene_two(current_score, current_lives):

    # initialize score
    score = current_score

    # scale text size
    score_text = stage.Text(width = 29, height = 14)

    # clear score
    score_text.clear()

    # set cursor to top left
    score_text.cursor(0,0)

    # move slightly down and to the side
    score_text.move(1,1)

    # set score to whatever the value is
    score_text.text("Score: {0}".format(score))

    # initialize lives
    lives = current_lives

    # scale text size
    lives_text = stage.Text(width = 29, height = 14)

    # clear lives
    lives_text.clear()

    # set cursor to top left
    lives_text.cursor(80, 0)

    # move slightly down and to the side
    lives_text.move(1,1)

    # set lives to whatever the value is
    lives_text.text("Lives: {lives}")

    # function to show alien
    def show_alien():

        # loop while alien number in range of amount of aliens
        for alien_number in range(len(aliens)):

            # check if alien position is less than zero aka in storing area
            if aliens[alien_number].x < 0:

                # move alien to random part at top of screen
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                                         constants.SCREEN_X - constants.SPRITE_SIZE),
                                                         constants.OFF_TOP_SCREEN)

                # break out of loop
                break

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
    #background_sound = open("news_x.wav", 'rb')
    shoot_sound = open("feedback_x.wav", 'rb')
    boom_sound = open("boom_x.wav", 'rb')
    hit_sound = open("baseball_hit.wav", 'rb')
    win_sound = open("applause_y.wav", 'rb')
    sound = ugame.audio

    # stop all sound
    sound.stop()

    # make sure audio isn't muted
    sound.mute(False)

    # play background sound
    sound.play(background_sound)

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

    # create list for aliens
    aliens = []

    # loop while in range of total number of aliens
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):

        # assign image to alien and move to off screen storing location
        a_single_alien = stage.Sprite(image_bank_sprites, 8,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)

        # append aliens to list
        aliens.append(a_single_alien)

    # call function to show alien
    show_alien()


    # create list for laser
    lasers = []

    # for loop while laser number is in range of number of total lasers
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):

        # assign image and location to laser
        a_single_laser = stage.Sprite(image_bank_sprites, 13,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)

        # append laser to list
        lasers.append(a_single_laser)

    # display images and set refresh rate to 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)

    # put images into a list assigned to game
    game.layers = [lives_text] + [score_text] + aliens + lasers + [ship] + [background]

    # display background
    game.render_block()


    # game loop
    while True:

        # get user button input
        keys = ugame.buttons.get_pressed()

        # check if B button is being pressed
        if keys & ugame.K_X:

            # check if sate is up
            if b_button == constants.BUTTON_STATE["button_up"]:

                # change to just pressed
                b_button = constants.BUTTON_STATE["button_just_pressed"]

            # else if check if it was just pressed
            elif b_button == constants.BUTTON_STATE["button_just_pressed"]:

                # change state to still pressed
                b_button = constants.BUTTON_STATE["button_still_pressed"]

                # speed boost for ship
                constants.SHIP_SPEED += 2
        else:

            # check if state is still pressed
            if b_button == constants.BUTTON_STATE["button_still_pressed"]:

                # change state to button released
                b_button = constants.BUTTON_STATE["button_released"]

                # speed boost for ship
                constants.SHIP_SPEED -= 2
            else:

                # else change state to button back up again
                b_button = constants.BUTTON_STATE["button_up"]

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

        # check if START button was pressed
        if keys & ugame.K_START:
            
            # unmute audio
            sound.mute(False)

        # check if SELECT is pressed
        if keys & ugame.K_SELECT:

            # mute all sound
            sound.mute(True)

        # check if right button is pressed
        if keys & ugame.K_RIGHT:

            # check if ship is within boundaries
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:

                # move ship 1 pixel right
                ship.move(ship.x + constants.SHIP_SPEED, ship.y)
            
            else:
                # wrap around screen
                ship.move(0, ship.y)

        # check if left button is pressed
        if keys & ugame.K_LEFT:

            # check if ship is within boundaries
            if ship.x >= 0:

                # move ship 1 pixel left
                ship.move(ship.x - constants.SHIP_SPEED, ship.y)
            
            # wrap around screen
            else:
                ship.move(160, ship.y)

        # check if the up button is being pressed
        if keys & ugame.K_UP:

            # check if ship is in boundaries
            if ship.y >= 0:

                # move ship up 1 pixel
                ship.move(ship.x, ship.y - constants.SHIP_SPEED)
            
            # prevent ship from getting out of the boundaries
            else:
                ship.move(ship.x, 0)
        
        # check if down button is being pressed
        if keys & ugame.K_DOWN:

            # check if ship is in boundaries
            if ship.y <= constants.SCREEN_Y - constants.SPRITE_SIZE:

                # move ship 1 pixel down
                ship.move(ship.x, ship.y + constants.SHIP_SPEED)
            
            # prevent ship from getting out of bounds
            else:
                ship.move(ship.x, constants.SCREEN_Y - constants.SPRITE_SIZE)

        # play sound and shoot if A button was just pressed
        if a_button == constants.BUTTON_STATE["button_just_pressed"]:
            
            # fire laser
            for laser_number in range(len(lasers)):

                # check if laser is less than 0
                if lasers[laser_number].x < 0:

                    # move laser to where ship is
                    lasers[laser_number].move(ship.x, ship.y)
            
                    # play shoot sound
                    sound.play(shoot_sound)

                    # break out of loop
                    break

        # for loop while laser number in range of amount of lasers
        for laser_number in range(len(lasers)):

            # check if laser number position is above 0
            if lasers[laser_number].x > 0:

                # move laser
                lasers[laser_number].move(lasers[laser_number].x,
                                          lasers[laser_number].y -
                                          constants.LASER_SPEED)

                # check if laser y position is off the screen
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:

                    # move laser to off screen storing location
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # for loop while alien number in range of amount of aliens
        for alien_number in range(len(aliens)):

            # check if alien x position is larger than 0
            if aliens[alien_number].x > 0:

                # move alien down
                aliens[alien_number].move(aliens[alien_number].x,
                                          aliens[alien_number].y +
                                          constants.ALIEN_SPEED)

                # check if alien is off screen
                if aliens[alien_number]. y > constants.SCREEN_Y:

                    # move alien to off screen storing location
                    aliens[alien_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)

                    # call function to show alien
                    show_alien()

                    # subtract one from score
                    score -= 1

                    # check if score falls under 0
                    if score < 0:

                        # keep score 0
                        score = 0
    
                    # clear score text
                    score_text.clear()

                    # reposition in top left of screen
                    score_text.cursor(0,0)
                    score_text.move(1,1)

                    # display score
                    score_text.text("Score: {0}".format(score))

            # loop through lasers
            for laser_number in range(len(lasers)):

                # check if laser is on screen
                if lasers[laser_number].x > 0:

                    # loop through aliens
                    for alien_number in range(len(aliens)):

                        # check if alien is on screen
                        if aliens[alien_number].x > 0:

                            # set bounding box and size them down to fit image sizes
                            if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                             lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                             aliens[alien_number].x + 1, aliens[alien_number].y,
                                             aliens[alien_number].x + 15, aliens[alien_number].y + 15):

                                # you hit an alien, move them off screen to staging
                                aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                                lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

                                # stop all sound
                                sound.stop()

                                # play boom sound
                                sound.play(boom_sound)

                                # call function to show aliens
                                show_alien()
                                show_alien()

                                # add one to score
                                score = score + 1

                                # clear text
                                score_text.clear()

                                # position score in top left
                                score_text.cursor(0,0)
                                score_text.move(1,1)

                                # display text
                                score_text.text("Score: {0}".format(score))

            # check if alien hits ship
            for alien_number in range(len(aliens)):

                # check if alien is on screen
                if aliens[alien_number].x > 0:

                    # check if alien hits ship bounding box
                    if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                     aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                     ship.x, ship.y,
                                     ship.x + 15, ship.y + 15):

                        # alien has hit ship, stop sound
                        sound.stop()

                        # play hit sound
                        sound.play(hit_sound)

                        # subtract one from lives
                        lives = lives - 1

                        # clear lives text
                        lives_text.clear()

                        # reposition in top right of screen
                        lives_text.cursor(80, 0)
                        lives_text.move(1, 1)

                        # display lives
                        lives_text.text("Lives: {lives}")

                        # check if lives falls under 0
                        if lives == 0:

                            # wait 3 seconds
                            time.sleep(3.0)

                            # pass score to game over scene function
                            game_over_scene(score)

        # if player gets 60 points they win
        if score == 60:

            # stop sound
            sound.stop()

            # make sure audio isn't muted
            sound.mute(False)

            # play applause sound
            sound.play(win_sound)

            # call you win scene
            win_scene()

        # redraw sprites
        game.render_sprites(aliens + lasers + [ship])
        game.tick()

def win_scene():

    # access image bank
    image_bank_3 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set image to 0 in bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # add text list
    text = []

    # customize text
    text1 = stage.Text(width=50, height=40, font=None, palette=constants.RED_PALETTE, buffer=None)

    # move text
    text1.move(49, 20)

    # display final score
    text1.text("You win!")

    # append to text list
    text.append(text1)

    # customize text 2
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)

    # move text 3
    text2.move(32, 110)

    # create text for text 3
    text2.text("PRESS SELECT")

    # append text to text list
    text.append(text2)

     # set frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # add text to game layer with background
    game.layers = text + [background]

    # display background and text
    game.render_block()

    # game loop
    while True:

        # get user input
        keys = ugame.buttons.get_pressed()

        # check if SELECT was pressed
        if keys & ugame.K_SELECT != 0:

            # reset PyBadge
            supervisor.reload()

            # game tick
            game.tick()

# game over scene function
def game_over_scene(final_score):

    # turn off sound
    sound = ugame.audio
    sound.stop()

    # access image bank
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set image to 0 in bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # add text list
    text = []

    # customize text
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)

    # move text
    text1.move(22, 20)

    # display final score
    text1.text("Final Score: {:0>2d}".format(final_score))

    # append to text list
    text.append(text1)

    # customize text 2
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)

    # move text 2
    text2.move(43, 60)

    # assign text to variable
    text2.text("Game Over")

    # append text to text list
    text.append(text2)

    # customize text 3
    text3 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)

    # move text 3
    text3.move(32, 110)

    # create text for text 3
    text3.text("PRESS SELECT")

    # append text to text list
    text.append(text3)

    # set frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # add text to game layer with background
    game.layers = text + [background]

    # display background and text
    game.render_block()

    # game loop
    while True:

        # get user input
        keys = ugame.buttons.get_pressed()

        # check if SELECT was pressed
        if keys & ugame.K_SELECT != 0:

            # reset PyBadge
            supervisor.reload()

        # game tick
        game.tick()

if __name__ == "__main__":
    splash_scene()

#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Jan. 10, 2024
# This program contains constants for the Space Aliens game.

# PyBadge screen size is 160x128
SCREEN_X = 160
SCREEN_Y = 128

# grid of the screen, how much of the 16x16 images it can fit
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8

# size of sprite
SPRITE_SIZE = 16

# total number of aliens
TOTAL_NUMBER_OF_ALIENS = 5

# declare total number of aliens in second level
TOTAL_NUMBER_OF_ALIENS_TWO = 3

# declare total number of lasers
TOTAL_NUMBER_OF_LASERS = 5

# declare ship speed
SHIP_SPEED = 1

# declare alien speed
ALIEN_SPEED = 1

# declare second alien speed
ALIEN_SPEED_TWO = 1

# declare laser speed
LASER_SPEED = 2

# declare off screen x value
OFF_SCREEN_X = -100

# declare off screen y value
OFF_SCREEN_Y = -100

# declare off top of screen
OFF_TOP_SCREEN = -1 * SPRITE_SIZE

# declare off bottom of screen
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE

# 60 FPS
FPS = 60

# Movement speed/how much it moves
SPRITE_MOVEMENT_SPEED = 1

# create a dictionary of all possible button states
BUTTON_STATE = {
    "button_up" : "up",
    "button_just_pressed" : "just pressed",
    "button_still_pressed" : "still pressed",
    "button_released" : "released"
}

# new palette for red filled text
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
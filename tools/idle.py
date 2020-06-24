# coding=UTF-8
"""
Keeps the OSRS client logged in.

"""
import logging as log
import random as rand
from ocvbot import input, misc, vision as vis

# Focus the client.
input.Mouse(region=vis.chat_menu).click_coord(move_away=True)

while True:
    # Every 3-5 minutes, hit an arrow key to move the client's camera.
    misc.sleep_rand(180000, 299000)
    key = rand.randint(1, 4)
    log.info('Hitting arrow key')
    if key == 1:
        input.Keyboard().keypress('left')
    elif key == 2:
        input.Keyboard().keypress('right')
    elif key == 3:
        input.Keyboard().keypress('up')
    elif key == 4:
        input.Keyboard().keypress('down')

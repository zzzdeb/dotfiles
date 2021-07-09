#!/usr/bin/env python3

import copy_selected
import os
from utils import parse_text_content, send_command_to_qute, to_clipboard

copy_selected.main()

send_command_to_qute("buffer naver")


from pynput.keyboard import Key, Controller

keyboard = Controller()
from time import sleep
sleep(1)
with keyboard.pressed(Key.ctrl):
    keyboard.press('v')
    keyboard.release('v')

keyboard.press('i')
keyboard.release('i')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

#!/usr/bin/env python

from i3ipc import Connection
import sys

REVERSE = {'right':'left', 'left': 'right', 'down':'up', 'up':'down'}

if __name__ == "__main__":
    direction = sys.argv[1]
    i3 = Connection()
    last_focused = i3.get_tree().find_focused()
    if not last_focused.fullscreen_mode:
        i3.command('focus '+direction)
        sys.exit()

    i3.command('fullscreen; focus '+direction)
    cur_focused = i3.get_tree().find_focused()
    if last_focused.workspace().id == cur_focused.workspace().id:
        i3.command('fullscreen')
        sys.exit()

    last_focused.command('fullscreen')

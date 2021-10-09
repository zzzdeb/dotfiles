#!/usr/bin/env python3

from i3ipc import Connection
import sys

REVERSE = {'right':'left', 'left': 'right', 'down':'up', 'up':'down'}

if __name__ == "__main__":
    direction = sys.argv[1]
    i3 = Connection()
    last_focused = i3.get_tree().find_focused()
    if not last_focused.fullscreen_mode:
        last_focused.command('focus '+direction)
        sys.exit()

    last_focused.command('fullscreen')
    last_focused.command('focus '+direction)
    cur_focused = i3.get_tree().find_focused()
    if last_focused.workspace().id == cur_focused.workspace().id:
        cur_focused.command('fullscreen')
    else:
        last_focused.command('focus; fullscreen')
    sys.exit()

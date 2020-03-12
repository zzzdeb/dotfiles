#!/usr/bin/env python
from gi.repository import Gdk; 
import sys

screen=Gdk.Screen.get_default()
for i in range(0, screen.get_n_monitors()):
    if screen.get_monitor_plug_name(i) == sys.argv[1]:
        geo = screen.get_monitor_geometry(i)
        xs = '+' if geo.x>=0 else '-'
        ys = '+' if geo.y>=0 else '-'
        print('{}x{}{}{}{}{}'.format(geo.width, geo.height, xs, geo.x, ys, geo.y))

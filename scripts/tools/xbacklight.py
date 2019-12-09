#!/usr/bin/env python

import sys
from pathlib import Path
import subprocess
if __name__ == "__main__":

    value=1.0
    value_path = Path("/tmp/xbacklight.value")

    if value_path.is_file():
        with open(value_path,"r") as f:
            value=float(f.readline())

    nvalue= value+float(sys.argv[2])
    nvstring='%.1f'%nvalue
    subprocess.run(["xrandr", "--output", sys.argv[1], "--brightness", nvstring])
    subprocess.run(["dunstify", "--replace=10", nvstring])

    with open(value_path,"w") as f:
        f.write(nvstring)


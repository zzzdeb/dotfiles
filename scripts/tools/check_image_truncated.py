#!/usr/bin/env python
from PIL import ImageFile
import sys


with open(sys.argv[1], 'rb') as f:
    p = ImageFile.Parser()
    while 1:
        s = f.read(1024)
        if not s:
            break
        p.feed(s)
    try:
        p.close()
        sys.exit(0)
    except OSError:
        sys.exit(1)

#!/usr/bin/env python3

import os
import html
import re
import sys
from utils import parse_text_content, send_command_to_qute, to_clipboard

def main():
    delimiter = sys.argv[1] if len(sys.argv) > 1 else ";"
    # For info on qute environment vairables, see
    # https://github.com/qutebrowser/qutebrowser/blob/master/doc/userscripts.asciidoc
    element = os.environ.get("QUTE_SELECTED_HTML")
    if element != None:
        text = parse_text_content(element)
    else:
        text = os.environ.get("QUTE_SELECTED_TEXT")
    to_clipboard(text, delimiter=delimiter)

    # notify
    send_command_to_qute(
        "message-info 'copied to clipboard: {info}{suffix}'".format(
            info=text.splitlines()[0],
            suffix="..." if len(text.splitlines()) > 1 else ""
        )
    )

if __name__ == "__main__":
    main()

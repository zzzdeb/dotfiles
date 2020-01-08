#!/usr/bin/env python3

import os
import html
import re
import sys

try:
    import pyperclip
except ImportError:
    PYPERCLIP = False
else:
    PYPERCLIP = True
import bs4


def parse_text_content(element):
    text = bs4.BeautifulSoup(element).text.strip()
    return text


def send_command_to_qute(command):
    with open(os.environ.get("QUTE_FIFO"), "w", encoding="utf-8") as f:
        f.write(command)

def to_clipboard(text, delimiter=';'):
    if PYPERCLIP:
        pyperclip.copy(text)
    else:
        # Qute's yank command  won't copy accross multiple lines so we
        # compromise by placing lines on a single line seperated by the
        # specified delimiter
        code_text = re.sub("(\n)+", delimiter, text)
        code_text = code_text.replace("'", "\"")
        send_command_to_qute("yank inline '{code}'\n".format(code=text))

def get_element_text(search_in_selected=True):
    element = os.environ.get("QUTE_SELECTED_HTML")
    if element == None:
        text = os.environ.get("QUTE_SELECTED_TEXT")
    else:
        text = parse_text_content(element)
    return text

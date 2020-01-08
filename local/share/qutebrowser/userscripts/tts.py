#!/usr/bin/env python3

import subprocess
import os
import html
import sys
import xml.etree.ElementTree as ET
from gtts import gTTS
import re
try:
    import pyperclip
except ImportError:
    PYPERCLIP = False
else:
    PYPERCLIP = True

from utils import send_command_to_qute, parse_text_content

TTS_MP3 = '/tmp/qutebrowser_tts.mp3'

def parse_text_content(element):
    root = ET.fromstring(element)
    # https://bilingualmanga.com/manga/yotsubato/chapter-1/5-2 specific
    for ruby in root.iter('ruby'):
        for rt in ruby.findall('rt'):
            ruby.remove(rt)
    text = ET.tostring(root, encoding="unicode", method="text")
    text = html.unescape(text)
    return text

def main():
    lang = 'ja'
    cmd = sys.argv[1] if len(sys.argv) > 1 else ";"
    if cmd == 'replay':
        returned_value = subprocess.call('mpv '+TTS_MP3, shell=True)  # returns the exit code in unix
        return
    elif cmd == 'play':
        if len(sys.argv) > 2:
            lang = sys.argv[2]
    # For info on qute environment vairables, see
    # https://github.com/qutebrowser/qutebrowser/blob/master/doc/userscripts.asciidoc
    element = os.environ.get("QUTE_SELECTED_HTML")
    if element == None:
        text = os.environ.get("QUTE_SELECTED_TEXT")
    else:
        text = parse_text_content(element)

    # playing
    tts = gTTS(text, lang=lang)
    tts.save(TTS_MP3)
    returned_value = subprocess.call('mpv '+TTS_MP3, shell=True)  # returns the exit code in unix

    return


if __name__ == "__main__":
    main()



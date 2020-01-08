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

def send_command_to_qute(command):
    with open(os.environ.get("QUTE_FIFO"), "w") as f:
        f.write(command)

def main():
    lang = 'ja'
    cmd = sys.argv[1] if len(sys.argv) > 1 else ";"
    if cmd == 'replay':
        returned_value = subprocess.call('mpv '+TTS_MP3, shell=True)  # returns the exit code in unix
        return
    elif cmd == 'play':
        lang = sys.argv[2] if len(sys.argv) > 2 else "en"
    #  else:
        #  return 1
    # For info on qute environment vairables, see
    # https://github.com/qutebrowser/qutebrowser/blob/master/doc/userscripts.asciidoc
    element = os.environ.get("QUTE_SELECTED_HTML")
    text = parse_text_content(element)

    # coping
    delimiter = ';'
    if PYPERCLIP:
        pyperclip.copy(text)
        send_command_to_qute(
            "message-info 'copied to clipboard: {info}{suffix}'".format(
                info=text.splitlines()[0],
                suffix="..." if len(text.splitlines()) > 1 else ""
            )
        )
    else:
        # Qute's yank command  won't copy accross multiple lines so we
        # compromise by placing lines on a single line seperated by the
        # specified delimiter
        text = re.sub("(\n)+", delimiter, text)
        text = text.replace("'", "\"")
        send_command_to_qute("yank inline '{code}'\n".format(code=text))

    # playing
    tts = gTTS(text, lang=lang)
    tts.save(TTS_MP3)
    returned_value = subprocess.call('mpv '+TTS_MP3, shell=True)  # returns the exit code in unix

    return


if __name__ == "__main__":
    main()



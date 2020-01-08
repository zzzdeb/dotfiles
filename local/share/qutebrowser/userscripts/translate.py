#!/usr/bin/env python3
from utils import get_element_text, send_command_to_qute
from urllib.parse import urlencode, urlparse, parse_qsl, urlunparse
import clipboard
import urllib.parse as pr
import sys, os
import re

def main():
    # For info on qute environment vairables, see
    # https://github.com/qutebrowser/qutebrowser/blob/master/doc/userscripts.asciidoc
    sl = sys.argv[1] if len(sys.argv) > 2 else "auto"
    destl = sys.argv[2] if len(sys.argv) > 2 else "en"
    qute_command = 'open -t'
    listed = [ 'https', 'translate.google.com', '/', '', '', 'view=home' ]
    frag = {
            'view':'home',
            'op':'translate',
            'sl': sl,
            'tl': destl
           }

    text = get_element_text()
    if text == '':
        # from clipboard
        text = clipboard.paste()

        # if in google translate alraidy, just change language
        url = os.environ.get("QUTE_URL")
        parsed_url = urlparse(url)
        if parsed_url.netloc == 'translate.google.com':
            # dont create new tab
            qute_command = 'open '
            frag.update(dict(parse_qsl(parsed_url.fragment)))
            frag['tl'] = destl
            try:
                # have to set it here cause text is used
                text = frag['text']
                listed = list(parsed_url)
            except KeyError:
                pass

    #  send_command_to_qute('open -t http://dict.leo.org/german-english/'+text)
    text = text.replace('%', '^')
    frag['text']=text
    listed[-1] = urlencode(frag)

    send_command_to_qute(qute_command + ' ' + urlunparse(listed))
    return

if __name__ == "__main__":
    main()



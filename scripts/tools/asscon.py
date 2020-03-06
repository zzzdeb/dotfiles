#!/usr/bin/env python

import ass
import os

doc = ass.document.Document()
docs = []
asss = os.listdir()
asss.sort()

for fn in asss:
    if fn.endswith('.ass'):
        with open(fn, encoding='utf_8_sig') as f:
            doc.events += ass.parse(f).events

style = ass.section.Style()
style.fontsize = 10
style.primary_color = ass.data.Color(r=0x70, g=0x6b, b=0x6c)
style.secondary_color = ass.data.Color(r=0x70, g=0x6b, b=0x6c)
style.margin_v = -1
style.alignment = 8
style.shadow = 0
style.outline = 0
doc.styles.append(style)

with open('out.ass', 'w', encoding='utf_8_sig') as f:
    doc.dump_file(f)

#!/usr/bin/env python

import fbchat as fb

import subprocess as sp
from subprocess import PIPE

import clipboard
import ast

DMENU = ['rofi','-dmenu','-theme',"/usr/share/rofi/themes/DarkBlue.rasi"]
FBUSERSPATH = '/tmp/fbusers.list'

import os.path

username = ''
if os.path.isfile(FBUSERSPATH):
    with open(FBUSERSPATH, 'r') as f:
        users_dict_fromstr = ast.literal_eval(f.read())

    userNames = '\n'.join(list(users_dict_fromstr.values()))
    p = sp.Popen(DMENU, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                universal_newlines=True)
    username = p.communicate(input=userNames)[0][:-1]

# creating message
p = sp.Popen(DMENU+['-l'+'0'], stdin=PIPE, stdout=PIPE, stderr=PIPE,
            universal_newlines=True)
message = p.communicate()[0]
if message == '**\n':
    message = clipboard.paste()

# getting pass
p = sp.Popen(['pass', 'facebook.com/deb_zolboo@yahoo.com'], stdin=PIPE, stdout=PIPE, stderr=PIPE,
            universal_newlines=True)
fbpass = p.communicate()[0][:-1]
# connection
client = fb.Client('deb_zolboo@yahoo.com', fbpass)
try:
    # getting username
    users = client.fetchAllUsers()
    user_dict = {a.uid: a.name for a in users}
    with open(FBUSERSPATH, 'w') as f:
        f.write(str(user_dict))

    if not username in user_dict.values():
        userNames = '\n'.join([a.name for a in users])
        p = sp.Popen(DMENU, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                    universal_newlines=True)
        username = p.communicate(input=userNames)[0][:-1]

    # getting user by name
    userto = list(filter(lambda x: x.name == username, users))[0]
    useruid = userto.uid

    #sending
    client.sendMessage(message, thread_id=useruid)
    p = sp.Popen(['notify-send', 'Message sent!'], stdin=PIPE, stdout=PIPE, stderr=PIPE,
                universal_newlines=True)
    p.communicate()
    client.logout()

except:
    p = sp.Popen(['notify-send', 'Failed to send message'], stdin=PIPE, stdout=PIPE, stderr=PIPE,
                universal_newlines=True)
    p.communicate()
    client.logout()

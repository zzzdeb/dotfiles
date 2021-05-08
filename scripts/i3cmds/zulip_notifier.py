#!/usr/bin/env python3

import time
import sys

import zulip
from notifypy import Notify

if __name__ == '__main__':
    # Pass the path to your zuliprc file here.
    client = zulip.Client(config_file="~/.zuliprc")
    while(True):

        # Get the 100 last messages sent by "iago@zulip.com" to the stream "Verona"
        res = client.get_messages({
            "anchor": "first_unread",
            "num_before":100,
            "num_after":0,
            "narrow":[
                {"operator":"is", "operand":'private'},
                {"operator":"is", "operand":"unread"}
            ]
        })

        if res['result'] != 'success':
            break

        msgs = res['messages']
        if len(msgs)> 0:
            unread_msgs_num = len(msgs)
            title = "📬 {}".format(unread_msgs_num)
            print(title)
            msg = msgs[0]
            content = msg['content']
            notification = Notify()
            notification.title = title
            notification.message = content
            #  notification.icon = "path/to/icon.png"

            notification.send()

        time.sleep(5)

    sys.exit(1)

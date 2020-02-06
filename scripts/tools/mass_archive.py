#!/usr/bin/env python


import os, sys
import subprocess as sp
from subprocess import PIPE
import string, random

p = sp.Popen(['pass', 'zip'], stdin=PIPE, stdout=PIPE, stderr=PIPE,
            universal_newlines=True)
zippass = p.communicate()[0][:-1]
ZIP=['7z', 'a', '-p'+zippass, '-mhe=on']

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for x in range(size))


if __name__ == "__main__":
    randomname = random_generator()+'.txt'
    f = open(randomname, 'w')
    for filename in os.listdir('.'):
        print(filename)
        if filename == randomname:
            continue

        # create random name
        zipname = random_generator()+'.7z'
        f.write(zipname+'\t'+filename+'\n')
        # zip theme
        p = sp.Popen(ZIP+['/media/BACKUP/Backup/jaa/onedrive/asdfas/new/'+zipname]+[filename], stdin=PIPE, stdout=PIPE, stderr=PIPE,
                    universal_newlines=True)
        p.communicate()[0]

    f.close()
    p = sp.Popen(ZIP+['/media/BACKUP/Backup/jaa/onedrive/asdfas/new/'+'names.7z']+[randomname], stdin=PIPE, stdout=PIPE, stderr=PIPE,
                universal_newlines=True)
    p.communicate()[0]

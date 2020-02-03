#!/usr/bin/env python
import copy
import sys
import math
import PyPDF2

def split_pages(src, dst):
    m = {'l':10, 'u':10, 'r':20, 'd':15}
    src_f = open(src, 'r+b')
    dst_f = open(dst, 'w+b')

    input = PyPDF2.PdfFileReader(src_f)
    output = PyPDF2.PdfFileWriter()
    current = 1

    for i in range(input.getNumPages()):
        p = input.getPage(i)
        q = copy.copy(p)
        q.mediaBox = copy.copy(p.mediaBox)

        x1, x2 = p.mediaBox.lowerLeft
        x3, x4 = p.mediaBox.upperRight
        #print('{} {} {} {}'.format(x1, x2, x3, x4))

        x1, x2 = math.floor(x1), math.floor(x2)
        x3, x4 = math.floor(x3), math.floor(x4)
        x5, x6 = math.floor(x3/2), math.floor(x4/2)

        if x3 > x4:
            # horizontal
            p.mediaBox.upperRight = (x5-m['d'], x4-m['r'])
            p.mediaBox.lowerLeft = (x1+m['u'], x2+m['l'])

            q.mediaBox.upperRight = (x3-m['d'], x4-m['u'])
            q.mediaBox.lowerLeft = (x5+m['u'], x2+m['l'])
        else:
            # vertical
            p.mediaBox.upperRight = (x3-m['d'], x4-m['r'])
            p.mediaBox.lowerLeft = (x1+m['u'], x6+m['l'])
            #rint('p {} {}'.format(p.mediaBox.upperRight,
            #                             p.mediaBox.lowerLeft))

            q.mediaBox.upperRight = (x3-m['d'], x6-m['r'])
            q.mediaBox.lowerLeft = (x1+m['u'], x2+m['l'])
            #rint('q {} {}'.format(q.mediaBox.upperRight, q.mediaBox.lowerLeft))

        if current:
            output.insertPage(p, index=i)
            output.insertPage(q, index=i+1)
        else:
            output.insertPage(q, index=i)
            output.insertPage(p, index=i+1)

        current += 1
        current %= 2



    output.write(dst_f)

    #  output1.write(dst_f)
    src_f.close()
    dst_f.close()

input_file = sys.argv[1]
output_file = sys.argv[2]

split_pages(input_file, output_file)

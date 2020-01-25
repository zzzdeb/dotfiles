#!/usr/bin/env python
import copy
import sys
import math
import PyPDF2

M = {'l':10, 'u':10, 'r':12, 'd':35}

def crop(src, dst, m):
    src_f = open(src, 'r+b')
    dst_f = open(dst, 'w+b')

    input = PyPDF2.PdfFileReader(src_f)

    output = PyPDF2.PdfFileWriter()
    output.cloneDocumentFromReader(input)
    #  current = 1

    for i in range(input.getNumPages()):
        p = output.getPage(i)

        x1, x2 = p.mediaBox.lowerLeft
        x3, x4 = p.mediaBox.upperRight
        print('{} {} {} {}'.format(x1, x2, x3, x4))

        # vertical
        p.mediaBox.lowerLeft = (x1+m['l'], x2+m['d'])
        p.mediaBox.upperRight = (x3-m['r'], x4-m['u'])

        #  output.addPage(p)


    output.write(dst_f)

    #  output1.write(dst_f)
    src_f.close()
    dst_f.close()

input_file = sys.argv[1]
output_file = sys.argv[2]

crop(input_file, output_file, M)

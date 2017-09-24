# -*- coding: UTF-8 -*-
import os

if __name__ == '__main__':
    path = os.getcwd()
    filenames = []
    sum_ann = 0
    sum_blank = 0
    sum_code = 0

    for filename in os.listdir(path):
        if filename.endswith('y'):
            filenames.append(filename)

    for file in filenames[0:len(filenames) - 2]:
        py_file = open(file)
        rows = py_file.readlines()
        ann_numbers = 0
        blank_numbers = 0
        code_numbers = 0
        print rows
        for row in rows:
            if row.startswith('#', 0, len(row)):
                ann_numbers += 1
            elif row.isspace():
                blank_numbers += 1
            else:
                code_numbers += 1
        sum_ann += ann_numbers
        sum_blank += blank_numbers
        sum_code += code_numbers
    print "代码行数：", sum_code
    print "注释行数：", sum_ann
    print "空格行数：", sum_blank

# -*- coding: UTF-8 -*-
import re


def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


if __name__ == '__main__':
    words = open('filtered_words.txt', 'r')
    contents = words.readlines()
    flag = 0
    input_word = raw_input("please enter your sentence:")
    for content in contents:
        content = ' '.join(content.split())
        pattern = re.compile(re.escape(content))
        match = re.match(pattern, input_word)
        if match:
            n = len(content)
            if check_contain_chinese(content):
                stars = '*' * (n / 3)
            input_word = pattern.sub(stars, input_word)
            flag = 1
            print input_word
            break
    if flag == 0:
        print input_word

# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    words = open('filtered_words.txt', 'r')
    contents = words.readlines()
    input_word = raw_input("please enter your word:")
    for content in contents:
        if input_word == content:
            print 'Freedom'
            break
        else:
            print 'Human Rights'
            break

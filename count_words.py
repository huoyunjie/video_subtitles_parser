import os
import sys
import re

from utils import *

WORDS_MODE = 1
WORDS_NUM_MODE = 3

def count_file_words(dict, words):
    for word in words:
        if dict.has_key(word) is True:
            dict[word] = dict[word] +1
        else:
            dict[word] = 1

def count_files_words(subtitles_path, subtitles_type):
    file_list = search_files(subtitles_path, subtitles_type)
    print_trace(file_list)

    dict = {}
    for file in file_list:
        # print os.path.join(SUBTITLES_PATH, file)
        with open(os.path.join(subtitles_path, file)) as diary:
            words = re.findall("[a-zA-Z]+'*-*[a-zA-z]", diary.read())
            count_file_words(dict, words)

    dict = sorted(dict.items(), key=lambda e:e[1], reverse=True)

    # print dict
    return dict

def count_words(subtitles_path, subtitles_type, out_file_name, mode):
    dict = count_files_words(subtitles_path, subtitles_type)

    fileHandle = open(os.path.join(subtitles_path, out_file_name), 'w')

    # Optimize: use string to store
    for word, num in dict:
        if mode == WORDS_MODE:
            fileHandle.write(word+'\n')
        elif mode == WORDS_NUM_MODE:
            fileHandle.write(word.ljust(50) + str(num) +'\n')
        else:
            print_error('%d mode is invalid!'%mode)
    
    fileHandle.close()

    return RET_SUCCESS
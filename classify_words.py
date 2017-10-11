
import os
from utils import *

def get_words_list_from_file(words_file):

    fileHandle_words_file = open(words_file, 'r')

    words_list = []
    for line in fileHandle_words_file.readlines():
        line = line.strip('\n')
        line = line.rstrip()

        # print line

        if words_list.count(line) == 0:
            words_list.append(line)

    fileHandle_words_file.close()

    return words_list


def classify_words(input_words_file, easy_words_file, difficult_words_file):

    fileHandle_difficultWords = open(difficult_words_file, 'w')

    input_words_list = get_words_list_from_file(input_words_file)
    easy_words_list = get_words_list_from_file(easy_words_file)
    difficult_words_list = [word for word in input_words_list if word not in easy_words_list]

    # This method do not sort
    # difficult_words_list = list(set(input_words_list) - set(easy_words_list))

    # print input_words_list
    # print easy_words_list
    # print difficult_words_list

    str = ''
    for word in difficult_words_list:
        str = str + word + '\n'

    fileHandle_difficultWords.write(str)

    fileHandle_difficultWords.close()
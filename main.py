import re

from utils import *
import parse_subtitles
import pre_video
import count_words
import trans_youdao
import classify_words

VIDEO_TYPE = '.mkv'
SUBTITLES_TYPE = '.srt'
VIDEO_PATH = 'video'
SUBTITLES_PATH = 'srt'

if __name__ == '__main__':

    # print_trace("hello", "....ok")
    # print_warning("hello", "....ok")
    # print_error("hello", "....ok")
    # print type('test')

    # Get file list
    # file_list = search_files(VIDEO_DIR_NAME, VIDEO_TYPE)
    # print_trace(file_list)

    # test = 'xx00.oo.mkv'
    # pos = test.rfind('.')
    # test_out = test[:pos+1]
    # print test_out
    # file_names = parse_files_name_without_type('xx.oo.mkv')
    # file_names = parse_files_name_without_type(file_list)
    # print_trace(file_names)


    # rename files
    # pre_video.rename_files(VIDEO_PATH, VIDEO_TYPE)

    # parse subtitles
    # parse_subtitles.parse_subtitles(VIDEO_PATH, SUBTITLES_PATH, VIDEO_TYPE, SUBTITLES_TYPE)

    # Count words
    # count_words.count_words(SUBTITLES_PATH, SUBTITLES_TYPE, 'count_words.xml', count_words.WORDS_MODE)

    # trans words
    # trans_youdao.trans_youdao_xml('srt/count_words.xml', 'srt/youdao_ml.xml', 'srt/youdao_error.xml')
    # trans_youdao.trans_youdao_xml('srt/test_input.xml', 'srt/test_output.xml', 'srt/test_output_error.xml')

    classify_words.classify_words('srt/test_input.xml', 'srt/easy_words.xml', 'srt/difficult_words.xml')
    # classify_words.test_func()
import os
import sys
import re
import urllib
import subprocess

from utils import *

def parse_subtitles(videos_dir, subtitles_dir, video_type, subtitle_type):
    file_list = []

    if os.path.isdir(videos_dir) is False:
        print_error(videos_dir, ', is invalid videos_dir!')
        return RET_FAILED

    if os.path.isdir(subtitles_dir) is False:
        print_error(subtitles_dir, ', is invalid subtitles_dir!')
        return RET_FAILED

    file_list = search_files(videos_dir, video_type)
    # os.mkdir(subtitles_dir)
    for file in file_list:
        name = parse_files_name_without_type(file)
        # print_trace(file, format(file))
        res = os.system('ffmpeg -i ' + videos_dir + '/' + file + ' -scodec srt ' + subtitles_dir + '/' + name + subtitle_type)
        if res:
            print_error(res)
            return RET_FAILED
        # ps = subprocess.Popen('ffmpeg -i ' + file + ' -scodec srt ' + subtitles_dir + '/' + name + subtitle_type)
    return RET_SUCCESS
import os

from utils import *

def rename_files(videos_path, video_type):
    # name = '1 - 3 - Supervised Learning. (12 min).mkv'
    # name_deal = name.replace(' ', '-')
    # num = name.count('.')
    # print name, name_deal, num

    # name_deal = name_deal.replace('.', '-', num-1)
    # print name_deal

    file_list = search_files(videos_path, video_type)
    print_trace(file_list)    

    for name in file_list:
        name_out = name.replace(' ', '-')
        num = name_out.count('.')
        name_out = name_out.replace('.', '-', num-1)
        
        fp_in = os.path.join(videos_path, name)
        fp_out = os.path.join(videos_path, name_out)
        os.rename(fp_in, fp_out)

    return RET_SUCCESS
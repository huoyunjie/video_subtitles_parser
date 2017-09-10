import os

RET_SUCCESS = 0
RET_FAILED = 1

def print_trace(*args):
    print '[TRACE  ]: ',
    for arg in args:
        print arg,
    print

def print_warning(*args):
    print '[WARNING]: ',
    for arg in args:
        print arg,
    print

def print_error(*args):
    print '[ERROR  ]: ',
    for arg in args:
        print arg,
    print

def search_files(path, type):
    if os.path.isdir(path) is False:
        print_error('%s is invalid path'%path)
        return None

    file_list = []
    for file in os.listdir(path):
        fp = os.path.join(path, file)
        if os.path.isfile(fp) and file.endswith(type):
            # print_trace(fp)
            # file_list.append(fp)
            file_list.append(file)
    # print_trace(file_list)
    return file_list

def parse_files_name_without_type(files):
    if type(files) is str:
        # print_trace('str')
        pos = files.rfind('.')
        name = files[:pos]
        # print name
        return name
    elif type(files) is list:
        # print_trace('list')
        name_list = []
        for file in files:
            pos = file.rfind('.')
            name = file[:pos]
            name_list.append(name)
            # print_trace(name, file_type)
        return name_list
    else:
        print_error('files is invalid')
        return None


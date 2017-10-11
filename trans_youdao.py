# -*- coding: UTF-8 -*-
import os
import sys
import re
import urllib
import subprocess
from utils import *

from utils import *

def trans_word(word, phonetic_mode):
    '''
    <h2 class="wordbook-js">
        <span class="keyword">hello</span>
                            <div class="baav">
                            <span class="pronounce">?
                                    <span class="phonetic">[h?'l??]</span>
                                                    <a href="#" title="????" class="sp dictvoice voice-js log-js" data-rel="hello&type=1" data-4log="dict.basic.ec.uk.voice"></a>
                                </span>
                                      <span class="pronounce">?
                                    <span class="phonetic">[h?'lo]</span>
                                                    <a href="#" title="????" class="sp dictvoice voice-js log-js" data-rel="hello&type=2" data-4log="dict.basic.ec.us.voice"></a>
                                </span>
                                  </div>
            </h2>
             <div class="trans-container">

   <ul>
     <li>int. ?;??</li>
     <li>n. ????, ???????????</li>
     <li>n. (Hello)??;(?)??</li>
    </ul>

    phonetic_mode: English = 0; American = -1
    '''
    url='http://dict.youdao.com/search?q=%s'%word

    content=urllib.urlopen(url)

    pattern=re.compile("<h2.*?</ul>",re.DOTALL)

    result0 = pattern.search(content.read())

    if result0 == None:
      print_error('Can not search this word: %s'%word)
      return None
    
    result1 = result0.group()

    # print  result1

    if result1.startswith('</h2></div>') == True:
      print_error('Can not translator this word: %s'%word)
      return None

    # ????
    pattern2=re.compile('<li>.*?</li>')
    trans = []
    for i in pattern2.findall(result1):
        # print i.strip('<li>').strip('</li>').decode('utf-8')
        trans.append(i.strip('<li>').strip('</li>'))
        # file_object.write(i.strip('<li>').strip('</li>')+'\n')

    # ??
    pattern3=re.compile('<span class="phonetic">.*?</span>')

    phonetic = pattern3.findall(result1)[phonetic_mode].strip('<span class="phonetic">').strip('</span>')

    return trans, phonetic

def structure_youdao_xml(word, phonetic_mode):
    '''
        <item>    <word>test</word>
        <trans><![CDATA[n. ??;??;
    vt. ??;??;
    vi. ??;??;
    n. (Test)??;(?)???]]></trans>
        <phonetic><![CDATA[[test]]]></phonetic>
        <tags></tags>
        <progress>1</progress>
    </item></wordbook>
    '''
    trans, phonetic = trans_word(word, phonetic_mode)

    # print trans, phonetic, len(phonetic)

    str = ''

    if trans == None:
        return str

    str += "</item><item>    <word>" + word + "</word>" + '\n'

    for i in range(len(trans)):
        # print i
        if i == 0:
            # file_object.write('<trans><![CDATA[' + trans[i] +)
            str += '<trans><![CDATA['

        str += trans[i]

        if i == len(trans)-1:
            # file_object.write(trans[i] + ']]></trans>')
            str += ']]></trans>'
        str += '\n'

    str += '<phonetic><![CDATA[' + phonetic + ']]></phonetic>\n'
    str += '<tags></tags>\n'
    str += '<progress>1</progress>\n'

    return str

phonetic_mode_English = 0
phonetic_mode_American = -1
phonetic_mode = phonetic_mode_American

def trans_youdao_xml(file_words, trans_out_file, trans_error_file):
    fileHandleWords = open (file_words, 'r')
    fileHandlexml = open(trans_out_file, 'w')
    errorFileHandlexml = open(trans_error_file, 'w')
    str = ''
    strOther = ''
    strTemp = ''
    trans_num = 0
    error_num = 0
    for line in fileHandleWords.readlines():
        line = line.strip('\n')
        word = line.rstrip()
        strTemp = structure_youdao_xml(word, phonetic_mode)
        if strTemp == '':
            strOther += word+'\n'
            error_num += 1
        else:
            str += strTemp
            trans_num += 1
        print 'trans_num: %d, error_num: %d' % (trans_num, error_num)

        # print word

    str += '</item></wordbook>'
    fileHandlexml.write(str)
    errorFileHandlexml.write(strOther)

    fileHandleWords.close()
    fileHandlexml.close()
    errorFileHandlexml.close()

    return RET_SUCCESS
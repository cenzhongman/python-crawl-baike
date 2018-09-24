import time
import urllib.parse as url_parse

import bs4
import os
import re

dir_path = '../../data/data1/'
file_list = os.listdir(dir_path)


def rename_file():
    for file in file_list:
        # if file.startswith('%'):
        try:
            # 编码去.html
            print(dir_path + file, dir_path + url_parse.quote(file[:-5]))
            # os.rename(dir_path + file, dir_path + url_parse.quote(file[5:]))
        except OSError as e:
            os.remove(dir_path + file)


def parse(context):
    bsobj = bs4.BeautifulSoup(context, 'html.parser', from_encoding='utf8')
    main_content = bsobj.find(name='div', attrs={'class': 'main-content'})
    out = str(main_content.get_text())
    out = re.sub('\n', ' ', out)
    out = re.sub('[\s]+', ' ', out) + '\n'
    return out[24:]


if __name__ == '__main__':
    save_path = '../../data/baike_line.txt'
    save_file = open(save_path, mode='a', encoding='utf-8')
    i = 0
    for file in file_list:
        html_file = open(dir_path + file, mode='r', encoding='utf-8')
        context = html_file.read()
        out = parse(context)
        save_file.write(out)

        i = i + 1
        if i % 1000 == 0:
            print('已经处理' + str(i) + '条数据')
    # rename_file()
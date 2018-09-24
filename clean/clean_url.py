import urllib.parse as url_parse

import os

path = 'D:/project/datainsights/NLP/data/source/dirty/baike/data/data1/'
all_url_path = 'D:/project/datainsights/NLP/data/source/dirty/baike/data/all_url.txt'
all_url_file = open(all_url_path, mode='a', encoding='utf-8')
file_list = os.listdir(path)
# for file in file_list:
#     # print('https://baike.baidu.com/item/' + url_parse.quote(file[:-5]) + '\n')
#     all_url_file.write('https://baike.baidu.com/item/' + url_parse.quote(file[:-5]) + '\n')

# 移动文件
# for file in file_list:
#     # print(path + file, path[:-2] + '/' + file)
#     shutil.move(path + file, path[:-2] + '/' + file)

# 删除小文件
for file in file_list:
    if os.path.getsize(path + file) / 1024 < 6:
        os.remove(path + file)

import jieba

i = 0

src_path = '../../data/baike_line.txt'
src_file = open(src_path, mode='r', encoding='utf-8')
src_lines = src_file.readlines()

out_path = '../../data/baike_line_participle.txt'
out_file = open(out_path, mode='a', encoding='utf-8')
for src_line in src_lines:
    small_lines = src_line.split(' ')
    for small_line in small_lines:
        word_list = jieba.cut(small_line)
        out_file.write(' '.join(word_list) + ' ')
    i = i + 1
    if i % 10000 == 0:
        print('已经处理' + str(i) + '条数据')

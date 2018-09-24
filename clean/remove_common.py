import time

# 将两个文件全部装进set里面，加起来要小于内存
line_set = set()

path1 = '../../data/baike_line.txt'
file1 = open(path1, mode='r', encoding='utf-8')
lines1 = file1.readlines()

path2 = '../../data/baike_line1.txt'
file2 = open(path2, mode='r', encoding='utf-8')
lines2 = file2.readlines()

for line1 in lines1:
    line_set.add(line1)

for line2 in lines2:
    line_set.add(line2)

if file1 in locals():
    file1.close()
if file2 in locals():
    file2.close()

# 用于保存的文件
new_path = '../../data/baike_line_new.txt'
new_file = open(new_path, mode='a', encoding='utf-8')

for new_line in line_set:
    new_file.write(new_line)

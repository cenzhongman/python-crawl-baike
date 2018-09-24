import jieba


def participle(context):
    word_list = jieba.cut(context)
    text = ' '.join(word_list)
    return text


if __name__ == '__main__':
    participle('岑忠满阿斯顿')

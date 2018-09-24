import re


def parser(context):
    if context is None:
        return

    url_clean_list = []
    url_dirty_list = re.findall(r'href=\"/item/[\S]*\"', context)

    for url in url_dirty_list:
        url_clean = 'http://baike.baidu.com' + url[6: -1]
        url_clean_list.append(url_clean)
    return url_clean_list


if __name__ == '__main__':
    print(parser('岑忠满asdasdasd'))

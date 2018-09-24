import threading

import HtmlDownloader as downloader
import HtmlParser as parser
import UrlManager as url

count = 0
mutex = threading.Lock()


def crawl():
    try:
        global count, mutex
        if mutex.acquire():
            count += 1
            new_url = url.get_new_url()
            print('正在爬第' + str(count) + '条：' + new_url)
            mutex.release()
            html = downloader.download(new_url)
            url_list = parser.parser(html)
            url.add_new_urls(url_list)
    except:
        print('未知异常')


if __name__ == '__main__':

    # 添加新的URL,并开始一轮爬取
    url.add_new_url('https://baike.baidu.com/item/%E6%99%BA%E6%85%A7%E5%9C%B0%E7%90%83/1071533')
    crawl()

    # 添加旧的URL,在进行了一轮爬取后再添加旧的
    print('已经添加旧的url')
    all_url_path = './all_url.txt'
    all_url_file = open(all_url_path, mode='r', encoding='utf-8')
    url_list = all_url_file.readlines()
    for url_1 in url_list:
        if url_1.find('http') == 0:
            url.add_old_url(url_1[:-1])

    # 开启多线程
    while url.has_new_url():
        t = None
        threads = []
        for i in range(30):
            thread = threading.Thread(target=crawl)
            threads.append(thread)

        for t in threads:
            t.setDaemon(True)
            t.start()

        if t is not None:
            t.join()

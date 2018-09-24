import urllib.request as request
import os
import sys
import logging

program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))


def download(url):
    if url is None:
        return
    try:
        response = request.urlopen(url)
        if response.getcode() == 200:
            file = open('../data/data1/' + url.split('/')[4].split('?')[0], mode='w', encoding='utf-8')
            conf = response.read().decode('utf8')
            file.write(conf)
            if file in locals():
                file.close()
            return conf
    except IOError as e:
        logging.error('IO异常' + str(e))
    except:
        logging.error('链接被拒绝')


if __name__ == '__main__':
    print(download('https://baike.baidu.com/item/%E9%87%8C%E5%A5%A5%C2%B7%E6%A2%85%E8%A5%BF/4443471?fromTaglist='))

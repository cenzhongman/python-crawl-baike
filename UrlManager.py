new_urls = set()
old_urls = set()


def is_new_url(url):
    if url not in old_urls:
        return True
    else:
        return False


def add_new_url(url):
    if url is None:
        return

    if is_new_url(url):
        new_urls.add(url)
    else:
        return


def add_old_url(url):
    if url is None:
        return
    old_urls.add(url)


def add_new_urls(urls):
    if urls is None:
        return
    for url in urls:
        add_new_url(url)


def has_new_url():
    return len(new_urls)


def get_new_url():
    url = new_urls.pop()
    add_old_url(url)
    return url

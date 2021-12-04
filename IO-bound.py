import concurrent
import concurrent
import concurrent.futures
from urllib.request import Request, urlopen
from urllib.parse import unquote

import requests as requests


def get_link_code(link):
    try:
        request = Request(
            link,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        return code
        resp.close()
    except Exception as e:
        return (link, e)


links = open('res.txt', encoding='utf8').read().split('\n')

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    futures = []
    for url in links:
        futures.append(
            executor.submit(
                get_link_code, link=url
            )
        )
    for future in concurrent.futures.as_completed(futures):
        try:
            print(future.result())
        except requests.ConnectTimeout:
            print("ConnectTimeout.")

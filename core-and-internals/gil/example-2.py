# GIL does not hurt I/O tasks


import threading
import time
import urllib.request


def fetch_url(url):
    urllib.request.urlopen(url)
    print(f"Done: {url}")


urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
]

start = time.time()
for url in urls:
    fetch_url(url)
print(f"Sequential: {time.time() - start:.2f}s")


start = time.time()
threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Threaded: {time.time()-start:.2f}s")

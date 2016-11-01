import threading
import queue
import urllib.request

def read_website(url, queue):
    data = urllib.request.urlopen(url).read()
    queue.put(data)

def fetch_website(websites):
    this_queue = queue.Queue()
    threads = [threading.Thread(target=read_website, args=(webaddr,this_queue)) for webaddr in websites]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return this_queue

f=fetch_website(["http://freegeoip.net/json/"])
e=f.get()
print (e)

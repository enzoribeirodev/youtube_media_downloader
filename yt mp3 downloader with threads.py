import os
import queue
from pytube import YouTube
import threading


def download_mp3(q):
    while not q.empty():
        yt = YouTube(q.get())
        stream = yt.streams.get_audio_only()
        d = stream.download()
        base, extension=os.path.splitext(d)
        new_file_name=base + '.mp3'
        os.rename(d, new_file_name)


q = queue.Queue()
urls = []
threads_list = []

while True:
    url = input('URL [type a whitespace to end loop]: ').strip()
    if url == '':
        break
    urls.append(url)
    q.put(url)


if not os.path.exists('yt mp3 downloader folder'):
    os.mkdir('yt mp3 downloader folder')

os.chdir('yt mp3 downloader folder')


for i in range(1, 6):
    t = threading.Thread(target = download_mp3, args = (q, ))
    t.start()
    threads_list.append(t)

for thread in threads_list:
    thread.join()

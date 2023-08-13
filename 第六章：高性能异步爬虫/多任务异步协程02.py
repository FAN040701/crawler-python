import requests
import asyncio
import time

start = time.time()
urls = ['http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom']

async def get_page(url):
    print('正在下载：', url)
    response = requests.get(url)
    #这里使用requests模块发送请求，是同步阻塞的,异步会中断


    print('下载完毕：', response.text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('总耗时：', round(end-start, 1))

import requests
import time
import asyncio
from lxml import etree

async def requests(url):
    print('正在请求的url是：',url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    #time.sleep(2)

    #当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'}
start = time.time()
urls = ['https://www.baidu.com/s?wd=ip','https://www.sogou.com/s?wd=ip','https://www.doubanjiang.com/s?wd=ip']
#创建一个任务对象列表
tasks = []
for url in urls:
    c = requests(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
#不能够使用for循环遍历tasks列表，因为for循环遍历的是协程对象，而不是任务对象
#需要将任务列表封装到wait中
#不能用sleep，因为sleep是同步阻塞的，而asyncio.sleep是异步非阻塞的
print(round(time.time()-start, 2))

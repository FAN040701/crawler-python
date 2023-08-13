import requests
from lxml import etree
import re
import time
from multiprocessing.dummy import Pool
import os
#需求：爬取梨视频的视频数据
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
               'Referrer Policy':
'strict-origin-when-cross-origin'}
#原则：线程池处理的是阻塞且较为耗时的操作

#对下述url发起请求解析出视频详情页的url和视频名称
url = 'https://www.pearvideo.com/category_1'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []#存储所有视频的链接
for li in li_list:
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    #print(detail_url,name)
    #对详情页的url发起请求
    detail_page = requests.get(url=detail_url,headers = headers).text
    json = requests.get(url='https://www.pearvideo.com/videoStatus.jsp?contId='+detail_url.split('_')[-1]+'&mrd='+str(int(time.time()*1000)),headers=headers).json()
    #从详情页中解析出视频的地址
    #print(json)
    ex = 'srcUrl="(.*?)"'
    video_url = re.findall(ex,detail_page)[0]
    #print(video_url)
    dict = {
        'name':name,
        'url':video_url
    }
    urls.append(dict)

def get_video_data(dic):
    url = dic['url']
    name = dic['name']
    print(name,'正在下载......')
    data = requests.get(url=url,headers=headers).content
    #持久化存储
    if not os.path.exists('./video'):
        os.mkdir('./video')
    with open('./video/'+name,'wb') as fp:
        fp.write(data)
        print(name,'下载成功！！！')


#实例化一个线程池对象
pool = Pool(4)
#map(func,iterable)：将可迭代对象中的每一个元素传递给func进行处理
start_time = time.time() 
pool.map(get_video_data,urls)
end_time = time.time()

pool.close()
#pool.close()和pool.join()的作用是为了让主线程等待子线程结束之后再结束
pool.join()
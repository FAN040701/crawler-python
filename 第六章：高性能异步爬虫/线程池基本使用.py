import time

#使用单线程串行方式执行

'''def get_page(str):
    print('正在下载：',str)
    time.sleep(2)
    print('下载成功：',str)

name_list = ['xiaozi','aa','bb','cc']

start_time = time.time()

for i in range(len(name_list)):
    get_page(name_list[i])

end_time = time.time()
print('%d second'%(end_time-start_time))
#一共花费了8秒钟'''

#使用线程池方式执行
from multiprocessing.dummy import Pool
start_time = time.time()
def get_page(str):
    print('正在下载：',str)
    time.sleep(2)
    print('下载成功：',str)

name_list = ['xiaozi','aa','bb','cc']

#实例化一个线程池对象
pool = Pool(4)
#将列表中每一个列表元素传递给get_page进行处理
pool.map(get_page, name_list)

end_time = time.time()
print('%d second'%(end_time-start_time))
#一共花费了2秒钟

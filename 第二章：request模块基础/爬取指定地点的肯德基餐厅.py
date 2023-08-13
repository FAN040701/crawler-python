import requests

if __name__ == '__main__':
    #1.指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    #UA伪装防止网站反爬
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    
    #用户输入一个城市
    city = input("enter a city name: ")

    #post请求参数处理（同get请求一致）
    param = {'cname': '',
             'pid': '',
             'keyword': city,
             'pageIndex': '1',}
    
    #2.对指定的url发起请求
    response = requests.post(url=url, data=param, headers=headers)

    #3.获取响应数据
    page_text = response.text

    #4.持久化存储
    filename = city + '.txt'

    fp = open(filename, 'w', encoding='utf-8')
    fp.write(page_text)

    #提取所有的页码中的信息

    all_results = []  # 存储所有索引的结果
    pageIndex = 2  # 开始的索引值

    while True:
        param['pageIndex'] = str(pageIndex)
        response = requests.post(url=url, data=param, headers=headers)
        page_text = response.text
        
        if "storeName" not in page_text :
            break  # 如果返回结果为空，则结束循环
        
        all_results.append(page_text)
        pageIndex += 1

    with open(filename, 'a', encoding='utf-8') as fp:
        for result in all_results:
            fp.write(result)
    fp.close() #关闭文件

    #对数据进行清洗
    with open(filename, 'r', encoding='utf-8') as fp2:
        content = fp2.read()
        lines = content.split(',')
    
    with open(filename, 'w', encoding='utf-8') as fp3:
        num = 1
        for line in lines:
            if 'storeName' in line or 'addressDetail' in line:

                #让它变得好看一点
                line = line.replace('storeName', str(num) +' 店名')
                if num <= 10:
                    line = line.replace('addressDetail', '  具体地址')
                elif num <= 100:
                    line = line.replace('addressDetail', '   具体地址')
                else:
                    line = line.replace('addressDetail', '    具体地址')
                line = line.replace('"', '')  # 删除双引号
                line = line.replace(':', '：')  # 替换冒号

                #写入文件
                fp3.write(line + '\n')
                
                if '店名' in line:
                    num += 1

    print(filename, '保存成功！！！')

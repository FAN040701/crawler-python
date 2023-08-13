import requests
import json
#这个程序现在无法正常运行，原因大概是网站新增了更高级的反爬机制，需要更高级的反爬技术

if __name__ == '__main__':
    
    #指定url
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []
    all_data_list = []#存储所有企业详情数据

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    #参数的封装
    for page in range(1,6): #爬取前5页的数据
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
            '7QBHXKaZ': '0XslELqlqEhiOSvLA2HZxW4FZ5kXRbK.F5m_7Tj1mCAb967tYCUMhWmd0dVgvTgwbGie0PLGFgqMoiZaYrR0Gmu5vSR0xA7FDw.3jv3IRjV0F79fjnw7ija'
        }
        #合并了第二步和第三步
        json_ids = requests.post(url=url,headers=headers,data = data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    
    #print(id_list)

    #获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=post_url,headers=headers,data=data).json()
        #print(detail_json, end='\n')
        all_data_list.append(detail_json)
    #持久化存储
    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!!!')


    """#持久化存储
    with open('./化妆品.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    fp.close()
    #此时化妆品.html中的内容是乱码，因为网页的编码方式是gbk，而我们用的是utf-8

    我们想要的数据是动态加载出来的
    通过原本的url无法直接获取到我们想要的数据，因为数据是通过ajax请求得到的"""
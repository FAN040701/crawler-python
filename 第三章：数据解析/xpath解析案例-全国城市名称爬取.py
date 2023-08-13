#需求：解析出所有城市名称 https://www.aqistudy.cn/historydata/
import requests
from lxml import etree
if __name__ == "__main__":
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)

    """host_li_list = tree.xpath('//div[@class="bottom"]/ul/li/a/text()')
    all_city_names = []
    # 解析到热门城市的名称
    for li in host_li_list:
        city_names = li.strip()
        all_city_names.append(city_names)
    #print(all_city_names)

    # 解析到全部城市的名称
    city_name_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in city_name_list:
        city_names = li.xpath('./a/text()')[0].strip()
        all_city_names.append(city_names)

    print(all_city_names, len(all_city_names))"""

    #解析到热门城市和全部城市对应的a标签
    #热门城市层级关系 //div[@class="bottom"]/ul/li/a
    #全部城市层级关系 //div[@class="bottom"]/ul/div[2]/li/a
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    #|表示或者
    all_city_names = []
    for a in a_list:
        city_names = a.xpath('./text()')[0]
        all_city_names.append(city_names)
    print(all_city_names, len(all_city_names))
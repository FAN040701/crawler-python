#需求：爬取三国演义小说中所有的章节标题和章节内容
#https://www.shicimingju.com/book/sanguoyanyi.html
import requests
import bs4
if __name__ == "__main__":
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    
    #对首页的页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).content

    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = bs4.BeautifulSoup(page_text, 'lxml')
    #2.解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo,txt', 'w', encoding='utf-8')
    for li in li_list:
        li_title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        #对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).content
        #解析出详情页中相关的章节内容
        detail_soup = bs4.BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_ = 'chapter_content')
        #解析到了章节的内容
        content = div_tag.text

        fp.write(li_title+': '+content+'\n')
        print(li_title, '爬取成功！！！')

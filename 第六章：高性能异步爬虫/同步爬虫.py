import requests
urls = ['https://www.scifac.hku.hk/',
        'https://saasweb.hku.hk/programme/stat.php',
        'https://webapp.science.hku.hk/sr4/servlet/enquiry']

def get_contetn(url):
    print('正在爬取：', url)
    try:
        #get方法是一个阻塞的方法，会等待服务器响应之后才会执行下一行代码
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(e)
        return None
    
def parese_content(content):
    print('响应数据的长度为：', len(content))

for url in urls:
    content = get_contetn(url)
    parese_content(content)
#单线程爬虫的缺点：1.效率低下 2.容易被封IP
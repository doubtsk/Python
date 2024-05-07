import re
import urllib.request


def GetHtmlCode(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    url = urllib.request.Request(url, headers=header)

    page = urllib.request.urlopen(url).read()
    page = page.decode('UTF-8')
    return page


def getPic(page):
    imgList = re.findall(r'(https:[^\s]*?(jpg))', page)
    x = 0
    for imageUrl in imgList:
        try:
            print('正在下载:%s'%imageUrl[0])
            image_save_path='./image/%d.png'%x
            urllib.request.urlretrieve(imageUrl[0],image_save_path)
            x=x+1
        except:
            continue
        pass

if __name__=='__main__':
    url="https://movie.douban.com/"
    page=GetHtmlCode(url)
    getPic(page)            
    
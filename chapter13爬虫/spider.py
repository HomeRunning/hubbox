"""
小型爬虫demo
爬虫框架:BeautifulSoup,Scrapy
爬虫,反爬虫,反反爬虫
封IP 代理Ip库
"""
import re
from urllib import request
from io import BytesIO
import gzip
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#<div class="DyListCover-info"><span class="DyListCover-hot"><svg class="DyListCover-hotIcon"><use xlink:href="#icon-hot_8a57f0b"></use></svg>110.8万</span><h2 class="DyListCover-user"><svg class="DyListCover-userIcon"><use xlink:href="#icon-user_c95acf8"></use></svg>王纪超666</h2></div>
class Spider():
    url = 'https://www.douyu.com/g_LOL'
    root_pattern = '<div class="DyListCover-info">([\s\S]*?)</div>'
    name_pattern = 'cf8"></use></svg>([\s\S]*?)</h2>'
    number_pattern = '</use></svg>([\s\S]*?)</span><h2'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')
        #htmls = str(htmls, encoding='utf-8')
        return htmls
        
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name, 'number':number}
            if anchor['name'] != []:
                anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        l = lambda anchor : {'name':anchor['name'][0].strip(),
                'number':anchor['number'][0]}
        return map(l,anchors)
        
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed,reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('\d*',anchor['number'])
        number = float(r[0])
        if '万' in  anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for anchor in anchors:
            print(anchor['name']+'------'+anchor['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)
        

spider = Spider()
spider.go()
    
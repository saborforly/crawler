import scrapy
import re

class StocksSpider(scrapy.Spider):
    name='stocks'
    start_url=['https://quote.eastmoney.com/stocklist.html']
    
    def parse(self, response):  #用于处理相应，解析内容形成字典，发现新的url请求
        #response是start_url网页的内容
        #css是国际公认的标签提取方法
        for href in response.css('a::attr(href)').extract(): #提取a标签属性是href的所有链接
            try:
                stock=re.findall(r'[s][hz]\d{6}',href)[0]    #获取股票的ID
                url='https://guopiao.baidu.com/stock/'+stock+'.html'  #使用百度股票，获取股票的链接信息
                self.log("url: %s"%url)
                yield scrapy.Request(url,callback=self.parse_stock)   #处理url响应的处理函数
            except:
                continue
    
    def parse_stock():
        #<div class='stock-bets'>
        #  <a class=bets-name'>启明股票
        #  <dt>成交量</dt><dd>100</dd>
        
        infoDict={}
        stockInfo = response.css('.stcok-bets')
        name=stockInfo.css('.bets-name').extract()[0]
        keyList=stockInfo.css('dt').extract()
        valueList=stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key=re.findall(r'>.*</dt>',keyList[i])[0][1:-5]
            try:
                val=re.findall(r'\d+\.?.*</dd>',valueList)[0][0:-5]
            except:
                val='--'
            infoDict[key]=val
        yield infoDict
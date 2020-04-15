import scrapy
import re

class StocksSpider(scrapy.Spider):
    name='stocks'
    start_url=['https://quote.eastmoney.com/stocklist.html']
    
    def parse(self, response):  #���ڴ�����Ӧ�����������γ��ֵ䣬�����µ�url����
        #response��start_url��ҳ������
        #css�ǹ��ʹ��ϵı�ǩ��ȡ����
        for href in response.css('a::attr(href)').extract(): #��ȡa��ǩ������href����������
            try:
                stock=re.findall(r'[s][hz]\d{6}',href)[0]    #��ȡ��Ʊ��ID
                url='https://guopiao.baidu.com/stock/'+stock+'.html'  #ʹ�ðٶȹ�Ʊ����ȡ��Ʊ��������Ϣ
                self.log("url: %s"%url)
                yield scrapy.Request(url,callback=self.parse_stock)   #����url��Ӧ�Ĵ�����
            except:
                continue
    
    def parse_stock():
        #<div class='stock-bets'>
        #  <a class=bets-name'>������Ʊ
        #  <dt>�ɽ���</dt><dd>100</dd>
        
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
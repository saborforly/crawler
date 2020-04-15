#处理解析后的数据（stocks.py中字典infoDict），并将数据存储到文件中
#需要在setting中配置s
class BaidustocksInfoPipline(object):
    def open_spider(self,spider):
        self.f=open('BaiduStockInfo.txt','w')
        
    def close_spider(self,spider):
        self.f.close()
    #item就是stocks中的字典数据
    def process_item(self,item,spider):
        try:
            line=str(dict(item))+'\n'
            self.f.write(line)
        except:
            pass
        return item
            
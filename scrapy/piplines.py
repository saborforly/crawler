#�������������ݣ�stocks.py���ֵ�infoDict�����������ݴ洢���ļ���
#��Ҫ��setting������s
class BaidustocksInfoPipline(object):
    def open_spider(self,spider):
        self.f=open('BaiduStockInfo.txt','w')
        
    def close_spider(self,spider):
        self.f.close()
    #item����stocks�е��ֵ�����
    def process_item(self,item,spider):
        try:
            line=str(dict(item))+'\n'
            self.f.write(line)
        except:
            pass
        return item
            
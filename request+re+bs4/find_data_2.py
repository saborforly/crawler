#coding=utf-8
import get_html_1
#soup 缩小范围  re 挑选数据

def find_html_soup(url_txt):
    from bs4 import BeautifulSoup
    ulist=[]
    #<tbody class="hidden_zhpm" style="text-align: center;">
    #   <tr class="alt">
    #	    <td>1</td>
    #       <td><div align="left">清华大学</div></td>
    #	    <td>北京</td>
    #       <td>94.6</td>
    #       <td class="hidden-xs need-hidden indicator5">100.0</td>
    #       ''''''
    #   </tr>
    import bs4
    soup=BeautifulSoup(url_txt,"html.parser")
    for tr in soup.find('tbody').children:  #获取tbody标签中的所有tr标签
        if isinstance(tr,bs4.element.Tag): #过滤非标签
            tds=tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])
    print("{0:^10}\t{1:{3}^10}\t{2:^10}".format('大学排名', '学校名称', '总分',chr(12288)))
    #chr(12288)用于字符填充
    for i in range(5):
        u=ulist[i]
        print("{0:^10}\t{1:{3}^10}\t{2:^10}".format(u[0], u[1], u[2],chr(12288)))
#url_txt=get_html_1.Down_html("http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html")
#find_html_soup(url_txt)

def find_html_re(url_txt):
    import re,os
    ulist=[]
    #匹配这一段内容,这段内容
    #可以从浏览器检查图片数据中获取，去掉class
    #<a href="https://static.vmgirls.com/image/2019/12/2019122210292813-scaled.jpeg" alt="少女情怀总是诗" title="少女情怀总是诗" class="nc-light-gallery-item">
    try:
        dir_name=re.findall('<h1 class="post-title h3">(.*?)</h1>',url_txt)[-1]
        plt=re.findall('<a href="(.*)" alt=".*" title=".*">',url_txt)
        
        print(plt)
        if not dir_name:
            print("无法抓取目录信息")
            exit(0)
        if not os.path.exists(dir_name):
            print(dir_name)
            os.mkdir(dir_name)
        for i in plt:
            print(i)
            get_html_1.Down_picture(dir_name,i)
    except:
        print("")
#url_txt=get_html_1.Down_html("https://www.vmgirls.com/13344.html")
#find_html_re(url_txt)

def find_html_soup_re(url_txt):
    #<div class='stock-bets'>
    #  <a class=bets-name'>启明股票
    #  <dt>成交量</dt><dd>100</dd>
    
    from bs4 import BeautifulSoup
    infoDict={}
    lst=[]
    soup=BeautifulSoup(url_txt,"html.parser")
    #根据标签属性挑选数据
    stockInfo=soup.find('div',attrs={'class':'stock-bets'})
    name=stockInfo.find_all(attrs={'class':'bets-name'})[0]
    infoDict.update({'股票名称':name.text.split()[0]})
    keyList=stockInfo.find_all('dt')
    valueList=stockInfo.find_all('dd')
    for i in range(keyList):
        key=keyList[i].text
        val=valueList[i].text
        infoDict[key]=val
    with open('股票.txt','wb',encoding="utf-8") as f:
        f.write(str(infoDict)+"/n")    
#coding=utf-8
import requests
import json

#根据关键字获取网页信息
def Down_html(url):
    #user-agent 从网页检查network中的13344.html可以找到
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        #print(r.text)
        return r.text
    except:
        return ""
    #查看url r.request.url
#Down_html("https://www.vmgirls.com/13344.html")

#获取json网页
def Down_json(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
    }
    #向浏览器的请求头 r.request.headers
    r = requests.get(url, headers)
    #状态码 r.status_code  
    #print(r.text)   #{'data': '{"lastUpdateTime":"2020-04-14 12:48:50","chinaTotal"'''
    
    res = json.loads(r.text)
    #{'data': '{"lastUpdateTime":"2020-04-14 12:48:50","chinaTotal"'''
    data_res = json.loads(res['data'])
    return data_res
Down_json('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5')

#下载图片数据等信息    
def Down_picture(dir_name,url):
    import random,string
    s3=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10) )
    path=s3+'.'+url.split('.')[-1]
    r = requests.get(url)
    with open(dir_name+'/'+path,'wb') as f:
        f.write(r.content)
    f.close()
#Down_picture('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1581523148093&di=a180baf2012597623ba0f937393e6a1e&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20181020%2F463cdf517bce41b7b5d5023be76b5b65.jpeg')

#查看ip地址位置
def ip_from():
    url='http://m.ip138.com/ip.asp?ip='
    try:
        r=request.get(url+'202.204.80.112')
        print(r.text[-500:])
    except:
        print('error')

def Parse_data1():
    data = Down_json('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5')
    list = ['截至时间：'+str(data['lastUpdateTime'])+'\n'
          '全国确诊人数：'+str(data['chinaTotal']['confirm'])+'\n'
          '今日新增确诊：'+str(data['chinaAdd']['confirm'])+'\n'
          '全国疑似：'+str(data['chinaTotal']['suspect'])+'\n'
          '今日新增疑似：'+str(data['chinaAdd']['suspect'])+'\n'
          '全国治愈：'+str(data['chinaTotal']['heal'])+'\n'
          '今日新增治愈：'+str(data['chinaAdd']['heal'])+'\n'
          '全国死亡：'+str(data['chinaTotal']['dead'])+'\n'
          '今日新增死亡：'+str(data['chinaAdd']['dead'])+'\n']
    result = ''.join(list)
    print(result)
    with open('疫情查询.txt', 'wt', encoding="utf-8") as f:
        f.write(result + '\n')
 

#Down_data()
#Parse_data1()
#Parse_data2()

import urllib.request as r
import urllib.parse as p
import json
import time

while True:
    content = input('请输入需要翻译的内容：(按"q"退出程序)')
    if content == 'q':
        break
    #首先打开审查元素,调到Network
    #找到method中的post
    #点击打开Headers

    #General栏中的Request URL,复制过来
    url = r'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    '''
    #隐藏自己方法一，使自己访问时认为是普通访问
    head = {}
    head['User-Agent'] = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    '''
    #From Data栏中的所有的复制过来，变为字符串型
    data = {'i':content,    #这行是要翻译的内容，可以进行调整
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1522508710787',
    'sign':'f04a925eebc8ba4727ba86a383cd5677',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'false'}

    #encode编码，将自然语言转换成计算机语言
    data = p.urlencode(data).encode('utf-8') #utf-8是默认值
    req = r.Request(url, data) #1号

    #隐藏自己方法二，使自己访问时认为是普通访问
    req.add_header('header', r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response = r.urlopen(req)#2号
    #1号和2号可合为 response = r.urlopen(url)

    #decode解码，将计算机语言转换成自然语言
    html = response.read().decode('utf-8')

    target = json.loads(html)

    print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']))
    #休眠5秒，防止访问过于频繁
    time.sleep(5)

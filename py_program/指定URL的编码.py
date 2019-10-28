import urllib.request as r
import chardet

def main():
    url = input('请输入URL：')
    response = r.urlopen(url)
    html = response.read()

    #识别网页编码
    encode = chardet.detect(html)['encoding']
    if encode == 'GB2312':
        encode = 'GBK'

    print('该网页的编码是：%s' % encode)
if __name__ == "__main__":
        main()

#coding:utf-8
import re
import requests
import time
import random
import urllib2

class Downloader(object):
    def __init__(self):
        self.header={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                     "Accept-Encoding":"gzip, deflate, br",
                     "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                     "Cache-Control":"max-age=0",
                     "Connection":"keep-alive",
                     "Host":"www.zhihu.com",
                     "If-Modified-Since":"Sun, 31 Jul 2016 02:45:05 GMT",
                     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
                     }
        self.headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                       "Accept-Encoding": "gzip, deflate, br",
                       "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                       "Cache-Control": "max-age=0",
                       "Connection": "keep-alive",
                       "Host": "www.zhihu.com",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
                       }
        self.downloader = requests.session()
        self.timeout = random.randint(5, 20)
        self.data = {"_xsrf": "",
                     #"captcha": "",
                     "email": "2530199385@qq.com",
                     "password": "xxxxxxx",
                     "remember_me": "true"}

    # 获取_xrsf验证
    def get_xsrf(self,page):
        pattern = re.compile('<input.*?type="hidden".*?name="_xsrf".*?value="(.*?)"/>')
        items = re.findall(pattern, page)
        xsrf = ''
        for item in items:
            xsrf = item
        return xsrf

    # 获取验证码
    def get_captcha(self):
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + str(int(time.time() * 1000))
        print captcha_url
        data = requests.get(captcha_url,self.headers).content
        f = file('captcha.gif', 'wb')
        f.write(data)
        f.close()
        captcha = raw_input('captcha is:')
        print captcha
        return captcha

    # 登录
    def login(self):
        index_page = self.downloader.get("https://www.zhihu.com").text
        self.data["_xsrf"] = self.get_xsrf(index_page)
        #self.data["captcha"] = self.get_captcha()
        self.downloader.post('https://www.zhihu.com/login/email', data=self.data, headers=self.header)

    # 下载新页面
    def download(self, new_url):
        try:
            print "crawing:" + new_url
            html_content = self.downloader.get(new_url, headers=self.header, timeout=self.timeout).text
            return html_content
        except:
            time.sleep(10)

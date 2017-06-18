#coding:utf-8
import outputer

class UrlManager():
    def __init__(self):
        self.out_put = outputer.Outputer()

    # 从新表中弹出一个未访问的链接
    def get_new_url(self):
        new_url =self.out_put.pop_new_url()
        if new_url is None:
            return
        else:
            return new_url

    # 新增一个未访问过链接
    def add_new_url(self, url):
        if url is None:
            return
        if not self.out_put.isSaved(url) and not self.out_put.isCrawed(url):
            self.out_put.add_new_url(url)

    # 判断是否还有未访问的链接
    def has_new_url(self):
        if self.out_put.has_new_url():
            return True

    # 增加一个未访问过的链接列表
    def add_new_urls(self, urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)


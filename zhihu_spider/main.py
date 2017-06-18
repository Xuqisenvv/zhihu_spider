#coding:utf-8
import url_manager
import page_downloader
import html_parser
import outputer
import time
import threading

class zhihu():
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = page_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.outputers = outputer.Outputer()

    def every_craw(self):
        new_url = self.urls.get_new_url()
        follow_list = self.downloader.download(new_url + "/followees")
        #print follow_list


        # 爬取页面中所有用户链接
        #good_new_urls = self.parser.get_good_new_urls(user_content)
        #followees = self.parser.get_follow_url(follow_list)
        # 获取用户的基本数据（昵称，签名，兴趣,性别，头像地址，职业经历，居住地信息，教育经历,提问数，回答数，关注数，粉丝数，关注的话题）
        base_data = self.parser.get_base_data(follow_list)
        base_data['id'] = new_url.split('/', 4)[4]

        # 处理数据
        #self.urls.add_new_urls(followees)
        self.outputers.save(base_data)

    def run(self):
        self.downloader.login()
        while self.urls.has_new_url():
            time1 = time.time()
            try:
               self.every_craw()
            except Exception as e:
                print "craw failed"
                print e
            time2 = time.time()
            print "用时：",time2 - time1
        self.outputers.close()

if __name__=="__main__":

    spider = zhihu()
    spider.run()




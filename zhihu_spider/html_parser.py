#coding:utf-8
from bs4 import BeautifulSoup


class Parser(object):


    def get_base_data(self,html_content):
        # 解析网页内容
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        base_data = {}
        base_data['nickname'] = soup.find('div', class_="title-section").a.get_text().encode('utf-8')
        base_data['picture_url'] = soup.find('img', class_="Avatar Avatar--l").get('src').encode('utf-8')
        if soup.find('span', class_="content") is not None:
            base_data['signature'] =soup.find('span', class_="content").get_text().encode('utf-8')
        else:
            base_data['signature'] = None
        # 性别
        if soup.find('span', class_="item gender") is not None:
             base_data['sex'] = soup.find('span', class_="item gender").i.get('class')[1].encode('utf-8')
        else:
            base_data['sex'] = None
        # 兴趣
        if soup.find('div', class_="title-section").find('div', class_="bio ellipsis") is  None:
            base_data['interest'] = None
        else:
            base_data['interest'] = soup.find('div', class_="title-section").find('div',class_="bio ellipsis").get_text().encode('utf-8')
        # 工作
        if soup.find('span', class_="position item") is not None:
             if soup.find('span', class_="position item").find('a') is not None:
                 base_data['job'] = soup.find('span', class_="position item").find('a').get_text().encode('utf-8')
             else:
                 base_data['job'] = soup.find('span', class_="position item").get_text().encode('utf-8')
        else:
            base_data['job']=None
        # 居住地
        if soup.find('span', class_="location item") is not None:
            if soup.find('span', class_="location item").find('a') is not None:
              base_data['living_place'] = soup.find('span', class_="location item").find('a').get_text().encode('utf-8')
            else:
              base_data['living_place'] = soup.find('span', class_="location item").get_text().encode('utf-8')
        else:
            base_data['living_place']=None
        # 所在领域
        if soup.find('span', class_="business item") is not None:
            if soup.find('span', class_="business item").a is not None:
                base_data['field'] = soup.find('span', class_="business item").a.get_text().encode('utf-8')
            else:
                base_data['field'] = soup.find('span', class_="business item").get_text().encode('utf-8')
        else:
            base_data['field'] = None
        # 教育
        if soup.find('span', class_="education item") is not None:
            if soup.find('span', class_="education item").a is not None:
                base_data['education'] = soup.find('span', class_="education item").a.get_text().encode('utf-8')
            else:
                base_data['education'] = soup.find('span', class_="education item").get_text().encode('utf-8')
        else:
            base_data['education'] = None

        data1 = soup.find_all('a', class_="item ")
        base_data['question'] = int(data1[0].span.get_text().encode('utf-8'))
        base_data['answers'] = int(data1[1].span.get_text().encode('utf-8'))

        base_data['zan'] = int(soup.find('span', class_="zm-profile-header-user-agree").find('strong').string.encode('utf-8)'))
        base_data['thanks'] = int(soup.find('span', class_="zm-profile-header-user-thanks").find('strong').string.encode('utf-8'))
        # 关注情况
        data2 = soup.find('div', class_="zm-profile-side-following zg-clear").find_all('a')
        base_data['followees'] = int(data2[0].strong.string.encode('utf-8'))
        base_data['fans'] = int(data2[1].strong.string.encode('utf-8'))
        # 话题
        base_data['topics']=""
        topics = soup.find_all('img', class_="Avatar Avatar--l")
        for topic in topics:
            base_data['topics'] = base_data['topics'] + topic.get('alt').encode('utf-8') + " "

        return base_data

    def get_good_new_urls(self, followees_list):
        soup = BeautifulSoup(followees_list, 'html.parser', from_encoding='utf-8')
        links2 = soup.find_all('a', class_="author-link")
        new_urls = set()
        for link in links2:
            url = link.get('href')
            new_urls.add(url)
        return new_urls

    def get_follow_url(self, follow_list):
        soup = BeautifulSoup(follow_list, 'html.parser', from_encoding='utf-8')
        links = soup.find_all('h2', class_="zm-list-content-title")
        new_urls = set()
        for link in links:
            url = link.a.get('href')
            new_urls.add(url)
        return new_urls



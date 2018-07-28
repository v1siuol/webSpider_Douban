# coding=utf-8
"""
豆瓣爬虫: 用beautifulsoup4库获取豆瓣排行榜上每部电影的有利于分析的数据细节再写入csv文件

更新2.2.1: some little fixes on the way to standard
XX: 魔法值 连数据库 异常判断
Introduction: This program is to output the information of each movie in the top ten latest movie charts to a csv file
** API由豆瓣提供: https://developers.douban.com/wiki/?title=movie_v2#subject

__author__ = v1siuol
__date__ = 2018-07-28
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import random
import re
import json
import time
import os
from webSpider_Douban.Movie import Movie


class Crawler:
    def __init__(self, info_option='1', output_option='1'):

        self.__movies = []  # avoid modifying
        self.__start_time = None  # avoid modifying
        self.file_path = None
        self.file_name = None
        self.set_info_option(info_option)
        self.set_output_option(output_option)

    def set_info_option(self, info_option='1'):
        # info_option:1 for short, 2 for details
        try:
            if info_option == '1' or info_option == '2':
                self.info_option = info_option
        except Exception as e:
            print('Catch in Crawler.py - def sef_info_option():', e)

    def set_output_option(self, output_option='1'):
        # output_option:1 for print, 2 for csv * developing 3 for sql
        try:
            if output_option == '1' or output_option == '2':
                self.output_option = output_option
        except Exception as e:
            print('Catch in Crawler.py - def set_output_option():', e)

    def set_file_path(self, file_path):
        # !!exception handler
        self.file_path = file_path

    def set_file_name(self, file_name):
        # !!exception handler
        self.file_name = file_name

    @staticmethod
    def run():
        # ask input?
        love.build()
        love.output(love.output_option)

    @staticmethod
    def help():
        print('Methods:')
        print('  .set_info_option((String)info_option)\t\t\t\t\t\t1 for only Chinese titles / 2 for details.')
        print('  .set_output_option((String)output_option)\t\t\t\t\t1 for printing in cmd '
              '(only support for Chinese titles now) / 2 for creating a new .csv file.')
        print(
            '  .set_file_path((String)file_path)\t\t\t\t\t\t\tdefault will automatically achieve path to desktop in Mac, '
            'in forms of \'/Users/your_name/Desktop\'.')
        print('  .set_file_name((String)file_name)\t\t\t\t\t\t\tdefault =\'lstMoviesAnaCharts.csv\', '
              'please follow the rules of file name.')
        print('  .build()\t\t\t\t\t\t\t\t\t\t\t\t\tFetching data.')
        print('  .output()\t\t\t\t\t\t\t\t\t\t\t\t\tDisplay results based on output setting.')
        print('  .run()\t\t\t\t\t\t\t\t\t\t\t\t\tAutomatically build and output.')
        print()

    def achieve_id(self):
        chart_url = 'https://movie.douban.com/chart'
        html = urlopen(chart_url)
        bs0bj = BeautifulSoup(html, 'lxml')
        lst_movies = bs0bj.find('div', {'class': 'indent'}).findAll('div', {'id': re.compile('collect_form_\d+')})
        lst_movies_id = [movie.attrs['id'][13:] for movie in lst_movies]
        return lst_movies_id

    def build(self):
        print('--Begin to fetch data------------------')
        print()
        # current_movie = Movie()
        self.__set_start_time()

        chart_url = 'https://movie.douban.com/chart'
        base_url = 'https://api.douban.com/v2/movie/subject/'
        counter = 0
        tempi = 1

        # 从豆瓣新片榜获取电影id / Retrieve movie_id from top ten latest movie charts
        html = urlopen(chart_url)
        # bs0bj = BeautifulSoup(html, 'html.parser')
        bs0bj = BeautifulSoup(html, 'lxml')
        lst_movies = bs0bj.find('div', {'class': 'indent'}).findAll('div', {'id': re.compile('collect_form_\d+')})
        lst_movies_id = [movie.attrs['id'][13:] for movie in lst_movies]

        for mId in lst_movies_id:
            # 接入api并解析json / Get data from api and deal with json
            response_json = json.loads(urlopen(base_url + mId).read().decode('utf-8'))  # {}
            # print(response_json)
            current_movie = Movie()

            current_movie.identity = response_json['id']  # 条目id
            current_movie.title = response_json['title']  # 中文名
            current_movie.originalTitle = response_json['original_title']  # 原名
            current_movie.rating = response_json['rating']  # 评分
            current_movie.aveRating = current_movie.rating['average']  # 平均评分
            current_movie.ratingsCount = response_json['ratings_count']  # 评分人数
            current_movie.wishCount = response_json['wish_count']  # 想看人数
            current_movie.collectCount = response_json['collect_count']  # 看过人数

            current_movie.directors = response_json['directors']  # 导演，数据结构为影人的简化描述
            current_movie.directorsName = ""  # 导演名字
            for director in current_movie.directors:
                current_movie.directorsName += director['name']
                if director != current_movie.directors[-1]:
                    current_movie.directorsName += ' / '

            current_movie.casts = response_json['casts']  # 主演，最多可获得4个，数据结构为影人的简化描述
            current_movie.castsName = ""  # 主演名字
            for cast in current_movie.casts:
                current_movie.castsName += cast['name']
                if cast != current_movie.casts[-1]:
                    current_movie.castsName += ' / '

            current_movie.year = response_json['year']  # 年代
            current_movie.genres = response_json['genres']  # 影片类型，最多提供3个
            current_movie.genresName = ""  # 影片类型名字
            for genre in current_movie.genres:
                current_movie.genresName += genre
                if genre != current_movie.genres[-1]:
                    current_movie.genresName += ' / '

            current_movie.countries = response_json['countries']  # 制片国家/地区
            current_movie.countriesName = ""  # 制片国家/地区名字
            for country in current_movie.countries:
                current_movie.countriesName += country
                if country != current_movie.countries[-1]:
                    current_movie.countriesName += ' / '

            current_movie.commentsCount = response_json['comments_count']  # 短评数量
            current_movie.reviewsCount = response_json['reviews_count']  # 影评数量

            self.__movies.append(current_movie)
            counter += 1
            # print('Finished %d/%d' % (counter, len(lst_movies_id)))

            if counter != tempi:
                print('', end='\r')

            if counter == len(lst_movies_id):
                print('|' + '██' * counter + '  ' * (10 - counter) + '|  %d%%' % (100 * counter // len(lst_movies_id)))
                print()
            else:
                print('|' + '██' * counter + '  ' * (10 - counter) + '|  %d%%' % (100 * counter // len(lst_movies_id)),
                      end='', flush=True)
                # 设置爬虫间隔2s(公开api接口: 40次请求/分钟) / Set the crawl span 2 seconds (public api: 40 requests per minute)
                time.sleep(1.5 + random.randint(1, 100) / 100)
            tempi = counter

        print('----------------------------Completed--')
        print('Time elapsed: %.6f(s)' % (time.time() - self.__start_time))

    def output(self, output_option):
        show_timeset = '%Y-%m-%d %X'

        print()

        if output_option == '1':
            print('+++++++++++++++++++++++++++++++++++++++')
            print('Updated time: ' + time.strftime(show_timeset, time.localtime(self.__start_time)))
            print('Top 10 latest movie chart: ')
            print('+++++++++++++++++++++++++++++++++++++++')
            for movie in self.__movies:
                print(movie.title)
            print('+++++++++++++++++++++++++++++++++++++++')

        elif output_option == '2':
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            self.file_path = desktop + '/'
            self.file_name = 'lstMoviesAnaCharts.csv'

            # !!exception handler
            # 打开或创建csv文件 / Open or create a csv file
            csv_file = open(self.file_path + self.file_name, 'w+')
            print('Files is created under %s%s' % (self.file_path, self.file_name))

            try:
                # 在csv文件创建表头 / Create the headings in csv file
                writer = csv.writer(csv_file)

                writer.writerow(['Updated time: ' + time.strftime(show_timeset, time.localtime(self.__start_time))])

                if self.info_option == '1':
                    writer.writerow(['中文名'])
                elif self.info_option == '2':
                    writer.writerow(('条目id', '中文名', '原名', '导演名字', '主演名字', '制片国家/地区', '影片类型', '平均评分',
                                     '年代', '评分人数', '想看人数', '看过人数', '短评数量', '影评数量'))

                # 把处理好的数据写入csv文件 / Write data into the csv file
                if self.info_option == '1':
                    for movie in self.__movies:
                        writer.writerow([movie.title])
                elif self.info_option == '2':
                    for movie in self.__movies:
                        writer.writerow(
                            (movie.identity, movie.title, movie.originalTitle, movie.directorsName,
                             movie.castsName, movie.countriesName, movie.genresName,
                             movie.aveRating, movie.year, movie.ratingsCount,
                             movie.wishCount, movie.collectCount, movie.commentsCount,
                             movie.reviewsCount))
            except Exception as e:
                print('Catch in Crawler.py - def output():', e)

            # 关闭csv文件 / Close csv file
            csv_file.close()

    def __set_start_time(self):
        # avoid access
        self.__start_time = time.time()


# -------------test case-----------------
if __name__ == '__main__':
    if True:
        love = Crawler(info_option='1', output_option='1')
        love.run()

"""
豆瓣爬虫V1:返回排行榜电影名字
V2:将会接入api提取json分析每部电影的细节
Introduction: This program is output the title-lists of top ten latest movie charts to a csv file
* May need to install package
__author__ = v1siuol
__date__ = 2017.2.27
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


def main():
    print("Begin----------------------------------")
    html = urlopen("https://movie.douban.com/chart")
    bs0bj = BeautifulSoup(html, "lxml")
    lstMovies = bs0bj.find("div", {"class": "indent"}).findAll("a", {"class": "nbg"})
    csvFile = open("./lstMoviesTitles.csv", "w+")
    try:
        writer = csv.writer(csvFile)
        writer.writerow(["豆瓣新片榜"])
        for i in lstMovies:
            writer.writerow([i['title']])
    finally:
        csvFile.close()
    print("------------------------------------End")

# -------------test case-----------------
if __name__ == "__main__":
    if False:
        main()

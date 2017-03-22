"""
豆瓣爬虫V2.1: 返回豆瓣排行榜上每部电影的数据细节(不再只是电影名!); 表头新增更新时间
V2.2: 将会对数据细节进行优化并加上适当注释 *将于两天内更新
V3: 将对数据进行细致处理并可视化 *更新日期待定
Introduction: This program is to output the information of each movie in the top ten latest movie charts to a csv file
** API由豆瓣提供: https://developers.douban.com/wiki/?title=movie_v2#subject
__author__ = v1siuol
__date__ = 2017.3.22
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re
import json
import time


def main():
    print("Begin----------------------------------")
    html = urlopen("https://movie.douban.com/chart")
    bs0bj = BeautifulSoup(html, "lxml")
    csvFile = open("./lstMoviesCharts.csv", "w+")
    lstMovies = bs0bj.find("div", {"class": "indent"}).findAll("div", {"id": re.compile("collect_form_\d+")})
    lstMoviesId = [i.attrs["id"][13:] for i in lstMovies]
    baseUrl = "https://api.douban.com/v2/movie/subject/"
    counter = 0
    showTimeSet = "%Y-%m-%d %X"

    try:
        writer = csv.writer(csvFile)
        writer.writerow(["Updated time: "+time.strftime(showTimeSet, time.localtime(time.time()))])
        writer.writerow(("条目id", "中文名", "原名", "又名", "条目页URL", "移动版条目页URL", "评分", "评分人数",
                         "想看人数", "看过人数","在看人数", "电影海报图", "条目分类", "导演", "主演", "豆瓣小站",
                         "年代", "影片类型", "制片国家/地区", "简介","短评数量", "影评数量", "总季数", "当前季数",
                         "当前季的集数", "影讯页URL", "分享链接"))
    except Exception as e:
        print("Exception:", e)
    for i in lstMoviesId:
        responseJson = json.loads(urlopen(baseUrl + i).read().decode("utf-8"))  # {}
        
        movieId = responseJson["id"]  # 条目id
        movieTitle = responseJson["title"]  # 中文名
        movieOriginalTitle = responseJson["original_title"]  # 原名
        movieAka = responseJson["aka"]  # 又名
        movieAlt = responseJson["alt"]  # 条目页URL
        movieMobileUrl = responseJson["mobile_url"]  # 移动版条目页URL
        movieRating = responseJson["rating"]  # 评分
        movieRatingsCount = responseJson["ratings_count"]  # 评分人数
        movieWishCount = responseJson["wish_count"]  # 想看人数
        movieCollectCount = responseJson["collect_count"]  # 看过人数
        movieDoCount = responseJson["do_count"]  # 在看人数，如果是电视剧，默认值为0，如果是电影值为null
        movieImages = responseJson["images"] # 电影海报图，分别提供288px x 465px(大)，96px x 155px(中) 64px x 103px(小)尺寸
        movieSubtype = responseJson["subtype"]  # 条目分类, movie或者tv
        movieDirectors = responseJson["directors"]  # 导演，数据结构为影人的简化描述
        movieCasts = responseJson["casts"]  # 主演，最多可获得4个，数据结构为影人的简化描述
        movieDoubanSite = responseJson["douban_site"]  # 豆瓣小站
        movieYear = responseJson["year"]  # 年代
        movieGenres = responseJson["genres"]  # 影片类型，最多提供3个
        movieCountries = responseJson["countries"]  # 制片国家/地区
        movieSummary = responseJson["summary"]  # 简介
        movieCommentsCount = responseJson["comments_count"]  # 短评数量
        movieReviewsCount = responseJson["reviews_count"]  # 影评数量
        movieSeasonsCount = responseJson["seasons_count"]  # 总季数(tv only)
        movieCurrentSeason = responseJson["current_season"]  # 当前季数(tv only)
        movieEpisodesCount = responseJson["episodes_count"]  # 当前季的集数(tv only)
        movieScheduleUrl = responseJson["schedule_url"]  # 影讯页URL(movie only)
        movieShareUrl = responseJson["share_url"]  # 分享链接 看起来像移动端链接??

        try:
            writer.writerow((movieId, movieTitle, movieOriginalTitle, movieAka, movieAlt, movieMobileUrl,
                             movieRating, movieRatingsCount, movieWishCount, movieCollectCount, movieDoCount, movieImages,
                             movieSubtype, movieDirectors, movieCasts, movieDoubanSite, movieYear, movieGenres,
                             movieCountries, movieSummary, movieCommentsCount, movieReviewsCount, movieSeasonsCount,
                             movieCurrentSeason, movieEpisodesCount, movieScheduleUrl, movieShareUrl))
            counter += 1
        except Exception as e:
            print("Exception:", e)

        print("Finished %d/%d" % (counter, len(lstMoviesId)))
        time.sleep(2)
    csvFile.close()
    print("------------------------------------End")

# -------------test case-----------------
if __name__ == "__main__":
    if False:
        main()

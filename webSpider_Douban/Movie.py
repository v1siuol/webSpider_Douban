# import os
# desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
# print(desktop)

class Movie:

    def __init__(self, identity, originalTitle, rating, aveRating, ratingsCount, wishCount, collectCout,
                 directors, directorsName, casts, castsName, year, genres, genresName, countries, countriesName,
                 commentsCount, reviewsCount):
        pass



    # movieId = responseJson["id"]  # 条目id
    # movieOriginalTitle = responseJson["original_title"]  # 原名
    # movieRating = responseJson["rating"]  # 评分
    # movieAveRating = movieRating["average"]  # 平均评分
    # movieRatingsCount = responseJson["ratings_count"]  # 评分人数
    # movieWishCount = responseJson["wish_count"]  # 想看人数
    # movieCollectCount = responseJson["collect_count"]  # 看过人数
    #
    # movieDirectors = responseJson["directors"]  # 导演，数据结构为影人的简化描述
    # movieDirectorsName = ""  # 导演名字
    # for director in movieDirectors:
    #     movieDirectorsName += director["name"]
    #     if director != movieDirectors[-1]:
    #         movieDirectorsName += " / "
    #
    # movieCasts = responseJson["casts"]  # 主演，最多可获得4个，数据结构为影人的简化描述
    # movieCastsName = ""  # 主演名字
    # for cast in movieCasts:
    #     movieCastsName += cast["name"]
    #     if cast != movieCasts[-1]:
    #         movieCastsName += " / "
    #
    # movieYear = responseJson["year"]  # 年代
    # movieGenres = responseJson["genres"]  # 影片类型，最多提供3个
    # movieGenresName = ""  # 影片类型名字
    # for genre in movieGenres:
    #     movieGenresName += genre
    #     if genre != movieGenres[-1]:
    #         movieGenresName += " / "
    #
    # movieCountries = responseJson["countries"]  # 制片国家/地区
    # movieCountriesName = ""  # 制片国家/地区名字
    # for country in movieCountries:
    #     movieCountriesName += country
    #     if country != movieCountries[-1]:
    #         movieCountriesName += " / "
    #
    # movieCommentsCount = responseJson["comments_count"]  # 短评数量
    # movieReviewsCount = responseJson["reviews_count"]  # 影评数量

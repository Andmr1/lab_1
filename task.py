from bs4 import BeautifulSoup
import requests
from time import sleep
import codecs
count_good = 0
count_bad = 0


def find_good(url_, pages, count_good_):
    for page in range(1, pages+1):
        print(page)
        url1 = url_ + f"/{page}/"
        delay_value = 30 + 2 * page
        sleep(delay_value)
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        film_name = soup.find("a", class_="breadcrumbs__link")
        sources = soup.findAll("div", class_="response good")
        for src in sources:
            rev = src.find("span", class_="_reachbanner_").text
            if count_good_ < 10:
                name = "000" + str(count_good_)
                file = codecs.open(u'' + "dataset/good/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_good_ += 1
            elif 10 <= count_good_ < 100:
                name = "00" + str(count_good_)
                file = codecs.open(u'' + "dataset/good/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_good_ += 1
            elif 100 <= count_good_ <= 999:
                name = "0" + str(count_good_)
                file = codecs.open(u'' + "dataset/good/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_good_ += 1
    return count_good_


def find_bad(url_, pages, count_bad_):
    for page in range(1, pages+1):
        print(page)
        url1 = url_ + f"/{page}/"
        delay_value = 30 + 2 * page
        sleep(delay_value)
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        film_name = soup.find("a", class_="breadcrumbs__link")
        sources = soup.findAll("div", class_="response bad")
        for src in sources:
            rev = src.find("span", class_="_reachbanner_").text
            if count_bad_ < 10:
                name = "000" + str(count_bad_)
                file = codecs.open(u'' + "dataset/bad/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_bad_ += 1
            elif 10 <= count_bad_ < 100:
                name = "00" + str(count_bad_)
                file = codecs.open(u'' + "dataset/bad/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_bad_ += 1
            elif 100 <= count_bad_ <= 999:
                name = "0" + str(count_bad_)
                file = codecs.open(u'' + "dataset/bad/" + name + ".txt", "w", "utf-8")
                file.write(film_name.text + "\n")
                file.write(rev)
                file.close()
                count_bad_ += 1
    return count_bad_


def find_bad_new(url_, pages, count_bad_):
    for page in range(1, pages+1):
        print(page)
        url1 = url_ + f"/{page}/"
        delay_value = 30 + 2 * page
        sleep(delay_value)
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        sources = soup.findAll("div", class_="response bad")
        for source in sources:
            film_name = source.find("p", class_="film").text
            rev = source.find("span", class_="_reachbanner_").text
            if count_bad_ < 10:
                name = "000" + str(count_bad_)
                file = codecs.open(u'' + "dataset/bad/" + name + ".txt", "w", "utf-8")
                file.write(film_name + "\n")
                file.write(rev)
                file.close()
                count_bad_ += 1
            elif 10 <= count_bad_ < 100:
                name = "00" + str(count_bad_)
                file = codecs.open(u'' + "dataset/bad/" + name + ".txt", "w", "utf-8")
                file.write(film_name + "\n")
                file.write(rev)
                file.close()
                count_bad_ += 1
            elif 100 <= count_bad_ <= 999:
                name = "0" + str(count_bad_)
                file = codecs.open(u'' + "dataset/bad/" + name + ".txt", "w", "utf-8")
                file.write(film_name + "\n")
                file.write(rev)
                file.close()
                count_bad_ += 1
    return count_bad_


count_good = find_good("https://www.kinopoisk.ru/film/448/reviews/ord/rating/status/good/perpage/25", 32, count_good)
count_good = find_good("https://www.kinopoisk.ru/film/258687/reviews/ord/rating/status/good/perpage/25", 32,
                       count_good)
count_bad = find_bad("https://www.kinopoisk.ru/film/623250/reviews/ord/date/status/bad/perpage/25", 4, count_bad)
count_bad = find_bad("https://www.kinopoisk.ru/film/278522/reviews/?status=bad&ord=date&rnd=1664127127&perpage=25", 4,
                     count_bad)
count_bad = find_bad("https://www.kinopoisk.ru/film/819101/reviews/ord/date/status/bad/perpage/25", 2, count_bad)
count_bad = find_bad("https://www.kinopoisk.ru/film/718222/reviews/ord/date/status/bad/perpage/25", 2, count_bad)
count_bad = find_bad("https://www.kinopoisk.ru/film/718223/reviews/ord/date/status/bad/perpage/25", 8, count_bad)
count_bad = find_bad("https://www.kinopoisk.ru/film/407636/reviews/ord/rating/status/bad/perpage/25", 3, count_bad)
count_bad = find_bad("https://www.kinopoisk.ru/film/277328/reviews/ord/rating/status/bad/perpage/25", 3, count_bad)
count_bad = find_bad("https://www.kinopoisk.ru/film/258687/reviews/?status=bad&ord=rating&rnd=1664126777&perpage=25",
                     4, count_bad)
count_bad = find_bad_new("https://www.kinopoisk.ru/reviews/type/comment/status/bad/period/month/perpage/25", 16,
                         count_bad)

from bs4 import BeautifulSoup
import requests
from time import sleep
import random
count_good = 0
count_bad = 0


def find_good(url_, pages, count_good_):
    for page in range(1, pages+1):
        print(page)
        url1 = url_ + f"/{page}/"
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        sleep(scaled_value)
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        film_name = soup.find("a", class_="breadcrumbs__link")
        revs = soup.findAll("span", class_="_reachbanner_")
        for rev in revs:
            if count_good_ < 10:
                name = "000" + str(count_good_)
            elif 10 < count_good_ < 100:
                name = "00" + str(count_good_)
            elif count_good_ > 100:
                name = "0" + str(count_good_)
            file = open(f"dataset/good/{name}.txt", "w", "utf-8")
            file.write(film_name.text + "\n")
            file.write(rev.text)
            file.close
            count_good_ += 1
    return count_good_


def find_bad(url_, pages, count_bad_):
    for page in range(1, pages+1):
        print(page)
        url1 = url_ + f"/{page}/"
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        sleep(scaled_value)
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        film_name = soup.find("a", class_="breadcrumbs__link")
        revs = soup.findAll("span", class_="_reachbanner_")
        for rev in revs:
            if count_bad_ < 10:
                name = "000" + str(count_bad_)
            elif 10 < count_bad_ < 100:
                name = "00" + str(count_bad_)
            elif count_bad_ > 100:
                name = "0" + str(count_bad_)
            file = open(f"dataset/good/{name}.txt", "w", "utf-8")
            file.write(film_name.text + "\n")
            file.write(rev.text)
            file.close
            count_bad_ += 1
    return count_bad_


count_good = find_good("https://www.kinopoisk.ru/film/448/reviews/ord/rating/status/good/perpage/200", 4, count_good)
count_good = find_good("https://www.kinopoisk.ru/film/258687/reviews/ord/rating/status/good/perpage/200", 4,
                       count_good)
count_bad = find_bad("https://www.kinopoisk.ru/film/623250/reviews/ord/date/status/bad/perpage/75", 1, count_bad)
count_bad = find_bad("https://www.kinopoisk.ru/film/278522/reviews/?status=bad&ord=date&rnd=1664127127&perpage=100/", 1,
                     count_bad)

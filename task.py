from bs4 import BeautifulSoup
import requests
from time import sleep
import random
count_good = 0
count_bad = 0
for page in range(1, 43):
    print(page)
    url = f"https://www.kinopoisk.ru/film/448/reviews/ord/rating/status/good/perpage/200/page/{page}/"
    r = requests.get(url)
    value = random.random()
    scaled_value = 1 + (value * (9 - 5))
    sleep(scaled_value)
    soup = BeautifulSoup(r.text, "lxml")
    revs = soup.findAll("span", class_="_reachbanner_")
    for rev in revs:
        if count_good < 10:
            name = "000"+str(count_good)
        elif 10 < count_good < 100:
            name = "00"+str(count_good)
        elif count_good > 100:
            name = "0"+str(count_good)
        file = open(f"dataset/good/{name}.txt", "w", "utf-8")
        file.write("Форрест Гамп\n")
        file.write(rev.text)
        file.close
        count_good += 1
for page in range(1, 4):
    print(page)
    url = f"https://www.kinopoisk.ru/film/258687/reviews/ord/rating/status/good/perpage/200/page/{page}/"
    r = requests.get(url)
    value = random.random()
    scaled_value = 1 + (value * (9 - 5))
    sleep(scaled_value)
    soup = BeautifulSoup(r.text, "lxml")
    revs = soup.findAll("span", class_="_reachbanner_")
    for rev in revs:
        if count_good < 10:
            name = "000" + str(count_good)
        elif 10 < count_good < 100:
            name = "00" + str(count_good)
        elif count_good > 100:
            name = "0" + str(count_good)
        file = open(f"dataset/good/{name}.txt", "w", "utf-8")
        if count_good < 999:
            file.write("Интерстеллар\n")
            file.write(rev.text)
        file.close
        count_good += 1

#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import xlwt
import os
import urllib3
import urllib
import re
from lxml import html

workbook = xlwt.Workbook()

sheet = workbook.add_sheet('PySheet1', cell_overwrite_ok=True)
sheet.write(0, 0, "Название")
sheet.write(0, 1, "Цена")
sheet.write(0, 2, "Описание")
sheet.write(0, 3, "старая цена")


# url = "https://store.nike.com/ru/ru_ru/?ipp=120/"
# page = requests.get(url)

f = open("/Users/kalugin/git_proj/mipt_tinkoff_hackathon_2019/data/sport/nike.com/Официальный магазин. Nike.com RU..html", "r")

page = f.read()

soup = BeautifulSoup(page, "lxml")
items = soup.find_all('div', {'class': 'grid-item fullSize'})
# print(len(items[0]))
# print(items[0].find_all('a', href=True)[0]['href'])

k = 1

for item in items:
    url = item.find_all('a', href=True)[0]['href']
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    try:
        name = soup.find('h1', {'id': 'pdp_product_title'}).text
        sheet.write(k, 0, name)

        prices = soup.find_all('div', {'data-test': 'product-price'})
        price = re.sub(r"[^\d+]", "", prices[0].text, flags=re.UNICODE)
        old_price = re.sub(r"[^\d+]", "", prices[1].text, flags=re.UNICODE)
        sheet.write(k, 1, price)
        sheet.write(k, 3, old_price)

        descr = soup.find('h2', {'data-test': 'product-sub-title'}).text
        sheet.write(k, 2, descr)

        # print(name, price, descr, old_price)
        k += 1
    except:
        print(url)
    if(k%10 == 0): print(k)
print(k)
workbook.save("nike.xls")
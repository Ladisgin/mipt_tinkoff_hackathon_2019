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

def get_value(s):
    s = re.sub(r"\.+$", "", s)
    s = re.sub(r",", ".", s)
    s = re.sub(r"[^\d+\.]", "", s)
    return s

workbook = xlwt.Workbook()

sheet = workbook.add_sheet('PySheet1', cell_overwrite_ok=True)
sheet.write(0, 0, "Название")
sheet.write(0, 1, "Описание")
sheet.write(0, 2, "Цена")
sheet.write(0, 3, "старая цена")
sheet.write(0, 4, "путь")


site = "https://sport-marafon.ru"
url = "https://sport-marafon.ru/catalog"
page = requests.get(url).text

# f = open("/Users/kalugin/git_proj/mipt_tinkoff_hackathon_2019/data/sport/nike.com/Официальный магазин. Nike.com RU..html", "r")
# page = f.read()

k = 1

soup = BeautifulSoup(page, "lxml")

categories = soup.find_all('div', {'class': 'activity-list__activity'})
for category in categories:
    t = category.find_all('a', {'class': 'activity-list__name'})
    if len(t):
        categoryName = t[0].text.strip()
        print(categoryName)
        subCategories = category.find_all('li', {'class': 'activity-list__item'})
        for subCategory in subCategories:
            subCategoryName = subCategory.text.strip()
            print("\t" + subCategoryName)
            nextUrl = site + subCategory.find_all('a', href=True)[0]['href']
            while nextUrl != "":
                url = nextUrl
                page = requests.get(url).text
                soup = BeautifulSoup(page, "lxml")
                items = soup.find_all('div', {'class': 'product-list__item'})

                t = soup.find_all('a', {'class': 'navigate__link navigate__link_arrow navigate__link_next'}, href=True)
                if len(t):
                    nextUrl = site + t[0]['href']
                    # nextUrl = ""
                else:
                    nextUrl = ""
                for item in items:
                    # url = site + item.find_all('a', {'class': 'product-list__name'},href=True)[0]['href']
                    # page = requests.get(url)
                    # soup = BeautifulSoup(page.text, "lxml")
                    try:
                        name = item.find('a', {'class': 'product-list__name'}).text
                        sheet.write(k, 0, name)

                        # descr = item.find('p', {'class': 'catalog-detail__description'}).text
                        # sheet.write(k, 2, descr)

                        prices = item.find_all('div', {'class': 'product-list__price product-list__price_new'})
                        if len(prices) < 1:
                            prices = item.find_all('div', {'class': 'product-list__price'})
                        price = get_value(prices[0].text)
                        sheet.write(k, 2, price)

                        old_prices = item.find_all('div', {'class': 'product-list__price product-list__price_old'})
                        if len(old_prices) > 0:
                            old_price = get_value(old_prices[0].text)
                            sheet.write(k, 3, old_price)

                        sheet.write(k, 4, categoryName + "~" + subCategoryName)

                        # print(name, price, descr, old_price)
                        k += 1
                    except:
                        print(url)
            print(k)

workbook.save("SportMarafon.xls")
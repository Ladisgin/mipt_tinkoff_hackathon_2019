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
    try:
        categoryName = category.find('a', {'class': 'activity-list__name'}).text.strip()
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
                    url = site + item.find_all('a', {'class': 'product-list__name'},href=True)[0]['href']
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "lxml")
                    try:
                        name = soup.find('h1', {'class': 'catalog-detail__name'}).text
                        sheet.write(k, 0, name)

                        prices = soup.find_all('div', {'class': 'catalog-detail__price catalog-detail__price_new'})
                        if len(prices) < 1:
                            prices = soup.find_all('div', {'class': 'catalog-detail__price'})
                        price = re.sub(r"[^\d+]", "", prices[0].text, flags=re.UNICODE)
                        sheet.write(k, 1, price)

                        old_prices = soup.find_all('div', {'class': 'catalog-detail__price catalog-detail__price_old'})
                        if len(old_prices) > 0:
                            old_price = re.sub(r"[^\d+]", "", old_prices[0].text, flags=re.UNICODE)
                            sheet.write(k, 3, old_price)

                        descr = soup.find('p', {'class': 'catalog-detail__description'}).text
                        sheet.write(k, 2, descr)
                        sheet.write(k, 4, categoryName + "+" + subCategoryName)

                        # print(name, price, descr, old_price)
                        k += 1
                    except:
                        print(url)
            # print(k)
    except:
        print(category)

workbook.save("SportMarafon.xls")
from bs4 import BeautifulSoup
import re

def local_html(file):
    with open(file, 'r', encoding="utf-8") as f:
        page = f.read()

    soup = BeautifulSoup(page, 'lxml')
    return soup

def get_price(row):
    num = re.findall("\d+", row.text)
    price = ""
    if len(num) > 1:
        price = f"{num[0]}.{num[1]}"
    else:
        if num != None:
            price = num[0]
        else:
            price = "--"
    return price

def get_supply(row):
    num = re.findall("\d+", row.text)
    return num[0]

def get_name(row):
    div = row.find("div", class_="nft-coll-info__CalendarItem_30xsS")
    a_tag = div.find("a")
    return a_tag.text

def get_website(row):
    div = row.find("div", class_="nft-coll-info__CalendarItem_30xsS")
    a_tag = div.find("a")
    web = a_tag.get("href")
    web = "https://solsea.io" + web
    return web

def get_likes(row):
    likes = row[0].text.replace(" ", "")
    return likes

def get_views(row):
    views = row[1].text.replace(" ", "")
    return views

def get_image(row):
    classed = row.find("img", class_="lazy")
    img = classed.get("src")
    return img

def get_date(row):
    date = row.find("div", class_="undefined calendar-date-holder__CalendarItem_1BAbz")
    month = date.find("div", class_="undefined calendar-month-holder__CalendarItem_7LFQc").text
    day = date.find("div", class_="undefined calendar-day-holder__CalendarItem_2C0O5").text
    year = date.find("div", class_="undefined calendar-year-holder__CalendarItem_2cX1A").text
    timee = date.find("div", class_="undefined calendar-time-holder__CalendarItem_2wpwd").text
    return f"{month} {day}, {year} at {timee}"

def is_verified(row):
    if row.find("span", class_="unverified-collection__CalendarItem_3Xuse") == None:
        return True
    else:
        return False

def get_content(page):
    container = page.find("div", class_="container page-wrapper")
    rows = container.find("div", class_="row")
    row_list = []
    for row in rows:
        row_list.append(row)
    return row_list

from bs4 import BeautifulSoup

def local_html(file):
    with open(file, 'r', encoding="utf-8") as f:
        page = f.read()

    soup = BeautifulSoup(page, 'lxml')
    return soup

def old_get_list(soup):
    content = soup.findAll("tbody")[1]
    areas = []
    for area in content:
        areas.append(area)

    return areas

def get_list(soup):
    content = soup.find("ul", class_="bg-black-def2 divide-y divide-gray-def text-3xs md:text-xs font-light zd-upcoming-nft-wrapper")
    areas = []
    for area in content:
        if len(area) > 3:
            areas.append(area)

    return areas

def old_get_name(area):
    name = area.find("td", class_="ninja_column_0 ninja_clmn_nm_name footable-first-visible")
    return name.text

def get_name(area):
    name = area.findAll("a")[0]
    return name.text

def old_get_price(area):
    price = area.find("td", class_="ninja_column_3 ninja_clmn_nm_price")
    return price.text

def get_price(area):
    price = area.findAll("div", class_="w-25 text-center hidden sm:block")[0]
    return price.text

def old_get_total(area):
    total = area.find("td", class_="ninja_column_4 ninja_clmn_nm_total")
    return total.text

def get_total(area):
    total = area.findAll("div", class_="w-25 text-center hidden sm:block")[1]
    return total.text

def old_get_date(area):
    date = area.find("td", class_="ninja_column_8 ninja_clmn_nm_date footable-last-visible")
    return date.text

def get_date(area):
    date = area.find("div", class_="w-14 md:w-18 lg:w-25 text-center px-2.5")
    return date.text.strip()

def old_get_image(area):
    image_class = area.find("td", class_="ninja_column_1 ninja_clmn_nm_image")
    image_src = image_class.find("img")
    src = image_src.get("src")
    return src

def get_image(area):
    img = area.find("img")
    src = img.get("src")
    return src

def old_get_discord(area):
    discord = area.find("td", class_="ninja_column_6 ninja_clmn_nm_discord")
    tag_a = discord.find("a")
    link = tag_a.get("href")
    return link

def get_discord(area):
    tag = area.find("a", class_="zd-social-link discord w-6 lg:w-8 rounded-full mr-2.5 lg:mr-0")
    if tag == None:
        return "No Discord"
    link = tag.get("href")
    return link

def old_get_twitter(area):
    main_class = area.find("td", class_="ninja_column_5 ninja_clmn_nm_twitter")
    tag_a = main_class.find("a")
    link = tag_a.get("href")
    return link

def get_twitter(area):
    twitter = area.find("a", class_="zd-social-link twitter w-6 lg:w-8 rounded-full mr-2.5 lg:mr-0")
    if twitter == None:
        return "No Twitter"
    link = twitter.get("href")
    return link

def old_get_website(area):
    main_class = area.find("td", class_="ninja_column_7 ninja_clmn_nm_website")
    tag_a = main_class.find("a")
    link = tag_a.get("href")
    return link

def get_website(area):
    web = area.findAll("a")[0]
    link = web.get("href")
    return link

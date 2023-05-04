from selenium import webdriver
from bs4 import BeautifulSoup

LINK5 = "https://upcomingnft.art/"

def get_page(link):
    headers = '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"'
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument(headers)
    driver = webdriver.Chrome(chrome_options=options, executable_path="chromedriver.exe")

    driver.get(link)

    page = driver.page_source

    driver.quit()
    soup = BeautifulSoup(page, 'lxml')
    return soup

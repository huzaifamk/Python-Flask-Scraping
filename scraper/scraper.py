from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from utils.utils import check_lines


def scrape():
    print('Enter scraping link')
    li = input()
    url = str(li)  # Replace with the URL of the website you want to scrape
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--headless=new")
    options.add_argument('--disable-extensions')
    options.add_argument("disable-extensions")
    options.add_argument("disable-infobars")
    options.add_argument("test-type")
    options.add_argument("ignore-certificate-errors")
    # options.add_argument("window-size=1050,800")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-logging')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-features=IsolateOrigins,site-per-process')
    options.add_argument('--disable-site-isolation-trials')
    options.page_load_strategy = 'eager'
    driver: WebDriver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)
    # Send a GET request to the website and retrieve the content
    driver.get(url)
    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')

    elements = soup.find('body').text
    # print(elements)
    ele = []

    with open("text.txt", "w", encoding='utf-8') as f:
        f.write(elements)
    with open("text.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        line = line.strip()
        if line:
            new_lines.append(line)

    print(new_lines)

    check_lines()

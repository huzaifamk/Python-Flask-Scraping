from flask import request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from db.database import mongo


def check_lines(lines):
    lines_with_more_than_two_words = []
    for line in lines:
        line = line.strip()

        words = line.replace('\xa0', '').split()
        if len(words) > 4:
            lines_with_more_than_two_words.append(line)

    data = []
    dat1 = []

    for line in list(set(lines_with_more_than_two_words)):
        data.append(line)

    record = {
        'User_id': 'MllUlAtG9UWDUnzudOXL8HOjyCU2',
        'Data': ''.join(data)
    }
    dat1.append(record)

    print(dat1)
    try:
        mongo(dat1)  # call MongoDB function
    except Exception as f:
        print(f)


def scrape():
    url = request.form.get('url')
    if not url:
        return 'URL is required', 400

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
    driver.get(url)
    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')

    elements = soup.find('body').text
    # Rest of the code...

    lines = elements.split('\n')
    new_lines = []
    for line in lines:
        line = line.strip()
        if line:
            new_lines.append(line)

    check_lines(new_lines)  # Call function

    return 'Scraping completed successfully'


def process():
    text = request.form.get('text')
    if not text:
        return 'Text is required', 400

    lines = text.split('\n')
    new_lines = []
    for line in lines:
        line = line.strip()
        if line:
            new_lines.append(line)

    check_lines(new_lines)  # Call function

    return 'Data processed successfully'

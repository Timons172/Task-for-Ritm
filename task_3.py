"""
Пример работы с Selenium:
    -парсинг сайта 'https://dtf.ru/games' с сохранением в файл 'articles.json'
    данных о названии статьи, ссылке на статью, времени публикации и кратком содержании
"""

import json

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


chrome_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrome_path)
browser = Chrome(service=browser_service)


def wait_element(browser, delay=5, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay).until(
        expected_conditions.presence_of_element_located((by, value))
    )


browser.get('https://dtf.ru/games')
articles_list = browser.find_elements(by=By.CLASS_NAME, value='content--short')

links = []
for article in articles_list:
    link = wait_element(browser=article, by=By.CLASS_NAME, value='content__link') \
            .get_attribute('href')
    links.append(link)

parsed_data = []
for link in links:
    browser.get(link)
    title = wait_element(browser=browser, by=By.TAG_NAME, value='h1').text.strip()
    time = wait_element(browser=browser, by=By.TAG_NAME, value='time').get_attribute('datetime')
    text = wait_element(browser=browser, by=By.CLASS_NAME, value='content__blocks').text

    parsed_data.append({
        'title': title,
        'link': link,
        'time': time,
        'text': text
    })

browser.quit()

with open('articles.json', 'w') as file:
    file.write(json.dumps(parsed_data, ensure_ascii=False, indent=4))

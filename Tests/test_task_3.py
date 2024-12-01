"""
Пример работы с pytest+selenium:
    - проверка на интересующем сайте название темы, заголовка
"""

import pytest

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_selenium():
    chrome_path = ChromeDriverManager().install()
    browser_service = Service(executable_path=chrome_path)
    browser = Chrome(service=browser_service)

    browser.get('https://dtf.ru/games')
    title = browser.title
    heading = browser.find_element(By.TAG_NAME, "h1").text
    try:
        assert title == "Игры (@games) — Сообщество на DTF", f"Название темы неверное. Актуальный название: {title}"
        assert heading == "Игры", f"Заголовок неверный. Актуальный заголовок: {heading}"
        print("Test passed")

    except AssertionError as error:
        print(f"Test failed: {error}")

    finally:
        browser.quit()

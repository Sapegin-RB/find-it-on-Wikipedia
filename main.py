from selenium import webdriver
from selenium.webdriver import Keys # Команда для ввода текста с клавиатуры
from selenium.webdriver.common.by import By # для поиска различных элементов на странице через дом

import time

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

assert "Википедия" in browser.title
time.sleep(5)
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys("Солнечная система")
search_box.send_keys(Keys.RETURN)

time.sleep(5)
a = browser.find_element(By.LINK_TEXT, "Солнечная система")
a.click()


from selenium import webdriver
import time # Модуль позволяет делать задержки в программе
browser = webdriver.Firefox() # Создаем объект нашего браузера
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model") # В браузере заходим на указанную страницу
browser.save_screenshot("dom.png") # Команда делает скриншет открытой страници
time.sleep(5) # Задержка открытого окна 10 сек.
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png") # Команда делает скриншет открытой страници
time.sleep(3)
browser.refresh()

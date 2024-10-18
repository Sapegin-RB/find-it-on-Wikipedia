from selenium import webdriver
import time # Модуль позволяет делать задержки в программе
browser = webdriver.Firefox() # Создаем объект нашего браузера
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model") # В браузере заходим на указанную страницу
time.sleep(10) # Задержка открытого окна 10 сек.
browser.quit() # Команда закрывающая окно сайта

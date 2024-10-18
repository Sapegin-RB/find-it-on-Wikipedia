from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализируем браузер
browser = webdriver.Firefox()  # Создаем экземпляр браузера Firefox для работы с Selenium


def get_paragraphs():
    """Функция для получения параграфов текущей статьи на Википедии"""
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')  # Ищем все элементы с тегом <p> (параграфы)
    return [p.text for p in paragraphs if p.text]  # Возвращаем список текста параграфов, если они не пусты


def get_related_links():
    """Функция для получения связанных ссылок на другие статьи"""
    # Ищем все ссылки, которые находятся в основном контенте статьи, исключая ссылки на редактирование
    links = browser.find_elements(By.XPATH,
                                  '//div[@id="bodyContent"]//a[@href and not(contains(@href, "action=edit"))]')

    related_links = {}  # Создаем пустой словарь для хранения связанных ссылок
    for i, link in enumerate(links[:10]):  # Ограничиваем количество ссылок до 10 для удобства пользователя
        title = link.get_attribute("title")  # Получаем заголовок статьи, на которую ведет ссылка
        href = link.get_attribute("href")  # Получаем саму ссылку
        related_links[i + 1] = (title, href)  # Добавляем ссылку и её заголовок в словарь с индексом
    return related_links  # Возвращаем словарь со связанными ссылками


def display_options(links):
    """Выводим на экран список связанных ссылок"""
    print("\nСвязанные статьи:")  # Сообщение пользователю о начале списка
    for index, (title, href) in links.items():  # Проходимся по словарю ссылок
        print(f"{index}. {title} - {href}")  # Выводим индекс, заголовок статьи и саму ссылку


def main():
    initial_query = input(
        "Введите запрос для поиска на Википедии: ")  # Запрашиваем у пользователя ввод поискового запроса
    browser.get(f"https://ru.wikipedia.org/wiki/{initial_query}")  # Открываем страницу Википедии по запросу

    while True:  # Главный цикл программы, который повторяется, пока пользователь не выйдет
        print("\nВыберите действие:")  # Выводим варианты действий
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")  # Запрашиваем у пользователя ввод номера действия

        if choice == '1':  # Если пользователь выбрал 1, то листаем параграфы статьи
            paragraphs = get_paragraphs()  # Получаем список параграфов текущей статьи
            for paragraph in paragraphs:  # Проходим по каждому параграфу
                print(paragraph)  # Выводим параграф на экран
                time.sleep(1)  # Задержка в 1 секунду для удобства чтения

        elif choice == '2':  # Если пользователь выбрал 2, то предлагаем перейти на связанную страницу
            related_links = get_related_links

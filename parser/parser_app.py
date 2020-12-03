import requests
from bs4 import BeautifulSoup
import logging

def check_categories(url):
    categories_to_find = ['Политика', 'В мире', 'Экономика', 'Общество', 'Происшествия',
                    'Армия', 'Наука', 'Культура', 'Религия', 'Спорт', 'Туризм']
    output = []
    response = requests.get(url)
    html = response.text
    bs = BeautifulSoup(html,'lxml')
    categories = bs.find_all('a', {'class': 'article__tags-item'})
    for category in categories:
        output.append(category.text)
    categories = output
    for category in categories:
        if categories_to_find.__contains__(category):
            cat = category
            return cat
    return ""
def parse_news(card):
    img = card.find('source')
    img_src = img.get('srcset')
    link = card.find('a', {'class': 'list-item__title'})
    href = 'https://ria.ru' + link.get('href')
    title = link.text
    m_response = requests.get(href)
    m_html = m_response.text
    m_bs = BeautifulSoup(m_html, 'lxml')
    date = m_bs.find('div', {'class': 'article__info-date'}).find('a').text
    m_text = m_bs.find_all('div', {'class', 'article__text'})
    output = ""
    for t in m_text:
        output = output + " " + t.text
    m_text = output
    category = check_categories(href)
    # categories = ['Политика', 'В мире', 'Экономика', 'Общество', 'Происшествия',
    #                 'Армия', 'Наука', 'Культура', 'Религия', 'Спорт', 'Туризм']
    # category = m_bs.find_all('a', {'class': 'article__tags-item'})
    # output = []
    # for cat in category:
    #     output.append(cat.text)
    # category = output
    # for cat in category:
    #     if categories.__contains__(cat):
    #         m_cat = cat
    #         fl = 1
    #         pass

    print("Дата публикации: ", date)
    if(len(category)>0):
        print("Категория: ", category)
    else:
        print("Категория: ", "отсутствует")
    print("Заголовок: ", title)
    print("Ссылка на новость: ", href)
    print("Ссылка на картинку: ", img_src)
    print("Текст новости: ", m_text)





def start_parser():
    url = "https://ria.ru/lenta/"
    response = requests.get(url)

    html = response.text
    bs = BeautifulSoup(html, 'lxml')
    container = bs.find('div', {'class': 'list'})
    cards = container.find_all('div', {'class': 'list-item'})
    for card in cards:
        parse_news(card)

if __name__ == '__main__':
    start_parser()
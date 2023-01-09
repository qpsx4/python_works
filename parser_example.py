import requests
from bs4 import BeautifulSoup


def get_page_data(html):
    soup = BeautifulSoup(html.text, 'lxml')
    if (exist_table := soup.find('table', id='theProxyList')) is None:
        return 0
    else:
        for elem in exist_table.find('tbody').findAll('tr'):
            td = elem.find_all('td')
            ip, port = td[1].text, td[2].text
            print(f"{ip}:{port}")


def pages_count(html):
    soup = BeautifulSoup(html.text, 'lxml')
    pages = soup.find('div', {'class': 'pager'}).getText()[-1]
    return int(pages)


if __name__ == "__main__":
    url = "http://foxtools.ru/Proxy?page="
    for page_number in range(pages_count(requests.get(url + "1"))):
        page_number += 1
        get_page_data(requests.get(url + str(page_number)))
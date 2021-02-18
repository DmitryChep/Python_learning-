from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.ua-football.com')
html = req.read()
soup = BeautifulSoup(html, "html.parser")
news = soup.find_all('li', class_='mb-3')

results = []
for item in news:
    title = item.find('span', class_='heading').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    results.append({'title': title,
                    'desc': desc,
                    'href': href,
                    })
file = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    file.write(f'Новость №{i}\n\n Название: {item["title"]}\n Описание: {item["desc"]}\n Ссылка: {item["href"]} \n\n'
               f'**********************************\n\n')
    i += 1

file.close()

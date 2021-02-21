from bs4 import BeautifulSoup
'''
ip install beautifulsoup4 - to install bs4 
'''
import urllib.request


class SearchHTML:
    def __init__(self, url):
        self.url = url

    @property
    def get_URL(self):
        req = urllib.request.urlopen(self.url)
        html = req.read()
        soup = BeautifulSoup(html, "html.parser")
        news = soup.find_all('li', class_='mb-3')
        return news



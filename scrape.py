import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

links = soup.select('.storylink')
subtext = soup.select('.subtext')


def get_highest_news(news):
    return sorted(news, key=lambda k: k['points'], reverse=True)


def create_hn_dictionary(links, subtext):
    h_news = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText('.score').replace(' points', ''))
            if points > 99:
                h_news.append({'title': title, 'href': href, 'points': points})

    return get_highest_news(h_news)


pprint.pprint(create_hn_dictionary(links, subtext))

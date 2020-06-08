import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

links = soup.select('.storylink')
subtext = soup.select('.subtext')


def get_top_titles(news):
    return sorted(news, key=lambda k: k['points'], reverse=True)


def create_n_dict(links, subtext):
    h_news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                h_news.append({'title': title, 'href': href, 'points': points})
    return get_top_titles(h_news)


pprint.pprint(create_n_dict(links, subtext))

import feedparser
from bs4 import BeautifulSoup

def latestSteamPost():
        steamRSSUrl = "https://store.steampowered.com/feeds/news/app/1282270/"

        rssParsed = feedparser.parse(steamRSSUrl)

        descHTML = (rssParsed['entries'][0]['summary']).replace('<br />', '\n')
        parser = BeautifulSoup(descHTML, features="html.parser")
        publishedDate = rssParsed['entries'][0]['published'][5:-6]

        return { 
                "title": rssParsed['entries'][0]['title'], 
                "description": parser.get_text(),
                "date": publishedDate
        }

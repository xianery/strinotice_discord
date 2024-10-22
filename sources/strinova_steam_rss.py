import feedparser
from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
        text = ""
        def handle_data(self, data):
                self.text += data

def Steam():
        steamRSSUrl = "https://store.steampowered.com/feeds/news/app/1282270/"

        rssParsed = feedparser.parse(steamRSSUrl)

        latestPostTitle = rssParsed['entries'][0]['title']

        latestPostDescHTML = HTMLFilter()
        latestPostDescHTML.feed(rssParsed['entries'][0]['summary'])
        latestPostDesc = latestPostDescHTML.text

        return latestPostTitle + "\n\n" + latestPostDesc

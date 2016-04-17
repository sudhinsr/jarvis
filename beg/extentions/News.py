# -*- coding: utf-8-*-
import re
import feedparser


WORDS = ["NEWS"]

PRIORITY = 3



class Article:

    def __init__(self, title):
        self.title = title
        """self.URL = URL"""


def getTopArticles(maxResults=None):
    d = feedparser.parse("https://news.google.com/?output=rss")
    count = 0
    articles = []
    for item in d['items']:
        articles.append(Article(item['title'])) 
        count += 1
        if maxResults and count > maxResults:
            break

    return articles


def handle(mic):
	
  
    mic.say("Pulling up the news")
    articles = getTopArticles(maxResults=3)
    titles = [" ".join(x.title.split(" - ")[:-1]) for x in articles]
    all_titles = "... ".join(str(idx + 1) + "  " + title for idx, title in enumerate(titles))
    print all_titles
   
    mic.say("Here are the current top headlines. " )
    mic.say(all_titles)


def isValid(text):
   
    return bool(re.search(r'\b(news|headline)\b', text, re.IGNORECASE))

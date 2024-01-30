# app/main.py
import feedparser
from app.models import Base
from app.utils import parse_and_process_article

RSS_FEEDS = [
    'http://rss.cnn.com/rss/cnn_topstories.rss',
    'http://qz.com/feed',
    'http://feeds.foxnews.com/foxnews/politics',
    'http://feeds.reuters.com/reuters/businessNews',
    'http://feeds.feedburner.com/NewshourWorld',
    'https://feeds.bbci.co.uk/news/world/asia/india/rss.xml'
]

def fetch_and_process_feeds():
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            article_data = {
                'title': entry.title,
                'content': entry.summary,
                'source_url': entry.link
            }
            parse_and_process_article.delay(article_data)

if __name__ == "__main__":
    # Fetch and process feeds
    fetch_and_process_feeds()

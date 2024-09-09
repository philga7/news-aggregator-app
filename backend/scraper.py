from newspaper import Article, build
from datetime import datetime

def extract_article_urls(news_site_url):
    """Extract article URLs using Newspaper3k's 'build' method."""
    paper = build(news_site_url, memoize_articles=False)
    article_urls = [article.url for article in paper.articles]
    
    return article_urls

def scrape_article(url):
    """Scrapes the article content from the given URL using Newspaper3k"""
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()  # Optional: NLP for keywords and summary

    return {
        'title': article.title,
        'author': article.authors,
        'url': article.url,
        'body': article.text,
        'published_date': article.publish_date or datetime.now(),
        'summary': article.summary,
        'keywords': article.keywords
    }

# type: ignore
from newspaper import Article

# Scrape article content using newspaper3k
def scrape_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return {
        'title': article.title,
        'text': article.text,
        'publish_date': article.publish_date
    }

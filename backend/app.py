from scraper import extract_article_urls, scrape_article
from database import session, news_table
from sqlalchemy import insert
import os
import uuid

API_KEY = os.getenv('NEWSAPI_KEY')

# List of news site URLs to scrape
NEWS_SITE_URLS = [
    f"https://newsapi.org/v2/top-headlines?country=us&apiKey=${API_KEY}",
]

def save_article(article_data):
    """Save the scraped article into the database"""
    stmt = insert(news_table).values(
        id=str(uuid.uuid4()),
        title=article_data['title'],
        url=article_data['url'],
        author=', '.join(article_data['author']),
        body=article_data['body'],
        published_date=article_data['published_date'],
        summary=article_data['summary'],
        keywords=', '.join(article_data['keywords'])
    )
    session.execute(stmt)
    session.commit()

def scrape_and_store():
    """Main function to scrape article URLs and save articles"""
    
    for news_site_url in NEWS_SITE_URLS:
        print(f"Scraping site: {news_site_url}")

        # Extract article URLs from the current news site
        article_urls = extract_article_urls(news_site_url)

        # Scrape and save each article from the extracted URLs
        for url in article_urls:
            try:
                article_data = scrape_article(url)
                save_article(article_data)
                print(f"Saved article: {article_data['title']}")
            except Exception as e:
                print(f"Failed to scrape or save article from {url}: {str(e)}")

if __name__ == '__main__':
    scrape_and_store()

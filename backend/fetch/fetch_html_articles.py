# type: ignore
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import torch
from pymongo import MongoClient
from datetime import datetime
from urllib.parse import urlparse

# Define a blacklist of domains to exclude (e.g., GitHub, personal websites, etc.)
BLACKLISTED_DOMAINS = [
    'github.com',
    'jeffjadulco.com',  # Add other personal or irrelevant domains as needed
    'ycombinator.com',
]

# MongoDB connection details (assuming MongoDB is exposed on localhost:27017)
client = MongoClient('mongodb://admin:1234qwer@localhost:27017/')

# Create or switch to the database
db = client['news_database']
# Create or switch to the collection (like a table in SQL)
articles_collection = db['articles']

# Set device (GPU if available)
# device = 0 if torch.cuda.is_available() else -1

# Hugging Face Summarization Pipeline (you can also use other models)
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device, clean_up_tokenization_spaces=True)

def fetch_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def is_external_link(href, full_url, base_domain):
    # Filter out mailto links and other non-http(s) schemes
    if href.startswith('mailto:'):
        return False  # Ignore mailto links explicitly
    
    parsed_url = urlparse(full_url)
    
    # If the netloc (domain) of the parsed URL is empty, it's a relative link; otherwise, it's absolute.
    if not parsed_url.netloc:
        return True  # Relative URL, considered external
    
    # Check if the scheme is HTTP/HTTPS, ignore other schemes like mailto, javascript, ftp, etc.
    if parsed_url.scheme not in ['http', 'https']:
        return False  # Ignore non-HTTP/HTTPS links
    
    # Exclude URLs from blacklisted domains
    for domain in BLACKLISTED_DOMAINS:
        if domain in parsed_url.netloc:
            return False  # Blacklisted, so not valid

    # If the domain of the link doesn't match the base domain, it's external
    return base_domain not in parsed_url.netloc

def extract_article_data(html, base_url):
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extract base domain from the base URL
    base_domain = urlparse(base_url).netloc

    # Find all anchor (`<a>`) tags
    article_links = []
    
    # Loop through all <a> tags that might represent article links
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        title = a_tag.get_text(strip=True)  # Strip extra whitespace from the title
        
        # Ensure the href is a valid article URL (skip empty or '#' links)
        if href and href != '#' and len(title) > 0:
            # Handle relative URLs by converting them to absolute URLs
            full_url = requests.compat.urljoin(base_url, href)
            
            # Ignore links that are internal (contain the base domain)
            if is_external_link(href, full_url, base_domain):
                article_links.append({
                    "url": full_url,
                    "title": title
                })
    
    return article_links

    # Package article data
    # article_data = {
    #     "title": title,
    #     "author": author,
    #     "content": article_summary,
    #     "description": article_summary[:200],  # Use first 200 chars as a description
    #     "url": url
    # }
    # return article_data

def store_article(article_data):
    # Prepare MongoDB data structure
    article = {
        "source": {"name": article_data.get("url")},
        "author": article_data.get("author", "Unknown"),
        "title": article_data.get("title", "No Title"),
        "description": article_data.get("description", ""),
        "url": article_data.get("url"),
        "urlToImage": "",  # Could be extracted separately, omitted here
        "publishedAt": datetime.now().isoformat(),
        "content": article_data.get("content", "")
    }
    articles_collection.insert_one(article)

def scrape_news_aggregators():
    # News aggregator URLs
    news_urls = [
        'https://citizenfreepress.com',
    ]

    for url in news_urls:
        html_content = fetch_html_content(url)
        if html_content:
            articles = extract_article_data(html_content, url)
            for article in articles:
                print(f"Title: {article['title']}, URL: {article['url']}")

if __name__ == "__main__":
    scrape_news_aggregators()

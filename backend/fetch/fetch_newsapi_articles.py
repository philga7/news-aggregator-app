# type: ignore
import requests
from pymongo import MongoClient

# MongoDB connection details (assuming MongoDB is exposed on localhost:27017)
client = MongoClient('mongodb://admin:1234qwer@localhost:27017/')

# Create or switch to the database
db = client['news_database']
# Create or switch to the collection (like a table in SQL)
articles_collection = db['articles']

# NewsAPI settings
NEWS_API_KEY = '5c38ffcd947e42fbaf45b975af9668f8'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

def fetch_articles():
    # Parameters for NewsAPI request
    params = {
        'country': 'us',
        'apiKey': NEWS_API_KEY,
        'pageSize': 100,  # Fetch up to 100 articles per request (max allowed by NewsAPI)
    }

    # Make a request to NewsAPI
    response = requests.get(NEWS_API_URL, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response as a Python dictionary
        return response.json().get('articles', [])
    else:
        print(f"Failed to fetch articles. Status code: {response.status_code}")
        return []
    
def store_articles_in_mongodb(articles):
    # Initialize the counters outside the loop
    stored_count = 0
    duplicate_count = 0
    
    if not articles:
        print("No articles to store.")
        return

    # Insert articles into MongoDB (ignoring duplicates by checking URL or another unique field)
    for article in articles:
        # Use URL as the unique identifier to avoid duplicates
        if articles_collection.count_documents({"url": article['url']}, limit=1) == 0:
            # Insert new article
            articles_collection.insert_one(article)
            stored_count += 1
        else:
            # Count duplicates
            duplicate_count += 1

    return stored_count, duplicate_count

if __name__ == '__main__':
    # Fetch articles from NewsAPI
    articles = fetch_articles()

    # Store the articles in MongoDB and track how many were stored and how many were duplicates
    stored_count, duplicate_count = store_articles_in_mongodb(articles)

    # Final messages
    print(f"Successfully stored {stored_count} new articles in MongoDB.")
    if duplicate_count > 0:
        print(f"Skipped {duplicate_count} duplicate articles.")

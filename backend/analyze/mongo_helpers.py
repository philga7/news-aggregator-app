# type: ignore
from pymongo import MongoClient

# MongoDB Setup
client = MongoClient("mongodb://admin:1234qwer@localhost:27017/")
db = client['news_database']
collection = db['articles']

# Fetch articles that need processing from MongoDB. This will return a cursor object that needs to be iterated over.
def fetch_unprocessed_articles():
    cursor = collection.find({
        'analyzed': False
    })

    return cursor

# Save or update the article data into MongoDB
def save_to_mongodb(article_data):
    print(f"Saving article data for URL {article_data['url']}")
    update_data = {**article_data, 'analyzed': True}

    collection.update_one(
        {'url': article_data['url']},
        {
            '$set': update_data
        },
        upsert=True
    )
    print(f"Article data saved successfully.")

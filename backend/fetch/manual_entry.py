# type: ignore
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection details (assuming MongoDB is exposed on localhost:27017)
client = MongoClient('mongodb://admin:1234qwer@localhost:27017/')

# Create or switch to the database
db = client['news_database']
# Create or switch to the collection (like a table in SQL)
articles_collection = db['articles']

# Function to add a new entry to MongoDB (with publishedAt field)
def add_entry(source, url, title, description, published_at=None):
    # If publishedAt is not provided, set it to the current date and time
    if not published_at:
        published_at = datetime.now()

    new_entry = {
        "source": source,
        "url": url,
        "title": title,
        "description": description,
        "save": True,  # Automatically mark the entry as permanently saved
        "entry_type": "manual",  # Mark this entry as a manual entry
        "publishedAt": published_at,  # Store the publishedAt date
        "analyzed": False  # Mark the entry as
    }

    # Insert the document into the collection
    result = articles_collection.insert_one(new_entry)

    print(f"Entry saved with ID: {result.inserted_id}")

# Main function to handle user input
def main():
    print("Add a new item to your collection.")

    source = input("Source (e.g., X.com, YouTube, Blog): ")
    url = input("URL: ")
    title = input("Title: ")
    description = input("Description/Notes: ")

    # Ask if the user wants to manually input the publishedAt date
    published_at_input = input("Published at (optional, format: YYYY-MM-DD HH:MM:SS) or leave blank for current time: ")
    published_at = None

    if published_at_input:
        try:
            # Convert user input to a datetime object
            published_at = datetime.strptime(published_at_input, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid date format. Setting to current date and time.")
            published_at = datetime.now()

    # Add the entry to MongoDB
    add_entry(source, url, title, description, published_at)

    print("\nItem added successfully!")

if __name__ == "__main__":
    main()

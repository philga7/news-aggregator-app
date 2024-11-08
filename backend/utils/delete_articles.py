import argparse
from pymongo import MongoClient
from datetime import datetime, timedelta, timezone

#
# python delete_articles.py 30 days
#
def delete_old_articles(age_value, age_unit):
    # Connect to the MongoDB client
    client = MongoClient('mongodb://admin:1234qwer@localhost:27017/')

    try:
        # Select the news_database and articles collection
        db = client['news_database']
        articles = db['articles']

        # Calculate the cutoff date with timezone-aware datetime in UTC
        cutoff_date = datetime.now(timezone.utc)

        if age_unit == 'days':
            cutoff_date -= timedelta(days=age_value)
        elif age_unit == 'weeks':
            cutoff_date -= timedelta(weeks=age_value)
        elif age_unit == 'months':
            # Handle month subtraction and year overflow manually
            month = (cutoff_date.month - age_value - 1) % 12 + 1
            year = cutoff_date.year + (cutoff_date.month - age_value - 1) // 12
            cutoff_date = cutoff_date.replace(year=year, month=month)
        
        # Perform the delete operation, ensuring that 'save' is False or not present
        result = articles.delete_many({
            'publishedAt': {'$lt': cutoff_date.isoformat() + "Z"},
            'save': {'$ne': True}  # Articles where "save" is True are not deleted
        })

        print(f"{result.deleted_count} documents deleted.")

    finally:
        # Close the MongoDB connection
        client.close()

if __name__ == "__main__":
    # Set up the argument parser for CLI input
    parser = argparse.ArgumentParser(description='Delete old articles from MongoDB.')
    
    parser.add_argument(
        'age_value', 
        type=int, 
        help='The value for age (number of days, weeks, or months).'
    )

    parser.add_argument(
        'age_unit', 
        choices=['days', 'weeks', 'months'], 
        help='The unit of age to determine how old articles should be deleted (days, weeks, or months).'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with CLI input
    delete_old_articles(args.age_value, args.age_unit)

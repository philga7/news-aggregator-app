import os
import psycopg2
from dotenv import load_dotenv

# PostgreSQL connection details (for Python)
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_NAME = os.environ.get("POSTGRES_DB_NAME")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

def insert_article_to_db(connection, title, body, author, publish_date, url, summary, keywords):
    cursor = connection.cursor()
    query = """
        INSERT INTO news_articles (title, body, author, publish_date, url, summary, keywords)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(query, (title, body, author, publish_date, url, summary, keywords))
        connection.commit()
    except Exception as e:
        print("Error inserting article:", e)
        connection.rollback()
    finally:
        cursor.close()

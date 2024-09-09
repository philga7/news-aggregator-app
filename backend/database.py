import os
from sqlalchemy import create_engine, Column, String, Text, DateTime, Table, MetaData
from sqlalchemy.orm import sessionmaker

# Use environment variable for the database URL
DATABASE_URL = os.getenv('POSTGRES_URL')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

# Define the news table schema
news_table = Table('news_articles', metadata,
    Column('id', String, primary_key=True),
    Column('title', String, nullable=False),
    Column('url', String, nullable=False),
    Column('author', String),
    Column('body', Text, nullable=False),
    Column('published_date', DateTime),
    Column('summary', Text),
    Column('keywords', Text)
)

# Create table if it doesn't exist
metadata.create_all(engine)

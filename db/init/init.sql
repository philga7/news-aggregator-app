DO $$BEGIN
IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'newsuser')
THEN CREATE ROLE newsuser WITH LOGIN PASSWORD 'OtSsEZ9RpB10SG';
END IF;
END$$;

CREATE DATABASE newssitedb WITH OWNER newsuser;

GRANT ALL PRIVILEGES ON DATABASE newssitedb TO newsuser;

CREATE TABLE IF NOT EXISTS news_articles (
    id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    author TEXT,
    body TEXT NOT NULL,
    published_date TIMESTAMP,
    summary TEXT,
    keywords TEXT
);

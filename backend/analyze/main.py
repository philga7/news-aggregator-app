# type: ignore
from mongo_helpers import fetch_unprocessed_articles, save_to_mongodb
from article_scraper import scrape_article
from sanity_check_models import sanity_check_models
from huggingface_api import process_text
from video_processor import is_video_url, extract_video_metadata, process_subtitles

def process_article(url):
    # Handle video URLs
    if is_video_url(url):
        print(f"Detected video URL: {url}")
        video_data = extract_video_metadata(url)
        text = video_data['description'] or ''
        title = video_data['title']
        transcript = video_data.get('subtitles', None)
        if transcript:
            subtitle_text = process_subtitles(transcript)
            text += "\n" + subtitle_text

        if video_data['has_captions']:
            print("Captions found, processing subtitles.")
            subtitle_text = process_subtitles(video_data['subtitles'])
            text += "\n" + subtitle_text  # Combine description and captions

    else:
        # Scrape article if it's not a video
        #print(f"Scraping article: {url}")
        article = scrape_article(url)
        #print(f"Scraped article: {article}")
        title = article['title']
        print(f"Title: {title}")
        text = article['text']
        #print(f"Text: {text}")

    # Skip processing if no text is found
    if not text.strip():
        print(f"No usable text for URL: {url}")
        return

    # Extract all entities, including Why and How using Hugging Face QA
    all_entities = process_text(text)
    print(f"Extracted entities: {all_entities}")
    # Combine extracted data
    article_data = {
        'url': url,
        'title': title,
        'text': text,
        'who': all_entities['who'],
        'where': all_entities['where'],
        'when': all_entities['when'],
        'why': all_entities['why'],
        'how': all_entities['how']
    }
    #print(f"Article data: {article_data}")
    # Save to MongoDB
    save_to_mongodb(article_data)

# Batch process articles or videos
def process_articles_in_batch():
    cursor = fetch_unprocessed_articles()
    #print(cursor)
    for article in cursor:
        #print(f"Processing article: {article}")
        url = article.get('url')
        print(f"URL: {url}")
        if url:
            try:
                print(f"Processing URL: {url}")
                process_article(url)
                print(f"Successfully processed: {url}")
            except Exception as e:
                print(f"Error processing {url}: {str(e)}")

# Main function to run the batch processing
if __name__ == "__main__":
    # Sanity check models
    ner_model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"  # NER model
    ap_model_name = "deepset/roberta-base-squad2"    # AP model (text classification)

    sanity_check_models(ner_model_name, ap_model_name)
    process_articles_in_batch()
# type: ignore
import requests
import re

# Hugging Face API Configurations
HUGGINGFACE_NER_API_URL = "https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english"
HUGGINGFACE_QA_API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
HUGGINGFACE_API_KEY = "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"

HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
}

# Function to clean text (remove special characters, non-ASCII, etc.)
def clean_text(text):
    # Remove non-ASCII characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # Optionally remove other unwanted characters, if necessary
    text = re.sub(r'[^\w\s,.!?]', '', text)
    return text

# Function to clean and validate NER tokens
def clean_ner_tokens(entities):
    return [entity for entity in entities if not entity.startswith("##")]

# Query Hugging Face API for NER
def query_ner_model(text):
    if not text:
        print("Error: No text provided for NER.")
        return None

    payload = {"inputs": text}
    #print(f"query_ner_model: {payload}")
    try:
        response = requests.post(HUGGINGFACE_NER_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during NER API call: {str(e)}")
        return None

# Function to extract NER entities from summarized text
def extract_ner_from_text(text):
    # Step 1: Extract NER entities from the summarized text
    ner_results = query_ner_model(text)

    if not ner_results or not isinstance(ner_results, list):
        print("Error: NER results are invalid or empty.")
        return {'who': [], 'where': [], 'when': []}

    # Step 2: Process the NER results into 'who', 'where', 'when' categories 
    who, where, when = set(), set(), set()

    for entity in ner_results:
        if isinstance(entity, dict):
            print(f"extract_ner_entities-entity: {entity}")
            entity_text = entity.get('word')
            print(f"extract_ner_entities-entity_text: {entity_text}")
            entity_type = entity.get('entity_group')
            print(f"extract_ner_entities-entity_type: {entity_type}")

            # Clean the entity text
            cleaned_entity_text = clean_ner_tokens([entity_text])

            if cleaned_entity_text: # Proceed only if cleaned text is valid
                entity_text = cleaned_entity_text[0]

                if entity_type == 'PER':
                    who.add(entity_text)
                elif entity_type == 'ORG':
                    who.add(entity_text)
                elif entity_type == 'LOC':
                    where.add(entity_text)
                elif entity_type == 'DATE':
                    when.add(entity_text)
                print(f"extract_ner_entities-entity_types_who_where_when: {who}, {where}, {when}")
        #     else:
        #         print(f"Entity {entity} discarded after cleaning.")
        # else:
        #     print(f"Unexpected entity format: {entity}")

    return {'who': list(who), 'where': list(where), 'when': list(when)} 

# Query Hugging Face API for question answering
def query_huggingface_api(question, context):
    if not context:
        print("Error: No context provided for QA.")
        return {}

    payload = {"inputs": {"question": question, "context": context}}
        #print(f"query_huggingface_api-payload: {payload}")
    try:
        response = requests.post(HUGGINGFACE_QA_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during QA API call: {str(e)}")
        #print(f"query_huggingface_api-response-json: {response.json()}")
        return {}

# Extract Why and How using Hugging Face QA model
def extract_why_and_how(text):
    why_answer = query_huggingface_api("Why did this happen?", text)
    print(f"extract_why_and_how-why-answer: {why_answer}")
    how_answer = query_huggingface_api("How did this happen?", text)
    print(f"extract_why_and_how-how-answer: {how_answer}")
    return {
        'why': why_answer.get('answer', 'N/A'),
        'how': how_answer.get('answer', 'N/A')
    }

# Main function that orchestrates the summarization and calls both extraction functions
def process_text(text):
    try:
        # Clean the text
        cleaned_text = clean_text(text)

        # Extract NER entities from the summary
        ner_entities = extract_ner_from_text(cleaned_text)
        print(f"Extracted NER entities: {ner_entities}")
        
        # Ensure that the necessary keys ('who', 'where', 'when') exist
        who = ner_entities.get('who', [])
        where = ner_entities.get('where', [])
        when = ner_entities.get('when', [])

        # Extract 'why' and 'how' from the summary
        why_and_how = extract_why_and_how(cleaned_text)
        print(f"Extracted 'why' and 'how': {why_and_how}")
        
        # Combine results
        return {
            'who': who,
            'where': where,
            'when': when,
            'why': why_and_how.get('why', 'N/A'),
            'how': why_and_how.get('how', 'N/A')
        }
    
    except KeyError as e:
        print(f"Missing key in extracted entities: {e}")
        return {
            'who': [],
            'where': [],
            'when': [],
            'why': 'N/A',
            'how': 'N/A'
        }
    except Exception as e:
        print(f"Error processing text: {str(e)}")
        return {
            'who': [],
            'where': [],
            'when': [],
            'why': 'N/A',
            'how': 'N/A'
        }

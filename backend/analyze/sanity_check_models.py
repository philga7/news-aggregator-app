# type: ignore
import requests
import time

# Hugging Face API settings
HEADERS = {"Authorization": f"Bearer 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"}
MAX_RETRIES = 10
DEFAULT_WAIT_TIME = 5  # seconds

# Function to check model loading status
def check_model_status(model_name):
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    response = requests.get(api_url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} while checking model {model_name}")
        return None
    
# Function to wait for model to load
def wait_for_model_load(model_name):
    for i in range(MAX_RETRIES):
        print(f"Checking model status for {model_name} (attempt {i + 1})...")
        status = check_model_status(model_name)

        if status:
            if status.get("loading", False):
                estimated_time = status.get("estimated_time", DEFAULT_WAIT_TIME)
                print(f"Model {model_name} is still loading, estimated time: {estimated_time} seconds")
                time.sleep(estimated_time)  # Wait and retry
            else:
                print(f"Model {model_name} is loaded and ready!")
                return True
        else:
            print(f"Error fetching model status for {model_name}, retrying in {DEFAULT_WAIT_TIME} seconds.")
            time.sleep(DEFAULT_WAIT_TIME)
    
    raise Exception(f"Model {model_name} failed to load within the expected time")

# Main function to check both NER and AP models
def sanity_check_models(ner_model_name, ap_model_name):
    # Check NER model
    if wait_for_model_load(ner_model_name):
        print(f"NER model '{ner_model_name}' is ready.")

    # Check AP model
    if wait_for_model_load(ap_model_name):
        print(f"AP model '{ap_model_name}' is ready.")

import requests
import json

def connect_to_gemini(dialogue):
    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}'    
    headers = {'Authorization': 'Bearer YOUR_API_KEY'}
    payload = {'dialogue': dialogue}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for 4xx/5xx status codes

        parsed_response = response.json()  # Convert response to JSON
        return parsed_response

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Gemini: {e}")
        return None

def write_to_dataset(data, dataset_path):
    try:
        with open(dataset_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data written to {dataset_path} successfully.")
    except Exception as e:
        print(f"Error writing to dataset: {e}")

# Example usage
if __name__ == "__main__":
    dialogue = "User: Hello! Gemini: Hi there, how can I help you?"
    parsed_result = connect_to_gemini(dialogue)

    if parsed_result:
        dataset_path = "output_dataset.json"
        write_to_dataset(parsed_result, dataset_path)
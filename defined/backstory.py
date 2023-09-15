from defined.char_builder import character

import os

API_KEY = os.getenv("gpt_key")

import requests


def generate_character_backstory(character):
    api_key = API_KEY

    # Construct the prompt using the character's attributes
    prompt = f"Create a backstory for a {character.race} {character.characterClass} named {character.name}. "

    # Define the API endpoint
    api_endpoint = "https://api.openai.com/v1/engines/davinci/completions"

    # Define the request headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Define the request payload
    data = {
        "prompt": prompt,
        "max_tokens": 150,  # You can adjust the maximum number of tokens here
        "temperature": 0.7,  # You can adjust the temperature to control the randomness of the output
    }

    try:
        # Make the API request
        response = requests.post(api_endpoint, headers=headers, json=data)
        response.raise_for_status()

        # Get the generated backstory
        backstory = response.json()["choices"][0]["text"]

        return backstory

    except Exception as e:
        print(f"Error: {str(e)}")
        return None


# # Example usage:
# backstory = generate_character_backstory(character)
# print(backstory)

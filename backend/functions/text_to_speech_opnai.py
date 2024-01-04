from decouple import config
import requests

#Retrieve environment variables
OPEN_AI_KEY = config('OPEN_AI_KEY')

#Open AI text to speech
#Convert Text to Audio

def convert_text_to_speech(message):
    #Define Data body
    body = {
        "model": "tts-1",
        "input": message,
        "voice": "nova"
        }

    # Constructing Headers and Endpoint
    headers = {'Authorization': f'Bearer {OPEN_AI_KEY}', 'Content-Type': 'application/json'}
    url = 'https://api.openai.com/v1/audio/speech'

    # Send request
    try:
        response = requests.post(url, json=body, headers=headers)
    except Exception as e:
        print(f"Error: {e}")
        return
    
    #"Handle response
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return

    

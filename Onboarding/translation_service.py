# translateapp/translation_service.py
import requests

def libre_translate(text, target_language):
    url = "https://libretranslate.de/translate"
    payload = {
        'q': text,
        'source': 'en',  # source language
        'target': target_language,
        'format': 'text'
    }
    response = requests.post(url, data=payload)
    return response.json()['translatedText']

"""
This module is used to translate text
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


SERVICE_URL = "https://api.us-south.language-translator.watson.cloud.ibm.com"
API_KEY = "OzxRv5gw9Z5gc-nN78e6-S0WtgtfISGefRk5dtpcamvR"

def english_to_french(text=None):
    """
    This function is used to translation from English to French
    """
    if text:
        authenticator = IAMAuthenticator(API_KEY)
        language_translator = LanguageTranslatorV3(
            version='2019-04-30',
            authenticator=authenticator
        )

        language_translator.set_service_url(SERVICE_URL)

        translation = language_translator.translate(
            text=text,
            model_id='en-fr',
            source='en',
            target='fr'
        ).get_result()

        results_string = json.dumps(translation, indent=2, ensure_ascii=False)
        results_json = json.loads(results_string)

        translated_text = results_json["translations"][0]["translation"]
        print(translated_text)
        return translated_text

    return None


def english_to_german(text=None):
    """
    This function is used to translation from English to German
    """
    if text:
        authenticator = IAMAuthenticator(API_KEY)
        language_translator = LanguageTranslatorV3(
            version='2019-04-30',
            authenticator=authenticator
        )

        language_translator.set_service_url(SERVICE_URL)

        translation = language_translator.translate(
            text=text,
            model_id='en-de',
            source='en',
            target='de'
        ).get_result()

        results_string = json.dumps(translation, indent=2, ensure_ascii=False)
        results_json = json.loads(results_string)

        translated_text = results_json["translations"][0]["translation"]
        print(translated_text)
        return translated_text

    return None

english_to_german("Hello")

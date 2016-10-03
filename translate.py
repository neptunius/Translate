import httplib2
import urllib
import json
from pprint import pprint


# Google Cloud API constants
GOOGLE_API_KEY = "--- secret ---"
GOOGLE_TRANSLATE_URL = "https://www.googleapis.com/language/translate/v2"


def translate(text):
    # Assemble the full URL with the query parameters
    url = GOOGLE_TRANSLATE_URL + "?key=" + GOOGLE_API_KEY
    url += "&source=en"
    url += "&target=es"
    url += "&q=" + urllib.quote_plus(text)

    # Create an HTTP client and make a GET request to the URL
    http = httplib2.Http()
    response, body = http.request(url, "GET")

    # Parse the JSON document into native Python structures
    content = json.loads(body)

    # Retrieve the translated text from the nested structure
    translatedText = content['data']['translations'][0]['translatedText']
    return translatedText


if __name__ == "__main__":
    # Test the translate function
    print translate("Hello world")

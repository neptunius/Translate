import httplib2
import urllib
import json
from pprint import pprint

GOOGLE_API_KEY = "--- secret ---"
GOOGLE_TRANSLATE_URL = "https://www.googleapis.com/language/translate/v2"
# params: ?key=$GOOGLE_API_KEY&source=en&target=es&q=Hello%20world"

url = GOOGLE_TRANSLATE_URL + "?key=" + GOOGLE_API_KEY
url += "&source=en"
url += "&target=es"
url += "&q=" + urllib.quote_plus("Hello world")

http = httplib2.Http()
# resp, content = http.request(url, method, headers=headers, body=data)
response, body = http.request(url)

# print type(response)
# pprint(response)

# print type(body)
# print body

content = json.loads(body)
# print type(content)
# print content

translatedText = content['data']['translations'][0]['translatedText']
# print type(translatedText)
print translatedText

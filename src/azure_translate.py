import json
import requests
import urllib
import sys

def trans(term):
	args = {
		'client_id': 'jackg825',#your client id here
		'client_secret': 'EyxaIr5iHMUMWvFkM3cZY9rMSSYjYSpLEDXKAHvhMhU=',#your azure secret here
		'scope': 'http://api.microsofttranslator.com',
		'grant_type': 'client_credentials'
	    }
	oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
	oauth_junk = json.loads(requests.post(oauth_url,data=urllib.urlencode(args)).content)
	translation_args = {
		'text': term,
		'to': 'zh-CHT',
		'from': 'en'
		}
	headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
	translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
	translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
	
	return translation_result.content



#print trans("fuck")

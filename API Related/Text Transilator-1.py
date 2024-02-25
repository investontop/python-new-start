# https://rapidapi.com/
# Remember this API requires Subscription (I subscribed BASIC). 1000 request per month.

import requests



# :Translating the TEXT using POST
# url = "https://text-translator2.p.rapidapi.com/translate"
# payload = {
#     "source_language": "en",
#     "target_language": "id",
#     "text": "What is your name?"
# }
# headers = {
#     "content-type": "application/x-www-form-urlencoded",
#     "X-RapidAPI-Key": "b3313c3760msh810678525cdff97p1eb563jsn701a8ffd6ba9",
#     "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
# }
#
# response = requests.post(url, data=payload, headers=headers)
#
# print(response.json())







# :Get the list of Languages
# import requests
# from tinydb import TinyDB
#
# url = "https://text-translator2.p.rapidapi.com/getLanguages"
#
# headers = {
#     "X-RapidAPI-Key": "b3313c3760msh810678525cdff97p1eb563jsn701a8ffd6ba9",
#     "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers)
#
# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Extract the languages from the "data" key
#     languages = [{"language": lang['name'], "code": lang['code']} for lang in response.json()['data']['languages']]
#
#     # Store languages in TinyDB
#     db = TinyDB('TextConv.json')
#     language_table = db.table('Language')
#     language_table.insert_multiple(languages)
#
#     print("Languages stored in TextConv.json under the 'Language' table.")
# else:
#     print(f"Failed to fetch languages. Status code: {response.status_code}")

#ToDO: Try to store the above languages in TinyDB and change the code to get input from users to enter the toLanguage and translate the content.
#ToDO: Store the API key in a config file or TinyDB
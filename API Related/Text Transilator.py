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


# :Translating the TEXT using GET
# :Response: {'message': "Endpoint '/translate' does not exist"}
# :If you're receiving a message like "Endpoint '/translate' does not exist" when attempting to convert a POST request to a GET request, it's possible that the API endpoint you are working with only supports the POST method. Not all APIs support both GET and POST for every endpoint.
# url = "https://text-translator2.p.rapidapi.com/translate"
#
# params = {
#     "source_language": "en",
#     "target_language": "id",
#     "text": "What is your name?",
# }
#
# headers = {
#     "X-RapidAPI-Key": "b3313c3760msh810678525cdff97p1eb563jsn701a8ffd6ba9",
#     "X-RapidAPI-Host": "text-translator2.p.rapidapi.com",
# }
#
# response = requests.get(url, params=params, headers=headers)
#
# print(response.json())




# :Get the list of Languages
import requests

url = "https://text-translator2.p.rapidapi.com/getLanguages"

headers = {
    "X-RapidAPI-Key": "b3313c3760msh810678525cdff97p1eb563jsn701a8ffd6ba9",
    "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

#ToDO: Try to store the above languages in TinyDB and change the code to get input from users to enter the toLanguage and translate the content.
#ToDO: Store the API key in a config file or TinyDB
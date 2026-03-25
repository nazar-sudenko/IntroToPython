import requests

response = requests.get("https://random-word-api.herokuapp.com/word")

data = response.json()

word = data[0]

first_letter = word[0]
last_letter = word[-1]
word_length = len(word)
mid_length = word_length - 2
dashes = "-" * mid_length



print(first_letter + dashes + last_letter)

import requests as re

#print(re.__version__)
print(re.get(url = 'https://www.google.com').text)

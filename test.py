import requests

url = 'https://www.baidu.com'

response = requests.get(url=url)
text = response.text
print(text)
response.close()

import requests

response = requests.get('http://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

print("That's how it all works...edit for github testing")

import requests
import itertools
import json
import os
from time import sleep

# Make a GET request to an API endpoint
#response = requests.get('http://yugiohprices.com/api/top_100_cards')
response = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php?attribute=divine')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Get the top 10 most expensive cards
    with open('divineAttributes.json', 'w') as f:
        json.dump(data, f)
 
else:
    print('Error:', response.status_code)
    

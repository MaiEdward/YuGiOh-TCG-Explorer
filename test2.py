import json
import random

with open('darkAttributes.json') as f:
    data = json.load(f)
    for i in range(10):
            card = random.choice(data['data'])
            print(card['name'])
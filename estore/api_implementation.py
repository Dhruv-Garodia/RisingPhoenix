import json
import requests


url = ''

input_data_for_model = {
    
    'product_id' : 5,
    'user_id' : 166,
    'rating' : 72,
    'time_stamp' : 19
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)



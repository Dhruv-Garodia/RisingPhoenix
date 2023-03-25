import json
import requests


url = 'http://127.0.0.1:8000/fed_prediction'

input_data_for_model = {
    
    'iid' : '0970407998' ,
    'uid' : 'A17HMM1M7T9PJ1' ,
    'r_ui' : 0,
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)

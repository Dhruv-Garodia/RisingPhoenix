import requests

# Set the API endpoint and secret key for the bin
endpoint1 = 'https://api.jsonbin.io/v3/b/641e7893c0e7653a05933364/latest'
secret_key = '$2b$10$JQjUv8ebz8Y4fcIJcOGCdeVYDe8c3d/K6SRydkrh68Bl2FFTQCW.i'
endpoint2 = 'https://api.jsonbin.io/v3/b/641e7893c0e7653a05933364'

# Make a GET request to retrieve the JSON data from the bin
headers = {
    'X-Master-Key': secret_key,
    'Content-Type': 'application/json'
}
response = requests.get(endpoint2, headers=headers)

# Parse the JSON data into a Python dictionary
data = response.json()
data['product7'] = "product9"
print(data)


# Access the employees object


# Make a PUT request to send the updated JSON data back to the bin

response = requests.put(endpoint2, json=data, headers=headers)
# response = requests.put(endpoint1, json=data, headers=headers)

# Check the response status code to ensure that the update was successful
if response.status_code == 200:
    print('JSON data updated successfully')
else:
    print('Error updating JSON data')

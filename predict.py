#While the server is running, you can modify 'data'and run the following code (python predict.py) to make a request to the server and get the prediction.

import requests

url = 'http://127.0.0.1:5000/predict'
headers = {'Content-Type': 'application/json'}
data = {'text': 'The earth is flat'}

response = requests.post(url, json=data, headers=headers)
print(response.json())

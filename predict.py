#While the server is running, you can modify 'data'and run the following code (python predict.py) to make a request to the server and get the prediction.

import requests

#url for using locally:
#url = 'http://127.0.0.1:5000/predict'

#url for using on AWS Elastic Beanstalk
url = 'http://pra5-ece444-env.eba-d45w3adj.us-east-2.elasticbeanstalk.com/predict'

headers = {'Content-Type': 'application/json'}
data = {'text': 'COVID-19 is a hoax'}

response = requests.post(url, json=data, headers=headers)
print(response.json())

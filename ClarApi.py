from clarifai.rest import ClarifaiApp
from clarifai.rest.client import Image
import requests
import pprint

app = ClarifaiApp(api_key='9d1135521f834d35969e93e8b94fb624')
model = app.models.get('general-v1.3')
urls = 'https://samples.clarifai.com/metro-north.jpg'
image = Image(url=urls)
#output is a dictionary
result = model.predict([image])
#data is a list
datas = result['outputs']
outputs = datas[0]
concepts = outputs['data']
data = concepts['concepts']
target = data[0]
pprint.pprint(target['name'])
from clarifai.rest import ClarifaiApp
from clarifai.rest.client import Image
import pprint

path = 'C:/Users/Nicholas/Desktop/Desk_tmp/1920x1080-Wallpaper-1.jpg'
print('In API')
app = ClarifaiApp(api_key='c0da642111c24a63b1988e0d14f30c71')
model = app.models.get('general-v1.3')
image = Image(file_obj=open(path, 'rb'))
#output is a dictionary
result = model.predict([image])
#data is a list
datas = result['outputs']
outputs = datas[0]
concepts = outputs['data']
data = concepts['concepts']
target = data[0]
pprint.pprint(target['name'])
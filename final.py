import io
import os
import google.cloud.vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\HP\\Desktop\\rahul\\lifcare\\VisionAPI\\vision.json"
# Create a Vision client.
vision_client = google.cloud.vision.ImageAnnotatorClient()

# TODO (Developer): Replace this with the name of the local image
# file to analyze. 
image_file_name ='C:\\Users\\HP\\Desktop\\rahul\\lifcare\\VisionAPI\\images\\med9.jpg'
with io.open(image_file_name, 'rb') as image_file:
    content = image_file.read()

# Use Vision to label the image based on content.
image = google.cloud.vision.types.Image(content=content)
response = vision_client.text_detection(image=image)

text_files = open("medicine.txt", "w", encoding='utf-8')
#import pdb; pdb.set_trace()
for text in response.text_annotations:
    text_files.write(text.description + " ")
text_files.close()

import json
import requests

file1 = open("medicine.txt", encoding='utf-8')
line = file1.read()# Use this to read file content as a stream:
words=line.split()
res=""
for r in words:
    res += r+ " "
parameters={"q":res, "size":1}
response = requests.get("http://sandbox.lifcare.in/v6/catalog/medicine/search", params=parameters)

# Print the content of the response (the data the server returned)
data=response.content.decode("utf-8")
data1=json.loads(data)
for item in data1["payload"]["content"]:
    name = item["name"]

import pandas as pd
import csv

index=0
my_csv = pd.read_csv('invoice.csv')
column = my_csv['ITEM NAME']
for r in column:
    if r==name:
        final_index=index
    index+=1

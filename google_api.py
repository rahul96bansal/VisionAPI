import io
import os
import google.cloud.vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\HP\\Desktop\\rahul\\lifcare\\VisionAPI\\vision.json"
# Create a Vision client.
vision_client = google.cloud.vision.ImageAnnotatorClient()

# TODO (Developer): Replace this with the name of the local image
# file to analyze. 
image_file_name ='C:\\Users\\HP\\Desktop\\rahul\\lifcare\\VisionAPI\\images\\med13.jpg'
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

#filenames = ['file1.txt', 'file2.txt', ...]
#with open('path/to/output/file', 'w') as outfile:
#    for fname in filenames:
#        with open(fname) as infile:
#            for line in infile:
#                outfile.write(line)
#print(res)
    #map[index]=str(text.description)
    #if index==1:
     #   print(str(text.description)
    #if str(text.description)=="Gelatin":
        #pass
       # print(map[index+1])

#from collections import Counter
#c = Counter(res.split())
#print(c.most_common())


import json
import requests
import pandas as pd
import io
import csv 

file1 = open("filteredtext.txt", encoding='utf-8')
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

print (type(data))
print (type(data1))
file2 = open("result.txt", "w", encoding='utf-8')
file2.write(data)
file2.close()

username=[]
for item in data1["payload"]["content"]:
    print (item["name"])
    res = item["salts"]
    for r in res:
        print(r["name"])
        username.append(r["name"])

with open('salt123.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',') # good point by @paco
    for row in reader:
        for field in row:
            if field == username[0]:
                print ("in the file")
            

#print(data1["name"])

    #my_dic={}
    #my_dict[]=item.get('payload').get('content').get('name')
#print (my_dict)
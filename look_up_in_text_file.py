import pandas as pd
import io
import json
from fuzzywuzzy import process

def get_matches(query, choices, limit=1):
    result = process.extract(query, choices, limit=limit)
    return result

file1 = open("filteredtext.txt", encoding='utf-8')
line = file1.read()# Use this to read file content as a stream:
data=line.split()

df = pd.read_csv('Invoice1.csv')
df_list=df['ITEM NAME'].tolist()
df_company=df['COMPANY'].tolist()
df_pack=df['PACK'].tolist()
df_batch=df['BATCH'].tolist()
df_expiry=df['EXPIRY'].tolist()
df_qty=df['QTY'].tolist()
df_mrp=df['MRP'].tolist()

initial=0
index=0
for r in df_list:
    res = get_matches(r, data)
    x=res[0][1]
    if x>=initial:
        initial=x
        ans= r #res[0][0]
        final_index=index
    index+=1
print ("Medicine Name:", ans)

print ("COMPANY:", df_company[final_index])
print ("PACK:", df_pack[final_index])
print ("BATCH:", df_batch[final_index])
print ("EXPIRY:", df_expiry[final_index])
print ("QTY:", df_qty[final_index])
print ("MRP:", df_mrp[final_index])

import json
import requests
parameters={"q":ans, "size":1}
response = requests.get("http://sandbox.lifcare.in/v6/catalog/medicine/search", params=parameters)

# Print the content of the response (the data the server returned)
data=response.content.decode("utf-8")
data1=json.loads(data)

username=[]
for item in data1["payload"]["content"]:
    print (item["name"])
    p=item["classification_code"]
    print (item["classification_code"])
    res = item["salts"]
    for y in res:
        print(y["name"])
        username.append(y["name"])
dic = {'Medicine Name': ans, 'classification_code': p, 'Salts': username[0], 'COMPANY': df_company[final_index],
'PACK': df_pack[final_index], 'BATCH': df_batch[final_index], 'EXPIRY': df_expiry[final_index], 
'QTY': df_qty[final_index], 'MRP': df_mrp[final_index]}
final=json.dumps(dic)
print (final)
file2 = open("result.txt", "w", encoding='utf-8')
file2.write(final)
file2.close()
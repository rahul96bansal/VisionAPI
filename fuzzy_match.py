import math 
import io 
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
def get_matches(query, choices, limit=1):
    result = process.extract(query, choices, limit=limit)
    return result
val=[]
string = {"Rs", "MFD", "No.", "EXP"}
index=0
file1 = open("filteredtext.txt", encoding='utf-8')
line = file1.read()# Use this to read file content as a stream:
data=line.split()
#text="M.R.P. R.s. 10.48 paracetamol medicine with mfd.09/2017 and B.No.2632723D7 and Exp.8/2017"
#data=text.split()

for pattern in string:
    res = get_matches(pattern, data)
    val.append(str(res[0][0]))
#print (val)
for word in val:
    count = 0
    for i in word:
        if i.isdigit():
            break
        count+=1
    if word[count:]=="":
        next_word =data[data.index(word) + 1]
        print (next_word)
    else:
        print (word[count:])


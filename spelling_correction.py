from textblob import TextBlob
file1 = open("medicine.txt", encoding='utf-8')
line = file1.read()# Use this to read file content as a stream:
words = line.split()
appendFile = open('corrected.txt',"w", encoding='utf-8')
for r in words:
    blob = TextBlob(r)
    appendFile.write(str(blob.correct())+" ")
    print (blob.correct())
appendFile.close()
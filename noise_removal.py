import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("medicine.txt", encoding='utf-8')
line = file1.read()# Use this to read file content as a stream:
words = line.split()

appendFile = open('filteredtext.txt',"w", encoding='utf-8')
for r in words:
    if not r in stop_words:
        appendFile.write(r+" ")
appendFile.close()

#for line in words:
#    if line.startswith("M.R.P.Rs."):
#        print(line[9:])
#    if line.startswith("B.No."):
#        print(line[5:])
#    if line.startswith("MFD."):
#        print(line[4:])
#    if line.startswith("EXP."):
#        print(line[4:])
#next_word =words[words.index("VOVERAN") + 1]
#print (next_word)
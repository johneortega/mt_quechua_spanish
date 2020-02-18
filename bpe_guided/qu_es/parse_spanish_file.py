import sys
import string
#### first read in the file and create a hashmap of all the words (dictionary)


print("Running Script ", sys.argv[0])
print("Text Filename:", sys.argv[1])
print("Suffix Filename:", sys.argv[2])
filename = sys.argv[1]
suffix_filename = sys.argv[2]
suffixes = []
glossary = {}
words_dict = {}
## load suffixes
with open(suffix_filename,'r') as sfh:
    for line in sfh:
        line = line.strip()
        suffixes.append(line)
with open(filename,'r') as fh:
    for line in fh:
        line = line.strip()
        words = line.split(' ')
        for word in words:
            if not word in string.punctuation and not word.isnumeric() and len(word) > 2: 
                words_dict[word]=True

for word, value in words_dict.items():
    newword = word[3:]
    newword = newword.lower()
    hassuffix = False
    for suffix in suffixes:
        #if newword.find(suffix) > -1:
        if suffix in newword:
            hassuffix = True
    if not hassuffix:
        glossary[word]=True
#print(words_dict)
for key,val in glossary.items():
    print(key)




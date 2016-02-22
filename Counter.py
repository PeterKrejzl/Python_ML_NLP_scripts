import pandas as pd
from pprint import pprint
import operator
import csv
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import word_tokenize


filename = '/Users/peterkrejzl/Documents/PHD/wikidump/anarchism.txt'
filename2 = '/Users/peterkrejzl/Documents/PHD/wikidump/wiki.en.text.txt'


cached_stop_words = stopwords.words("english")


i = 0
fdist = FreqDist()
with open(filename2, 'r') as fin:
    for word in word_tokenize(fin.read()):
        if word not in cached_stop_words:
            fdist[word] += 1
            i += 1
            if i % 50000 == 0:
                pprint(fdist)
            
        
sorted_x = sorted(fdist.items(), key=operator.itemgetter(1), reverse=True)[:50]
#pprint(sorted_x)

with open("fdist.csv", "wb") as fp:
    writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
    writer.writerows(sorted_x)
    
    
    
pprint(fdist)
print('Done')
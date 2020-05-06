import pandas as pn 
import spacy
import os 
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import multidict
nlp = spacy.load('en_core_web_sm')

words = [{}, {}, {}]

def read(path_):
    data = pn.read_csv(path_)
    data = data[["Translated_Review","Sentiment"]]
    data = data.dropna()

    return data

def getTags(text, sentimemt):
    doc = nlp(text)
    pos = 0 
    if sentimemt == "Neutral":
        pos = 1
    if sentimemt == "Negative":
        pos == 2
        print("entro")

    for token in doc:
        if not (token.tag_[0:2] == "NN" or token.tag_[0:2] == "VB" or token.tag_[0:2] == "JJ"):
            continue 
        if not token.lemma_ in words[pos].keys():
            words[pos][token.lemma_] = 0
        words[pos][token.lemma_] += 1
    return doc
    
def countingWords(data):
    for ind in data.index:
        getTags(data.iloc[ind]["Translated_Review"],data.iloc[ind]["Sentiment"] )
    

data = read("data.csv")
countingWords(data)
fullTermsDict = multidict.MultiDict()
for key in words[0]:
        fullTermsDict.add(key, words[0][key])
wordcloud = WordCloud().generate_from_frequencies(fullTermsDict)

image1 = wordcloud.to_image()
image1.show()

fullTermsDict = multidict.MultiDict()

for key in words[1]:
        fullTermsDict.add(key, words[1][key])
wordcloud = WordCloud().generate_from_frequencies(fullTermsDict)
image2 = wordcloud.to_image()
image2.show()

fullTermsDict1 = multidict.MultiDict()

for key in words[2]:
        fullTermsDict1.add(key, words[2][key])
wordcloud = WordCloud().generate_from_frequencies(fullTermsDict1)
image3 = wordcloud.to_image()
image3.show()

import pandas as pn 

def read():
    data = pn.read_csv("googleplaystore_user_reviews.csv")
    data = data[["Translated_Review", "Sentiment"]]
    data = data.dropna()
    data.to_csv("data.csv")
    return data

read()
import streamlit as st
import string
from nltk.stem.porter import PorterStemmer
import pickle

model = pickle.load(open('model.pkl','rb'))
tfidf = pickle.load(open('vectorizer.pkl','rb'))

ps = PorterStemmer()
f = open('english_stopwords.txt')
stopwords = f.read()
def preprocessing(text):
    text = text.lower()
    text = text.split()
    y = []
    for word in text:
        if word.isalnum():
            y.append(word)
    text = y[:]
    y.clear()
    for word in text:
        if word not in stopwords and word not in string.punctuation:
            y.append(word)
    return " ".join(y)

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

st.title('Email Spam Classifier')
email = st.text_area("Enter Email")
transformed_email = preprocessing(email)
final_email = stem(transformed_email)

if st.button("Predict"):
    x = tfidf.transform([final_email])
    result = model.predict(x)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

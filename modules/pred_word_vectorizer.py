# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:31:37 2020

@author: A789074
"""

from IPython.display import display


def cleaning(df):
  df.dropna(subset=['keyword'], inplace=True)

  df['clean'] = df['text'].copy()
  df['clean'] = df['clean'].str.lower()

  df.replace( {'clean': r'@\w+'},  {'clean': '@@@'} , regex=True, inplace=True )
  #df.replace( {'clean': r'#\w+'},  {'clean': '###'} , regex=True, inplace=True )
  df.replace( {'clean': r'#'},  {'clean': ''} , regex=True, inplace=True )

  df.replace( {'clean': r'https?:\/\/\S+'},  {'clean': 'http'} , regex=True, inplace=True )

  #df.replace( {'clean': r'[^#@a-zA-Z|\s]'},  {'clean': ' '} , regex=True, inplace=True )
  df.replace( {'clean': r'[^@a-zA-Z|\s]'},  {'clean': ' '} , regex=True, inplace=True )

  df.replace( {'clean': r'\s\w{1,2}\s'},  {'clean': ' '} , regex=True, inplace=True )
  df.replace( {'clean': r'^\w{1,2}\s'},  {'clean': ' '} , regex=True, inplace=True )
  df.replace( {'clean': r'\s\w{1,2}$'},  {'clean': ' '} , regex=True, inplace=True )
  return df


def lemmatizer(df):
  import nltk
  nltk.download('stopwords')
  from nltk.corpus import stopwords
  print(stopwords.words('english'))
  nltk.download('wordnet')
  my_stopwords = stopwords.words('english')

  from nltk.stem import PorterStemmer, WordNetLemmatizer
  stemmer = PorterStemmer()
  lemmar = WordNetLemmatizer()

  df["clean"] = df["clean"].apply( lambda txt: " ".join( [word for word in txt.split() if word not in my_stopwords] ))

  df["clean"]  =  df["clean"].apply( lambda txt: " ".join( [ lemmar.lemmatize(word) for word in txt.split() ] ))
  #df["clean"]  =  df["clean"].apply( lambda txt: " ".join( [ stemmer.stem(word) for word in txt.split() ] ))
  return df



def vectorizer(df):
  from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

  #vectorizer = TfidfVectorizer()
  vectorizer = CountVectorizer()

  matrix_words = vectorizer.fit_transform( df['clean'] )

  matrix_keywords = df["keyword"].str.get_dummies()

  matrix_keywords = matrix_keywords.to_numpy()
  #matrix_keywords = np_matrix_keywords * 100.0

  import numpy as np
  X_matrix = np.hstack( [matrix_keywords, matrix_words.toarray()] )
  X_matrix.shape

  from sklearn.model_selection import cross_val_score
  from sklearn.pipeline import make_pipeline
  from sklearn.linear_model import LogisticRegression
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import accuracy_score

  X = matrix_words
  #X = X_matrix
  y = df['target']

  X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42, stratify=y)

  print( 'X_train ', X_train.shape)
  print( 'y_train ', y_train.shape)
  print( 'X_test  ', X_test.shape)
  print( 'y_test  ', y_test.shape)

  from sklearn.naive_bayes import MultinomialNB

  model = MultinomialNB()
  model.fit(X_train, y_train)
  y_pred = model.predict(X)

  print('matrix shape', X.shape)
  print('y shape', y_pred.shape)

  import pandas as pd

  df = pd.concat( [ df, pd.Series( y_pred, name='y_pred', index=df.index) ] , join='inner', axis='columns')

  print('accuracy_score', round( accuracy_score( df['target'], df['y_pred'] ),  2))
  return df

def simple_vectorizer(df):
  from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

  #vectorizer = TfidfVectorizer()
  vectorizer = CountVectorizer()

  matrix_words = vectorizer.fit_transform( df['clean'] )

  matrix_keywords = df["keyword"].str.get_dummies()

  matrix_keywords = matrix_keywords.to_numpy()
  #matrix_keywords = np_matrix_keywords * 100.0

  import numpy as np
  X_matrix = np.hstack( [matrix_keywords, matrix_words.toarray()] )
  X_matrix.shape

  from sklearn.model_selection import cross_val_score
  from sklearn.pipeline import make_pipeline
  from sklearn.linear_model import LogisticRegression
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import accuracy_score

  return matrix_words





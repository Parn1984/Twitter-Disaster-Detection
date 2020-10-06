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

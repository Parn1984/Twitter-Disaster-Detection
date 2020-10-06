# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv("../data/disaster_tweets.csv")

print(df[df.text.str.contains('fire')])
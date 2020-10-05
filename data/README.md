# 'data'-Folder

## Files
README.md  
disaster_tweets.csv

### File Descriptions:

#### README.md
Markdown File containing this Text. Describes all Files within the 'data'-folder.

#### disaster_tweets.csv 
CSV File containing about 10.000 Tweets as reference to train/test any possible algorithem. This file contains a
 header line and following columns:
 
column   | Description
---------|-----------
id       | Tweet ID
keyword  | A keyword from that tweet (if known)
location | The location the tweet was sent from (if known)
text     | The text of a tweet
target   | Target (1 for disaster, 0 for false alert)
import pandas as pd
import json
import os
import time

#opening and loading teh file which is in json format

with open("trendpulse-SaiAkhilM/data/trends_20260404.json", "r") as file:
    data = json.load(file)
#print(data)
print(type(data))#checking the datatype of data if it is list of json we can directly conver into daftames 
#converting the json into df
df=pd.DataFrame(data)
print(f"{len(df)}number of rows loaded ")#printing numbe rof rows loaded 
##2 — Clean the Data 
print(f"list of non duplicate post id's  :{df[['post_id']].drop_duplicates()}")
#Duplicates — remove any rows with the same post_id
#Missing values — drop rows where post_id, title, or score is missing
df = df[
    df['post_id'].notna() & # we are including the rows where post_id is not null
    df['title'].notna() & # we are including the rows where title is not null
    df['score'].notna() &
    df['num_comments'].notna()
 # we are including the rows where title is not nul
]
#Data types — make sure score and num_comments are integers
df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)
print(f"datatype of 'score' is {df['score'].dtype} and  datatype of 'num_comments' is {df['num_comments'].dtype}")

# Low quality — remove stories where score is less than 5
df=df[df['score']>=5]
print(df.head())
#Whitespace — strip extra spaces from the title column
df['title'] = df['title'].str.strip().str.replace(r'\s+', ' ', regex=True)
#print(df.head())
# I'm verifying the whethwe the leadinf and ending spaces are removed as per teh requiremnt
print(df[df['title'].str.startswith(' ')])
print(df[df['title'].str.endswith(' ')])
#saving the cleaned data to a csv file
df.to_csv("trendpulse-SaiAkhilM/data/trends_clean.csv", index=False)
#printing number of rows inserted
print(f"{len(df)} number of rows are inserted")
#using group by to create categories and size to show how many stories are per category 
print(f"Stories per {df.groupby('category').size()}")
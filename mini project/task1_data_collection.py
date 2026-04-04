
import requests
from pprint import pprint
import os
import json
from datetime import datetime
import time

url="https://hacker-news.firebaseio.com/v0/topstories.json"
#end poind 1

#header as mentioned  in problem
headers = {"User-Agent": "TrendPulse/1.0"}

try:
    response=requests.get(url,headers= headers)#get req to url 
    response.raise_for_status() # knowing the status of the url 
    story_ids=response.json()#converting json data into list and storing  ids in a  variable  
except requests.exceptions.ConnectionError:#handling  connection  errors
    print("check connection")

except requests.exceptions.HTTPError as e: #handling  http   error
    print(f"HTTP error occured {e}")

story_ids2=story_ids[:500]# taking first 500 ids as per problem
print(f"received {len(story_ids2)} Ids ")

# using a counter dictionary to  accepts only 25 stories per category
category_count = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0
}

all_stories = []# empty list to store all the final stories

categories = {# assigingin all the title and key words as per the problem statemnt using key value pairs 
"technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
"worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
"sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
"science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
"entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

for i in story_ids2:
    url2=f"https://hacker-news.firebaseio.com/v0/item/{i}.json"# get req to url2 whicha has actual data for each id
    response=requests.get(url2,headers= headers)#get req to url 

    try:
        response.raise_for_status()#checking status
        data=response.json()

        # checking if data is available fir all ids if not it will continue without  raiging errors
        if data is None:
            print(f"response for {i} is null")
            continue

        #extracting the title filed form the dictionary
        title=data.get("title") 

        # if title is not present skipping that record
        if title is None:
            continue

        required_categories = None #using an empty variable to add a category to found categories

        #converting all the title into lower case 
        title_lower=title.lower()

        #accessing key and values to iterate to each title and key word
        for category,keyword_list in categories.items():
            #iterating to each keyword for  a specifired title
            for keyword in  keyword_list:
                #checking keyword is found
                if keyword in title_lower :
                    #after finding teh category assign it to the required category variable
                    required_categories = category 
                    break#breaking as soon the category is found as soon as the key word is identified

            # checking if we found category then only proceed
            if required_categories :

                # checking if that category has less than 25 records
                if category_count[required_categories]<25:

                    # creating dictionary for final output
                    story_dict = {
                        "post_id": data.get("id"),
                        "title": data.get("title"),
                        "category": required_categories,
                        "score": data.get("score"),
                        "num_comments": data.get("descendants"),
                        "author": data.get("by"),
                        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }

                    # adding to final list
                    all_stories.append(story_dict)

                    # incrementing that specific category count
                    category_count[required_categories]+=1

                    # when that category reached 25 waiting for 2 seconds
                    if category_count[required_categories]==25:
                        time.sleep(2)

                # to break the outer loop as soon as we  found  category  to avoid other iterations
                break

        # once all categories reach total 125 records stop the loop
        if sum(category_count.values())>=125:
            break

    except requests.exceptions.ConnectionError:#handling  exception errors
        print("check connection")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occured {e}")

# creating file name with date
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

#check if folder is existed or else create one 
if not os.path.exists("data"):
    os.makedirs("data")
# checking if file already exists
if os.path.exists(filename):
    print("file already exists so overwriting the data")

# overwrite data into json file 
with open(filename, "w") as f:
    json.dump(all_stories, f, indent=4)

# printing final output count
print(f"Collected {len(all_stories)} stories. Saved to {filename}")
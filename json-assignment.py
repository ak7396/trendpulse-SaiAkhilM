'''Task 1 — Build a JSON Structure
Create a Python dictionary representing a user profile with the following 
fields: name, age, email, is_active, and a list of skills. 
Convert it to a JSON string using json.dumps() and print it with proper indentation.

Task 2 — Parse an API Response
You receive the following mock API response as a JSON string:

{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}
Write Python code to parse this string and print:

The username
The score
A message: "User alex99 scored 87.5 points"
Task 3 — Handle Nested JSON
Given the nested JSON below, extract and print the city and zip code of the user:

{
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}
Then add a new key "country": "India" inside the address and print the updated JSON.

'''
#****************************** task 1 ******************************

import json #importing json module
user_profile={"name":"sai", #its a python dictinoary 
"age": 26,
"Email" :"skhil@gmail.com",
"is_active" : True,
"skills":["java","python","sql"]

}

json_format= json.dumps(user_profile,indent=2) 
#json.dumps will convert py dict to json format and storing the result in a variable and print it
print(json_format)

#****************************** task 2 ******************************
json_string='''{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}''' #api response should be in the string format only 
python_dict=json.loads(json_string) #loads will conver the or parse the json format into python dictinoary
print(python_dict["data"]["username"]) #unpacking each elemen of the json file
print(python_dict["data"]["score"])
print(f'"User {python_dict["data"]["username"]} scored {python_dict["data"]["score"]} points"')

#****************************** task 3 ******************************

nested_json='''{
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}'''

dicts_format=json.loads(nested_json)
print(f'{dicts_format["address"]["city"]} and {dicts_format["address"]["zip"]}') #printed state adn zip code
dicts_format["address"]["Country"]="India"# i have added a new key valeu pair insisde a diction whic h is address 
updated_json=json.dumps(dicts_format,indent=2) #converting dict into json file as requested and printing it 
print(updated_json)


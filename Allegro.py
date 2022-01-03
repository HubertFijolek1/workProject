import requests
import json
from operator import itemgetter
from collections import Counter
def connection():
    global username 
    username = str(input("enter any github username "))
    url = "https://api.github.com/users/{}/repos".format(username)
    requests.get(url)
    return requests.get(url)
response = connection()
while response.status_code == 404:
        print("Invalid username. Please enter a valid name")
        response = connection()
if response.ok:
    output = json.loads(response.text)
    i = numberOfStar = 0
    listOfLanguage=[]
    listoflanguagewithsize = []
    try:
        while output[i]['full_name'] != None:
            print(f'\nRepository name: {output[i]["full_name"]}, number of stars for this repository: {output[i]["stargazers_count"]}')
            numberOfStar += output[i]["stargazers_count"]
            listOfLanguage.append(output[i]['language'])
            listoflanguagewithsize.append((output[i]['language'], (output[i]['size'])))
            i+=1
    except IndexError:
        pass
    print("The total number of repositories is " + str(i))
    print(f"\nThe sum of the stars in all repositories is {numberOfStar} ")
    listCounter=Counter(listOfLanguage)
    mostCommon = listCounter.most_common()
    gooddict=dict(mostCommon)
    if list(gooddict.keys())[0] != None:
        print(f"\nThe most popular technology/language using by {username} is {list(gooddict.keys())[0]}")
    else:
        print(f"\nThe most popular technology/language using by {username} is {list(gooddict.keys())[1]}")

    sortedlist = sorted(listoflanguagewithsize, key = itemgetter(1), reverse = True)
    print(f'\nThe largest repo is {sortedlist[0][1]} kb ')



    
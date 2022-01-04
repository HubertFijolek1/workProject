import requests
import json
from operator import itemgetter
from collections import Counter
def connection():
    """
    We create a global variable that will be visible in the entire file, not only in the function.
    The user enters the username and if it is correct then we access to the content of the page
    using the github api and the requests library .


    """
    global username 
    username = str(input("enter valid github username: ")) # for example can be my github username: HubertFijolek1
    url = f"https://api.github.com/users/{username}/repos"
    return requests.get(url)

response = connection() #we make a connection

while response.status_code == 404:
    """
    if the username is incorrect, we repeat the query for the correct input of the correct name
    """
    print("Invalid username. Please enter a valid name")
    response = connection()

if response.ok:
    """
    If everything is alright then we deserialize a JSON document to a Python object and 
    create the  necessary variables
    """
    output = json.loads(response.text)
    i = numberOfStar = 0
    listOfLanguage=[]
    listoflanguagewithsize = []
    try:
        while output[i]['full_name'] != None:
            """
            in this loop we list each repository of a given user, the number of stars and
            add to special lists, which will later be used to determine the most frequently
            used technology/language and which repository takes the most space
            """
            print(f'\nRepository name: {output[i]["full_name"]}, number of stars for this repository: {output[i]["stargazers_count"]}')
            numberOfStar += output[i]["stargazers_count"]
            listOfLanguage.append(output[i]['language'])
            listoflanguagewithsize.append((output[i]['language'], (output[i]['size'])))
            i+=1
    except IndexError:
        print("\nThe total number of repositories is " + str(i))
    print(f"\nThe sum of the stars in all repositories is {numberOfStar} ")
    listCounter=Counter(listOfLanguage) #thanks to the counter library, we are able to easily count how often a given user has used a given technology
    mostCommon = listCounter.most_common() #we sort starting from the most frequently chosen technology
    gooddict=dict(mostCommon)

    """
    it happens that a user in a given repository only has data and does not use any technology,
    then we do not take it into account and this conditional instruction helps us in this
    """
    if list(gooddict.keys())[0] != None: 
        print(f"\nThe most popular technology/language using by {username} is {list(gooddict.keys())[0]}")
    else:
        print(f"\nThe most popular technology/language using by {username} is {list(gooddict.keys())[1]}")

    """
    We sort the list of tuples according to the second element of the tuple, which is the size of the file,
    the itemgetter function makes this task easier and faster for us
    """    
    sortedlist = sorted(listoflanguagewithsize, key = itemgetter(1), reverse = True)
    print(f'\nThe largest repo is {sortedlist[0][1]} kb ')



    
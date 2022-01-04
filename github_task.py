import requests
import json
from operator import itemgetter
from collections import Counter

def connection():
    """
    We create a global variable that will be visible in the entire file,
    not only in the function. The user enters the username and
    if it is correct then we access to the content of the page
    using the github api and the requests library .
    """
    global username
    # for example can be my github username: HubertFijolek1 
    username = str(input("enter valid github username: ")) 
    url = f"https://api.github.com/users/{username}/repos"
    return requests.get(url)

response = connection() #we make a connection

while response.status_code == 404:
    """
    if the username is incorrect, we repeat the query for 
    the correct input of the correct name
    """
    print("Invalid username. Please enter a valid name")
    response = connection()

if response.ok:
    """
    If everything is alright then we deserialize a JSON document to 
    a Python object and create the  necessary variables
    """
    output = json.loads(response.text)
    i = numberOfStar = 0
    list_of_language = []
    list_of_language_with_size = []

    try:
        while output[i]['full_name'] != None:
            """
            in this loop we list each repository of a given user,
            the number of stars and add to special lists, which will
            later be used to determine the most frequently
            used technology/language and which repository 
            takes the most space
            """
            print(f'\nRepository name: {output[i]["full_name"]}, number of stars for this repository: {output[i]["stargazers_count"]}')
            numberOfStar += output[i]["stargazers_count"]
            list_of_language.append(output[i]['language'])
            list_of_language_with_size.append((output[i]['language'], (output[i]['size'])))
            i+=1
    except IndexError:
        print("\nThe total number of repositories is " + str(i))
        print(f"\nThe sum of the stars in all repositories is {numberOfStar} ")

    """thanks to the counter library, we are able to easily count 
    how often a given user has used a given technology"""    
    listCounter=Counter(list_of_language)
    #we sort starting from the most frequently chosen technology 
    most_common1 = listCounter.most_common() 
    counter_dict=dict(most_common1)

    """
    it happens that a user in a given repository only has data and
    doesn't use any technology, then we don't take it into account and
    this conditional instruction helps us in this
    """

    if list(counter_dict.keys())[0] != None: 
        print(f"\nThe most popular technology/language using by {username} is {list(counter_dict.keys())[0]}")
    else:
        print(f"\nThe most popular technology/language using by {username} is {list(counter_dict.keys())[1]}")

    """
    We sort the list of tuples according to the second element of the
    tuple, which is the size of the file, the itemgetter function
    makes this task easier and faster for us
    """
        
    sorted_list = sorted(list_of_language_with_size, key = itemgetter(1), reverse = True)
    print(f'\nThe largest repo is {sorted_list[0][1]} kb ')



    
import requests
import json
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
    try:
        while output[i]['full_name'] != None:
            print(f'Repository name: {output[i]["full_name"]}, number of stars for this repository: {output[i]["stargazers_count"]}')
            numberOfStar += output[i]["stargazers_count"]
            i+=1
    except IndexError:
        pass
    print("The total number of repositories is" + str(i))
    print(f"The sum of the stars in all repositories is {numberOfStar} ")

    
    
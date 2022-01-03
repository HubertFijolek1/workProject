from github import Github

#My private token, please don't touch it ;)
g = Github('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') 

numberOfStars = 0
for repo in g.get_user().get_repos():
    repo=g.get_repo(f"HubertFijolek1/{repo.name}")
    print("Repository name" + repo.name + "\nthe number of stars for this repository " + str(repo.stargazers_count))
    numberOfStars+= repo.stargazers_count

print("Total stars for all repositories" + str(numberOfStars))
    




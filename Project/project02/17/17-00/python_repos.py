import requests

# https://api.github.com/ - API calls responder
# search/repositories - call method for search in repositories
# ? - we will pass an argument
# q - query
# = - begin specifying a query
# language:python - argument name and value
# &sort=stars - sort the result by stars

# make an api call and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
print("Status code:", r.status_code)

# store api response in a variable
response_dict = r.json()

# print keys in response dictionary
print(response_dict.keys())

print("Total repositories:", response_dict['total_count'])

# explore information about repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# examine first repository
repo_dict = repo_dicts[0]
print("\nFirst repository info:")
print("Keys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)


def pretty_print_key_value(key, value):
    print(f"{key:15}{str(value):>60}")


print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    pretty_print_key_value("Name:", repo_dict['name'])
    pretty_print_key_value("Owner:", repo_dict['owner']['login'])
    pretty_print_key_value("Stars:", repo_dict['stargazers_count'])
    pretty_print_key_value("Repository:", repo_dict['html_url'])
    pretty_print_key_value("Created:", repo_dict['created_at'])
    pretty_print_key_value("Updated:", repo_dict['updated_at'])
    pretty_print_key_value("Description:", repo_dict['description'])
    print()


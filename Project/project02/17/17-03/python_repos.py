import requests


def request_python_repositories():
    """Make an api call and return the response."""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    print("Sending the request.")
    r = requests.get(url, headers=headers)
    print("Status code:", r.status_code)
    return r


def get_repository_dictionaries(r):
    """Return the 'items' dictionary from api response which holds the repository items."""
    # store api response in a variable
    response_dict = r.json()
    # explore the api response
    print("Keys seen in response: ", response_dict.keys())
    print("Total repositories: ", response_dict['total_count'])
    # get the 'items' dictionary
    repo_dicts = response_dict['items']
    print("Repositories returned: ", len(repo_dicts))

    return repo_dicts


def pretty_print_key_value(key, value):
    print(f"{key:15}{str(value):>60}")


if __name__ == '__main__':
    r = request_python_repositories()
    repo_dicts = get_repository_dictionaries(r)
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

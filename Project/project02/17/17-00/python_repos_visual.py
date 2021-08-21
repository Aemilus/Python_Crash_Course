import requests

from plotly.graph_objs import Bar
from plotly import offline

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
repo_dicts = response_dict['items']

# process results
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    # x-axis: links for when clicking the name of the repo you will navigate to that repository
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f'<a href="{repo_url}">{repo_name}</a>'
    repo_links.append(repo_link)

    # y-axis: repo stars count
    repo_stars_count = repo_dict['stargazers_count']
    stars.append(repo_stars_count)

    # make the tooltips that you will get when hovering the mouse over a bar in the plot
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# make visualization
data_1 = {
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}
data = [data_1]

layout = {
    'title': "Most-Starred Python Projects on GitHub",
    'titlefont': {'size': 28},
    'xaxis': {
        'title': "Repository",
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': "Stars",
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename="data/python_repos.html")

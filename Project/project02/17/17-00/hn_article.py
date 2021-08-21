import requests
import json

# make an api call and store response
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url=url)
print(f"Status code: {r.status_code}")

# explore structure of data
response_dict = r.json()
readable_file = "data/readable_hn_data.json"
with open(readable_file, "w") as fh:
    json.dump(response_dict, fh, indent=4)

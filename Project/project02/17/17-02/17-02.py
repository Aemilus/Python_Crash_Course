"""
17-2. Active Discussions: Using the data from hn_submissions.py, make a bar
chart showing the most active discussions currently happening on Hacker
News. The height of each bar should correspond to the number of comments
each submission has. The label for each bar should include the submission’s
title and should act as a link to the discussion page for that submission.
"""

from operator import itemgetter
import requests
from plotly import offline

# make an api call and store response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url=url)
print("Response code: ", r.status_code)
submission_ids = r.json()

# process info about top 30 submissions to hacker news webpage
submission_dicts = []
for submission_id in submission_ids[:30]:
    # make a separate call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url=url)
    print(r.json())
    print(f"id: {submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    # build a dictionary for each article
    try:
        title = response_dict['title']
        hn_link = f"http://news.ycombinator.com/item?id={submission_id}"
        comments = response_dict['descendants']
    except KeyError as key_err:
        print(f"Skipping below dict because of {key_err}:\n{response_dict}")
        continue
    submission_dict = {
        'title': title,
        'hn_link': hn_link,
        'comments': comments,
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

title_links, comments_counts = [], []
for submission_dict in submission_dicts:
    # retrieve data
    title = submission_dict['title']
    hn_link = submission_dict['hn_link']
    comments_count = submission_dict['comments']
    # log to console the data retrieved
    print(f"\nTitle: {title}")
    print(f"Discussion Link: {hn_link}")
    print(f"Comments: {comments_count}")
    # save the data retrieved for plotting
    title_link = f'<a href="{hn_link}">{title}</a>'
    title_links.append(title_link)
    comments_counts.append(comments_count)

# console log the saved data
print("Title Links:\n", title_links, "\n")
print("Title Links:\n", comments_counts, "\n")

data_1 = {
    'type': 'bar',
    'x': title_links,
    'y': comments_counts,
}

data = [data_1]

layout = {
    'title': "Most active discussions on Hacker News",
    'xaxis': {'title': "Submissions"},
    'yaxis': {'title': "Comments"},
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename="hacker_news_submissions.html")

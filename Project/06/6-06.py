"""
6-6. Polling: Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

people = ["bob", "john", "phil", "laura", "jen", "tim", "edward"]

for person in people:
    if person in favorite_languages.keys():
        print("Hi {0}! Thank you for participating in our favorite programming language poll.".format(person.title()))
    else:
        print("Hi {0}, we invite you to participate in our favorite programming language poll.".format(person.title()))

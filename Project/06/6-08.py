"""
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
"""

rex = {
        "name": "rex",
        "kind": "dog",
        "owner": "emil"
    }

thomas = {
        "name": "thomas",
        "kind": "cat",
        "owner": "john"
    }

stella = {
        "name": "stella",
        "kind": "horse",
        "owner": "oana"
    }

ozzy = {
        "name": "ozzy",
        "kind": "parrot",
        "owner": "laura"
    }

pets = [rex, thomas, stella, ozzy]

for pet in pets:
    describe_pet = "{0} is a {1} and it's owner is {2}."
    name = pet["name"].title()
    kind = pet["kind"]
    owner = pet["owner"].title()
    print(describe_pet.format(name, kind, owner))

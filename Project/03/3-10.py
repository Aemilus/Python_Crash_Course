"""
3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
"""

print("{0:-^83}".format("   Countries   "))

countries = ["Romania", "Germany", "England", "France", "Italy", "Spain", "Sweden", "Portugal"]
print("Original list:")
print(countries)

len_countries = len(countries)
print("The list has {0} countries.".format(len_countries))

print("Reverse order of list:")
countries.reverse()
print(countries)
print("Reverse back the list:")
countries.reverse()
print(countries)

middle = len(countries) // 2 - 1
print("The country in middle of list is:", countries[middle])

print("First country on the list is:", countries[0])
print("Last country on the list is:", countries[len_countries - 1])

print("List of countries in alphabetical order:")
countries.sort()
print(countries)

print("List of countries in reverse alphabetical order:")
countries.sort(reverse=True)
print(countries)

print("Removing the 2nd country in the list..")
del countries[1]
print(countries)

country = "France"
print("Remove {0} from this list:".format(country))
countries.remove(country)
print(countries)

print("Remove last element in the list:")
countries.pop()
print(countries)

country = "Poland"
index = 2
print("Insert {0} on index {1}:".format(country, index))
countries.insert(index, country)
print(countries)

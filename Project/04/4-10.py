"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
• Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.
"""

million = [i for i in range(1, 1_000_001)]

print("The first three items in the list are:", million[:3])

middle = len(million) // 2 - 1
print("Three items from the middle of the list are:", million[middle-1:middle+2])

print("The last three items in the list are:", million[-3:])

"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename = "reasons.txt"

while True:
    reason = input("Why do you like programming?\n").strip()
    if reason.lower() in ["", "quit", "q", "no"]:
        break
    else:
        with open(filename, "a") as file:
            file.write(reason + "\n")

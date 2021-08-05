"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s
name in a variable called famous_person. Then compose your message
and store it in a new variable called message. Print your message.
"""

famous_person = "John Dewey"

message = '''\
"I believe that the school must represent present life-life as real and vital \
to the child as that which he carries on in the home, in the neighborhood, or on the playground."

\t--%s (My Pedagogic Creed)\
''' % famous_person

print(message)

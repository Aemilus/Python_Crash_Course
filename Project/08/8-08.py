"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""


def make_album(artist, album, tracks=0):
    """Returns a dictionary with info about a music album."""
    album_dict = {
        "artist_name": artist,
        "album_name": album
    }
    if tracks:
        album_dict["number_of_tracks"] = tracks

    return album_dict


print("Type 'quit' to exit.")
while True:
    print()
    artist_input = input("Artist name: ")
    if artist_input.lower() == "quit":
        break
    album_input = input("Album name: ")
    if album_input.lower() == "quit":
        break
    print(make_album(artist_input, album_input))

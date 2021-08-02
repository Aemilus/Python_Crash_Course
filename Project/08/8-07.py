"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
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


print(make_album("Vali Vijelie", "Sa iubesti doua femei", 17))
print(make_album("3rei Sud Est", "Cu capu-n nori"))
print(make_album(tracks=12, album="Elements of Life", artist="Tiesto"))

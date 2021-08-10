"""
14-5. Refactoring: Look for functions and methods that are doing more
than one task, and refactor them to keep your code organized and efficient.
For example, move some of the code in check_bullet_alien_collisions(),
which starts a new level when the fleet of aliens has been destroyed,
to a function called start_new_level(). Also, move the four separate
method calls in the __init__() method in Scoreboard to a method called
prep_images() to shorten __init__(). The prep_images() method could also
help check_play_button() or start_game() if you’ve already refactored
check_play_button().

note: Before attempting to refactor the project, see Appendix D to learn
how to restore the project to a working state if you introduce bugs
while refactoring.
"""
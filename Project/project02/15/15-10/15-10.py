"""
15-10. Practicing with Both Libraries: Try using Matplotlib to make a die-rolling
visualization, and use Plotly to make the visualization for a random walk. (You’ll
need to consult the documentation for each library to complete this exercise.)
"""


def die_rolling_visualization_using_matplotlib():
    import matplotlib.pyplot as plt
    from die import Die

    # make a 6 sided die
    die = Die()

    # roll the die 50.000 times
    rolls_count = 50_000
    results = [die.roll() for x in range(rolls_count)]

    # value on x-axis
    x_values = list(range(1, die.sides_count + 1))
    # values on y-axis
    y_values = [results.count(result) for result in range(1, die.sides_count + 1)]

    # plot settings
    fig, ax = plt.subplots()
    ax.set_title("Results of rolling a D6 die for %d times" % rolls_count)
    ax.set_xlabel("Result", fontsize=14)
    ax.set_ylabel("Count of Result", fontsize=14)
    plt.bar(x_values, y_values, width=0.4)

    plt.savefig('roll_D6_results.png')
    plt.show()


def random_walk_visualization_using_plotly():
    import plotly.express as px
    import pandas as pd
    from plotly import offline
    from random_walk import RandomWalk

    # create and fill random walk
    rw = RandomWalk()
    rw.fill_walk()

    # visualization
    data = {'x steps': rw.x_values, 'y steps': rw.y_values}
    df = pd.DataFrame(data)
    fig = px.scatter(df, x="x steps", y="y steps", title="Random walk", color=df.index)

    offline.plot(fig, filename='random_walk.html')


die_rolling_visualization_using_matplotlib()
random_walk_visualization_using_plotly()

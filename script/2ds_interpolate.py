import random
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")

# set type to make code clearer
Point = np.ndarray

# these are the edge points, the initial edges of that triangle
# we later select randomly from these
edge_points = [
    np.array([-1, -1]),
    np.array([0, 1]),
    np.array([1, -1]),
]


def compute_midpoint(point_1: Point, point_2: Point, distance: float) -> Point:
    return point_1 + (distance * (point_2 - point_1))


def select_edge_point(points: list[Point]) -> Point:
    # randomly selects one point from a list of points
    return random.choice(points)


def run_sierpinski_ifs(
    number_of_iterations: int,
    distance: float = 0.5,
    starting_point: Point = np.zeros(2),
) -> tuple[list[float], list[float]]:
    # create an empty list for recording the points
    point_history = list()
    # place the first point (0, 0) in the list
    point_history.append(starting_point)
    # run the IFS
    for iteration_index in range(number_of_iterations):
        last_point = point_history[iteration_index]
        edge_point = select_edge_point(edge_points)
        next_point = compute_midpoint(
            point_1=last_point,
            point_2=edge_point,
            distance=distance,
        )
        point_history.append(next_point)
    # split the list of points like so:
    # [[0,1], [2, 3], [4, 5]] -> [[0, 2, 4], [1, 3, 5]]
    x_points, y_points = list(zip(*point_history))
    x_points = [float(x) for x in x_points]
    y_points = [float(y) for y in y_points]
    # return the results
    return x_points, y_points


def run_and_plot(iterations: int = 1_000_000, distance: float = 0.5) -> None:
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot()
    size = min(1, 1000 / iterations + 0.005)
    ax.scatter(*run_sierpinski_ifs(iterations, distance), alpha=1, s=size)
    for side in ["top", "right", "bottom", "left"]:
        ax.spines[side].set_visible(False)
    ax.tick_params(axis="both", which="both", length=0)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.show()


if __name__ == "__main__":
    print("How many iterations do you want to run?")
    iterations = int(input("> "))
    print("What distance should the midpoint use?")
    distance = float(input("> "))
    run_and_plot(iterations, distance)

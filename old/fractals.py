import random
import numpy as np
from ifs.resources.simplex import SIMPLEX

# where point = the current point, and edges = the edge points
select = lambda point, edges: random.choice(edges)


# where A = point 1, B = point 2, and x = some parameter

# def sierpinski(n: int, dim: int, x: float):
#     midpoint = lambda A, B, x: ((A - B) * x) + B
#     e, p = SIMPLEX[dim], [np.zeros(dim)]
#     return [midpoint(p[i], random.choice(e), x) for i in range(n)]


def sierpinski(n: int, dim: int):
    e, p = SIMPLEX[dim], [np.zeros(dim)]
    for i in range(n):
        p.append(((p[i] + random.choice(e)) / 2))
    return p

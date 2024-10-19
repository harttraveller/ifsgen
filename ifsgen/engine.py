import numpy as np
from typing import Optional
from dataclasses import dataclass
from .types import Point


# todo: include methods to visualize fractal and compute stats/access state


@dataclass
class Fractal: ...


class IFS:
    def __init__(
        self,
        vertices,
        midpoint,
        selector,
        starting,
        iterations,
    ) -> None:
        self.vertices = vertices
        self.midpoint = midpoint
        self.selector = selector

    def run(self, iters: int, start: Optional[Point] = None) -> Fractal:
        # this should capture DivisionByZero or OverflowErrors and still return the points graphed leading up to the exceptions
        # there should be property or attribute on returned fractal that states whether it finished running, or the number of iters before failure
        ...

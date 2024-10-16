"""
This is the class to generate an IFS fractal. It requires:

* a set of verticies in n dimensions
* a function that accepts two points from n dimensional space, along with several parameters
* a ruleset for the application of the function
* some arbitrary starting point

? TODO: add recursion - allow IFS parameters to be informed by values generated in the IFS


"""

import numpy as np
from types import FunctionType
from typing import Dict


class Midpoint:
    def __init__(self, function):
        pass

    def set_params(self, **kwargs):
        self.params = kwargs

    def compute(self, A, B):
        pass


class Ruleset:
    def __init__(self, function):
        pass

    def set_params(self, **kwargs):
        self.params = kwargs

    def compute(self, A, B):
        pass


class IFS:
    def __init__(
        self,
        start: np.array,
        edges: np.array,
        midpoint: Midpoint,
        ruleset: Ruleset,
        feedback: bool = False,
    ) -> None:
        self.start = start
        self.edges = edges
        self.midpoint = midpoint
        self.ruleset = ruleset
        self.feedback = feedback

    def run(self, n: int) -> np.array:
        """
        Runs the IFS system.

        Params:
            n (int): The number of iterations to run the IFS system.
        """
        points = [self.start]
        selected_edges = list()
        for _ in range(n):
            # could potentially set new params here, forming internal feedback loop
            selected_edge = self.ruleset.compute(points, selected_edges, self.edges)
            selected_edges.append(selected_edge)
            computed_midpoint = self.midpoint.compute(points[-1], selected_edge)
            points.append(computed_midpoint)
        return points, selected_edges


class IFS:
    def __init__(
        self,
        edges: np.array,
        midpoint: FunctionType,
        midpoint_params: Dict,
        ruleset: FunctionType,
        ruleset_params: Dict,
        start_point: np.array = None,
    ) -> None:
        self.edges = edges
        self.dimensions = self.__resolve_dimensionality(edges)
        self.midpoint = midpoint
        self.midpoint_params = midpoint_params
        self.ruleset = ruleset
        self.ruleset_params = ruleset_params
        self.start_point = self.__set_default_start(start_point, self.dimensions)

    # Private Methods
    def __resolve_dimensionality(self, edges: np.array) -> int:
        """
        Resolves the number of dimensions the vertices are expressed in.
        ? Surely a better way to articulate.
        """
        return len(edges)

    def __set_default_start(self, start_point: np.array, dimensions: int) -> Dict:
        if start_point is None:
            return np.zeros(dimensions)
        else:
            return start_point

    # Run IFS
    def run(self, n: int) -> np.array:
        """
        Runs the IFS system.

        Params:
            n (int): The number of iterations to run the IFS system.
        """
        points = [self.start_point]
        selected_edges = list()
        for _ in range(n):
            selected_edge = self.ruleset(
                points, selected_edges, self.edges, **self.ruleset_params
            )
            computed_midpoint = self.midpoint(
                self.points[-1], selected_edge, **self.midpoint_params
            )
            points.append(computed_midpoint)
        return points

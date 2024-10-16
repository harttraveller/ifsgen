"""
Add: convergence checking
- For a given function, this *may* be dependent on dimensionality, ruleset,
  and the location of the start point.
"""

import numpy as np
import uuid
import string
import random
from typing import List
from pydantic import BaseModel
import math


class EdgeVerticesGenerator:
    "Need to be able to generate n-dimensional edge vertices"
    pass


class RulesetGenerator:
    """
    Need to be able to generate a ruleset (probably hardest generator)
    Question is how we encode if/else rules... Can do implicitly with math?
    """

    pass


class MidpointGenerator:
    def __init__(self, min_params, max_params) -> None:
        self.min_params = min_params
        self.max_params = max_params
        self.letters = list(string.ascii_lowercase)
        self.numbers = list(string.digits)

    def gen_func_name(self) -> str:
        "Generates a random function name"
        return str(uuid.uuid4()).replace("-", "_")

    def select_num_params(self) -> int:
        "Selects the number of parameters to go in the function"
        return np.random.randint(self.min_params, self.max_params)

    def gen_param_names(self, num_params: int) -> List[str]:
        "Generates list of parameter names"
        params = set()
        while len(params) < num_params:
            params.add(f"{random.choice(self.letters)}{random.choice(self.numbers)}")
        return params

    def run(self):
        function = "def "
        function = function + self.gen_func_name() + "A, B, "
        num_params = self.select_num_params()
        params = ", ".join(self.gen_param_names(num_params))
        function = function + params + "):"

"""
- Contains a midpoint equation generation class
- contains an operation handler class as a resource for midpoint generation class
- Also contains a class to load a midpoint equation as a function,
and

? Include tanh function, what other operations can be included?
"""


from typing import List
import numpy as np
from tqdm import tqdm
from numpy import sin, cos, tan
from math import log


class OperationHandler:
    def __init__(self, components: List[str], bias: List[float] = None) -> None:
        if bias is not None:
            assert len(components) == len(bias)
        self.components = components
        self.bias = bias
        self.operations = {
            "add": lambda components, bias: f"({' + '.join([np.random.choice(components, p=bias), np.random.choice(components, p=bias)])})",
            "subtract": lambda components, bias: f"({' - '.join([np.random.choice(components, p=bias), np.random.choice(components, p=bias)])})",
            "multiply": lambda components, bias: f"({' * '.join([np.random.choice(components, p=bias), np.random.choice(components, p=bias)])})",
            "divide": lambda components, bias: f"({' / '.join([np.random.choice(components, p=bias), np.random.choice(components, p=bias)])})",
            "exponent": lambda components, bias: f"({' ** '.join([np.random.choice(components, p=bias), np.random.choice(components, p=bias)])})",
            "logarithm": lambda components, bias: f"(log({np.random.choice(components, p=bias)}, {np.random.choice(components, p=bias)}))",
            "sin": lambda components, bias: f"(sin({np.random.choice(components, p=bias)}))",
            "cos": lambda components, bias: f"(cos({np.random.choice(components, p=bias)}))",
            "tan": lambda components, bias: f"(tan({np.random.choice(components, p=bias)}))",
        }

    def add(self):
        return self.operations["add"](self.components, self.bias)

    def subtract(self):
        return self.operations["subtract"](self.components, self.bias)

    def multiply(self):
        return self.operations["multiply"](self.components, self.bias)

    def divide(self):
        return self.operations["divide"](self.components, self.bias)

    def exponent(self):
        return self.operations["exponent"](self.components, self.bias)

    def logarithm(self):
        return self.operations["logarithm"](self.components, self.bias)

    def sin(self):
        return self.operations["sin"](self.components, self.bias)

    def cos(self):
        return self.operations["cos"](self.components, self.bias)

    def tan(self):
        return self.operations["tan"](self.components, self.bias)

    def random(self):
        return self.operations[np.random.choice(list(self.operations.keys()))](
            self.components, self.bias
        )


class EquationGenerator:
    def __init__(
        self, params: List[str], bias: List[float], layers: List[int], n: int
    ) -> None:
        self.params = params
        self.bias = bias
        self.layers = layers
        self.n = n
        self.string_params = ", ".join(params)

    def generate_list_of_components(
        self, params: List[str], bias: List[float], n: int
    ) -> List[str]:
        op = OperationHandler(params, bias)
        return [op.random() for _ in range(n)]

    def generate_equation(
        self, params: List[str], bias: List[float], layers: List[int]
    ):
        if layers[-1] != 1:
            layers.append(1)
        for i in layers:
            params = self.generate_list_of_components(params, bias, i)
            bias = None  # bias can only be applied on first round
        equation = params[0]
        equation = f"f({self.string_params}) = {equation}"
        return equation

    def generate_equations(
        self, params: List[str], bias: List[float], layers: List[int], n: int
    ):
        return [self.generate_equation(params, bias, layers) for _ in tqdm(range(n))]

    def run(self):
        return self.generate_equations(self.params, self.bias, self.layers, self.n)


class EquationLoader:
    def __init__(self) -> None:
        pass

    def load(self, equation):
        """
        example: "f(A, B, x, y) = ((log((A ** A), (A + x))) / (log((A ** A), (A + x))))"
        """
        front, back = equation.split(" = ")
        string_params = front[2:-1]
        func_lambda = "".join(["lambda ", string_params, ": "])
        function = eval(f"{func_lambda}{back}")
        variables = string_params.split(", ")
        return function, variables, equation


class Midpoint:
    def __init__(self, function, variables, equation) -> None:
        self.__validate(variables)
        self.function = function
        self.variables = variables
        self.equation = equation

    def __validate(self, variables):
        assert len(set(variables).intersection({"A", "B"})) == 2

    def set_params(self, **kwargs):
        self.params = kwargs

    def execute(self, A, B):
        return self.function(A, B, **self.params)

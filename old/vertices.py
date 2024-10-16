import numpy as np

SIMPLEX = {
    1: [np.array([-1]), np.array([1])],
    2: [
        np.array([-1 / 2, -np.sqrt(3) / 4]),
        np.array([0, np.sqrt(3) / 4]),
        np.array([1 / 2, -np.sqrt(3) / 4]),
    ],
    3: [
        np.array([np.sqrt(8 / 9), 0, -1 / 3]),
        np.array([-np.sqrt(2 / 9), np.sqrt(2 / 3), -1 / 3]),
        np.array([-np.sqrt(2 / 9), -np.sqrt(2 / 3), -1 / 3]),
        np.array([0, 0, 1]),
    ],
    4: [
        np.array([1 / np.sqrt(10), 1 / np.sqrt(6), 1 / np.sqrt(3), 1]),
        np.array([1 / np.sqrt(10), 1 / np.sqrt(6), 1 / np.sqrt(3), -1]),
        np.array([1 / np.sqrt(10), 1 / np.sqrt(6), -2 / np.sqrt(3), 0]),
        np.array([1 / np.sqrt(10), -np.sqrt(3 / 2), 0, 0]),
        np.array([-2 * np.sqrt(2 / 5), 0, 0, 0]),
    ],
}

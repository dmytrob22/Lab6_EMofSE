import numpy as np

class Line:
    def __init__(self, k: float, b: float, n: int):
        self.k = k
        self.b = b
        self.n = n
        self.x = np.arange(n + 10)
        self.y = self.k * self.x + self.b

    def get_points(self):
        return self.x, self.y

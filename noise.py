import numpy as np

class Noise:
    def __init__(self, std_dev: float):
        self.std_dev = std_dev

    def apply(self, y: np.ndarray) -> np.ndarray:
        noise = np.random.normal(0, self.std_dev, size=len(y))
        return y + noise

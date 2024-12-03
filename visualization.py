import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    @staticmethod
    def plot(x: np.ndarray, y_original: np.ndarray, y_noisy: np.ndarray, y_regression: np.ndarray):
        plt.figure(figsize=(10, 6))
        plt.plot(x, y_original, label="Original Line (y=kx+b)", color="blue", linewidth=2)
        plt.scatter(x, y_noisy, label="Noisy Data", color="red")
        plt.plot(x, y_regression, label="Regression Line (y=mx+c)", color="green", linestyle="--")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Linear Regression with Noisy Data")
        plt.legend()
        plt.grid(True)
        plt.show()

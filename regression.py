import numpy as np

class Regression:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.slope = None
        self.intercept = None

    def compute(self):
        """Compute slope and intercept manually using the least squares method."""
        # Calculate means of x and y
        mean_x = np.mean(self.x)
        mean_y = np.mean(self.y)

        # Calculate the numerator and denominator for the slope (m)
        numerator = np.sum((self.x - mean_x) * (self.y - mean_y))
        denominator = np.sum((self.x - mean_x) ** 2)

        # Compute slope (m) and intercept (b)
        self.slope = numerator / denominator
        self.intercept = mean_y - self.slope * mean_x

    def get_regression_line(self):
        """Get the y-values of the regression line."""
        if self.slope is None or self.intercept is None:
            raise ValueError("Regression coefficients have not been computed yet.")
        return self.slope * self.x + self.intercept

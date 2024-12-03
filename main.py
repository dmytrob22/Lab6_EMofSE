from line import Line
from noise import Noise
from regression import Regression
from visualization import Visualization

def get_user_input():
    """Gets and validates user input for N, k, and b."""
    try:
        N = int(input("Enter basic point number (N): "))
        k = float(input("Enter the slope of the line (k): "))
        b = float(input("Enter the intercept of the line (b): "))
        if N < 0:
            raise ValueError("N must be a non-negative integer.")
        return N, k, b
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def main():
    # Step 0: Get user input
    user_input = get_user_input()
    if not user_input:
        return  # Exit if input is invalid
    N, k, b = user_input
    std_dev = N / 5  # Standard deviation of noise

    # Step 1: Create original line
    line = Line(k=k, b=b, n=N)
    x, y_original = line.get_points()

    # Step 2: Add noise
    noise = Noise(std_dev=std_dev)
    y_noisy = noise.apply(y_original)

    # Step 3: Compute regression
    regression = Regression(x=x, y=y_noisy)
    regression.compute()
    y_regression = regression.get_regression_line()

    # Step 4.1: Output coefficients
    print(f"Original line: y = {k}x + {b}")
    print(f"Regression line: y = {regression.slope:.2f}x + {regression.intercept:.2f}")

    # Step 4.2: Visualize results
    Visualization.plot(x, y_original, y_noisy, y_regression)

if __name__ == "__main__":
    main()

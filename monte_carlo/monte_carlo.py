import random
import math

def in_unit_circle(N):
    """
    Computes the number of points M that fall inside the unit circle
    given N random points uniformly scattered in the first quadrant.

    Parameters:
    N (int): Number of random points to generate.

    Returns:
    int: The count of points inside the unit circle.
    """
    M = 0  # Counter for points inside the circle

    for _ in range(N):
        # Generate random x, y coordinates between 0 and 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        # Check if the point is within the unit circle
        if x**2 + y**2 <= 1:
            M += 1  # Increment counter if point is in the circle

    return M


def estimate_pi(N):
    """
    Estimates the value of π using the Monte Carlo method.

    Parameters:
    N (int): Number of random points to generate.

    Returns:
    float: The estimated value of π.
    """
    M = in_unit_circle(N)  # Get the count of points inside the circle
    return 4 * M / N  # Calculate π


def get_accuracy(N):
    """
    Computes the absolute difference between the estimated value of π
    and the exact value of π.

    Parameters:
    N (int): Number of random points to generate.

    Returns:
    float: The absolute difference between the estimated π and the exact π.
    """
    estimated_pi = estimate_pi(N)
    exact_pi = math.pi
    return abs(exact_pi - estimated_pi)  # Return the absolute difference


# Test the functions with different values of N
if __name__ == "__main__":
    test_values = [1000, 10000, 100000, 1000000]  

    for N in test_values:
        estimated_pi = estimate_pi(N)
        accuracy = get_accuracy(N)
        print(f"N: {N}, Estimated π: {estimated_pi}, Accuracy: {accuracy}")

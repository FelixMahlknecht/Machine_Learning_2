import matplotlib.pyplot as plt
import math

# (a) Define the function for the probability density of the normal distribution
def f(x, mu, sigma):
    return (1 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# (b) Create the lists of x and y values
def create_density_plot(mu, sigma):
    xs = [round(-5 + i * 0.1, 1) for i in range(101)]  # Generate x values from -5 to 5
    ys = [f(x, mu, sigma) for x in xs]  # Calculate corresponding y values
    return xs, ys

# (c) Plotting the graph
def plot_density(mu_values, sigma_values):
    plt.figure(figsize=(10, 6))  # Set the figure size
    
    for mu, sigma in zip(mu_values, sigma_values):
        xs, ys = create_density_plot(mu, sigma)
        plt.plot(xs, ys, label=f'μ={mu}, σ={sigma}')  # Plot each curve

    plt.title('Probability Density Function of Normal Distribution')
    plt.xlabel('x')
    plt.ylabel('f(x, μ, σ)')
    plt.axhline(0, color='black', lw=0.5, ls='--')  # x-axis line
    plt.axvline(0, color='black', lw=0.5, ls='--')  # y-axis line
    plt.grid()
    plt.legend()  # Show legend
    plt.show()

# (d) Try different values for μ and σ
mu_values = [1, 0, -1]  # Different means
sigma_values = [1, 2, 5]  # Different standard deviations

# (e) Plot multiple graphs with different μ and σ
plot_density(mu_values, sigma_values)

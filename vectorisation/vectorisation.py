import numpy as np
import timeit
import matplotlib.pyplot as plt

# Non-vectorized version
def non_vectorized_version(N):
    matrix = np.random.random((2, N))  # Create a 2xN matrix of random numbers
    count = 0
    for i in range(N):
        if matrix[0, i] + matrix[1, i] > 1:  # Element-wise condition
            count += 1
    return count

# Vectorized version
def vectorized_version(N):
    matrix = np.random.random((2, N))  # Create a 2xN matrix of random numbers
    M = np.sum(matrix > 1, axis=0)  # Element-wise condition using vectorization
    return np.sum(M)

# Test the two versions for similar accuracy
def test_accuracy(N):
    non_vec_count = non_vectorized_version(N)
    vec_count = vectorized_version(N)
    return non_vec_count == vec_count

# Measure execution time for different N values
N_values = [10, 100, 1000, 10000, 100000]
non_vectorized_times = []
vectorized_times = []

for N in N_values:
    non_vec_time = timeit.timeit('non_vectorized_version(N)', globals=globals(), number=10)
    vectorized_time = timeit.timeit('vectorized_version(N)', globals=globals(), number=10)
    
    non_vectorized_times.append(non_vec_time)
    vectorized_times.append(vectorized_time)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(N_values, non_vectorized_times, label='Non-Vectorized Version', marker='o')
plt.plot(N_values, vectorized_times, label='Vectorized Version', marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Execution Time (seconds, log scale)')
plt.title('Execution Time Comparison of Vectorized vs Non-Vectorized Version')
plt.legend()
plt.grid()
plt.show()

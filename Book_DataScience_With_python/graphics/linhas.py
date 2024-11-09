from matplotlib import pyplot as plt


varience = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

total_error = [x + y for x, y in zip(varience, bias_squared)]

xs = [i for i, _ in enumerate(varience)]

plt.plot(xs, varience, 'g-', label='varience')

plt.plot(xs, bias_squared, 'r-', label='bias^2')

plt.plot(xs, total_error, 'b:', label='total error')

plt.legend(loc=9)
plt.xlabel("complexidade do modelo")
plt.title("Between Polari x Varience")
plt.show()
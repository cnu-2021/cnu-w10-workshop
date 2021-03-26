import numpy as np
import matplotlib.pyplot as plt

# Task 1

# Define all values of a
a = np.array([2.9, 3.1, 3.5, 3.7], dtype = float)

# Prepare an array to store the solutions
x = np.zeros([4, 201])
x[:, 0] = np.random.rand(4)

# Iterate all four at the same time
for i in range(x.shape[1] - 1):
    x[:, i + 1] = a * x[:, i] * (1.0 - x[:, i])
    

# Plot the results
fig, ax = plt.subplots(len(a), 1, figsize = (8, 12))
for i in range(len(a)):
    ax[i].plot(x[i, :], "k")
    ax[i].set(xlim=[0, x.shape[1] - 1], ylim=[0, 1], xlabel=r"$n$", ylabel=r"$x_n$", title=f"a = {a[i]}")

plt.subplots_adjust(hspace = 0.5)
plt.show()


# Task 2

# Prepare the plot
fig, ax = plt.subplots()
ax.set(xlabel=r"$a$", ylabel=r"$x_n$")

# Initial value and coefficient a
x = np.random.rand(1)
avals = np.arange(2.5, 3.801, 0.025)

# Loop over values of a
for a in avals:
    # Iterate 100 times per value of a
    for i in range(100):
        x = a * x * (1.0 - x)
        
        # Plot the point
        ax.plot(a, x, 'o', color=[0.1]*4, markersize=2)

plt.show()

# We can see bifurcations happening at certain values of a, which seem to get closer
# and closer together. In many cases, for a given a, the solution seems to periodically
# end up cycling around 2, then 4, then 8 values, etc. (with increasing a). This corresponds
# to the results from Task 1, where for different values of a, we seem to observe some
# periodicity/cycling between distinct values.



# Bonus task
# Adapted from cobweb.py

pause_time = 0.1
a = 3.5

#  Iteration function
def G(x):
   return a * x * (1 - x)

# Initial guess and number of iterations
x0 = np.random.random(1)
kmax = 100

# Plot y=x and y=G(x)
fig, ax = plt.subplots(figsize=(10, 6))

xmin, xmax = 0, 1
x = np.linspace(xmin, xmax, 500)
ax.plot(x, x, 'b-', label=r'$y = x$')
ax.plot(x, G(x), 'r-', label=r'$y = G(x)$')
ax.set(xlim=[xmin, xmax], ylim=[xmin, xmax])

plt.ion()
plt.show()
plt.pause(pause_time)

# Iterate
for k in range(kmax):
    # Fixed point iteration
    x_new = G(x0)
    
    # Draw cobweb diagram
    ax.plot([x0, x0], [x0, x_new], 'g', alpha=0.2, marker='.')
    plt.pause(pause_time)
    
    ax.plot([x0, x_new], [x_new, x_new], 'g', alpha=0.2, marker='.')
    plt.pause(pause_time)
    
    k += 1
    x0 = x_new


# This also corresponds to observations from Task 2. For instance, at a=3.5,
# we clearly observe that the logistic map eventually settles to a cycle
# between 4 points, corresponding to the 4 distinct points seen at a=3.5
# in the graph from Task 2.

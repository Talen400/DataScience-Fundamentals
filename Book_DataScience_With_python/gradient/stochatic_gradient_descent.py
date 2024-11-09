import gradient as g
import random

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0 = 0.01):
    data = zip(x, y)
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float('inf')
    interations_with_no_improvement = 0

    while interations_with_no_improvement < 100:
        value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data)
    if value < min_value:
        min_theta, min_value = theta, value
        interations_with_no_improvement = 0
        alpha = alpha_0
    else:
        alpha *= 0.9
    
    for x_i, y_i in in_random_order(data):
        gradient_i = gradient_fn(x_i, y_i, theta)
        theta = g.vector_subtract(theta, scalar_multiply(alpha, gradient_i))
    return min_theta
from collections import Counter
import math as math

def mean(x):
    """
    Calculate a mean of a number list:

    Parameters:

    x (list of float): The list of numbers

    Returns:
    a float (The mean of the numbers in the list)

    """
    return sum(x) / len(x)

def median(v):
    """
    Calculates the median of a list of numbers

    Parameters:
    v (list of float): The list of numbers.

    Returns:
    float: The median of the numbers
    """
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return(sorted_v[lo] + sorted_v[hi])/2

def mode(x):
    """
    Calculates the mode(s) of a list of numbers

    Parameters:
    x (list of float): The list of numbers

    Returns:
    list of float: A list with the mots frequent number(s)
    """
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

def quantile(x, p):
    """
    Calculates the p-th quantile of a list of numbers

    Parameters:
    x (list of float): The list of numbers.
    p (float): The percentile (a value between 0 and 1).
    
    Returns: 
    float: The p-th quantile of the list
    """
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def data_range(x):
    """
    Calculates the range of a list of numbers (difference between the maximum and minimum values)

    Parameters:
    x (list of float): The list of numbersw.

    Returns:
    float: The diffwerence between the maximum and minimum values.
    """
    return max(x) - min(x)

# -----------------Vectors------------------------------
def dot(v, w):
    """
    Calculates the dot product of two vectors.

    Parameters:
    v (list of float): The first vector.
    w (list of float): The second vector.

    Returns:
    float: The dot product of the two vectors.w
    """
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """
    Calculates the sum of squares of the components of a vector.

    Parameters:
    v (list of float): The vewctor.

    Returns:
    float: The sum of squares of thew vector's components.
    """
    return dot(v, v)

# -----------------------------------------------

def de_mean(x):
    """
    Centers the data by subtracting the mean from each data point.

    Parameters:
    x (list of float): The list of numbers.

    Returns:
    list of float: A list of the centered data.
    """
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """
    Calculates the varience of a list of numbers.

    Parameters:
    x (list of float): the list of numbers

    Returns:
    float: The varience of the numbers in the list.
    """
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations)/(n-1)

def stardard_deviation(x):
    """
    Calculates the standard deviation of a list of numbers.

    Parameters:
    x (list of float): The list of numbers.

    Returns:
    float: The standard deviation of wthe numbers in the list.
    """
    return math.sqrt(variance(x))

def covarience(x, y):
    """
    Calculates the varience between two values
    
    Parameters:
    x (list of float): The first list of numbers.
    y (list of float): The second list of numbers.

    Returns:
    float: The covarience
    """
    n = len(x)
    return dot(de_mean(x), de_mean(y))/(n-1)

def correlation(x, y):
    """
    Correlation divides two standard deviations of two values

    parameters:
    x (list of float): The first list of numbers
    y (list of float): The second list of numbers

    return:
    Covariance or zero, if no amplitude
    """

    stdev_x = stardard_deviation(x)
    stdev_y = stardard_deviation(y)

    if stdev_x > 0 and stdev_y > 0 :
        return covarience(x, y)/stdev_x/stdev_y
    else:
        return 0
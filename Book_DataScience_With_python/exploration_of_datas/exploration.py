from matplotlib import pyplot as plt
import random
import all_forms as af
from collections import Counter
import math


def bucketize(point, bucket_size):

    """reduza o ponto para o próximo múltiplo mais baixo de bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):

    """agrupa os pontos e conta quantos em cada bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):

    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

random.seed(0)

uniform = [200 * random.random() - 100 for _ in range(1000)]

normal = [57 * af.inverse_normal_cdf(random.random())
          for _ in range(10000)]

plot_histogram(uniform, 10, "Histograma de Uniform")


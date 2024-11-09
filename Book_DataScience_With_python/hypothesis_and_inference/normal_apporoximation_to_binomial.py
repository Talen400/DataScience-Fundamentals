import math
import all_forms as af

def normal_approximation_to_binomial(n, p):

    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

normal_probability_below = af.normal_cdf

def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - af.normal_cdf(lo, mu, sigma)

def normal_probability_between(lo, hi, mu=0, sigma=1):
    return af.normal_cdf(hi, mu, sigma) - af.normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    return af.inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    return af.inverse_normal_cdf(1 - probability, mu=0, sigma=1)

def normal_two_sided_bouds(probability, mu=0, sigma=1):

    tail_probability = (1 - probability) / 2

    upper_bound = normal_upper_bound(tail_probability, mu, sigma)

    lower_bound = normal_lower_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

"""
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

print(f"mu_0= {mu_0}, sigma_0 = {sigma_0}")

h_0 = normal_two_sided_bouds(0.95, mu_0, sigma_0)

print(f"h0 : {h_0}")

lo, hi = normal_two_sided_bouds(0.95, mu_0, sigma_0)

mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability

print(f"power: {power}")

"""
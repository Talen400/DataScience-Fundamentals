import math
import random
import normal_apporoximation_to_binomial as natb
import all_forms as af

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        return 2 * natb.normal_probability_above(x, mu, sigma)
    else:
        return 2 * natb.normal_probability_below(x, mu, sigma)
    
extreme_value_count = 0

for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else 0
                    for _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1

print (extreme_value_count/100000)

mu_0, sigma_0 = natb.normal_approximation_to_binomial(1000, 0.5)

print(two_sided_p_value(531.5, mu_0, sigma_0))

upper_p_value = natb.normal_probability_above
lower_p_value = af.normal_cdf

print(upper_p_value(524.5, mu_0, sigma_0))

print(upper_p_value(526.5, mu_0, sigma_0))
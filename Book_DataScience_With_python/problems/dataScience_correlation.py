from matplotlib import pyplot as plt
import general_trends_library as gtl

num_friends1 = [ 55,32,60,93,28,33,78,63,44,5,
                54,64,77,11,46,10,55,94,39,71,
                31,67,15,65,9,70,5,37,36,19,
                75,81,11,89,36,85,16,40,33,34,
                16,80,25,65,51,17,39,35,39,82]

daily_minutes = [5,12,2,6,13,7,12,1,3,7,
                2,5,11,5,15,8,13,7,11,6,
                6,15,11,3,1,6,12,1,13,14,
                9,2,1,8,14,6,7,1,8,9,
                1,7,11,15,7,11,9,5,2,12]

outlier = num_friends1.index(max(num_friends1)) # value discrepant

num_friends1_good = [x
                    for i, x in enumerate(num_friends1)
                    if i != outlier]
daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

print(f"correelation: {gtl.correlation(num_friends1_good, daily_minutes_good)}") # correlation < -0.25 = weakness



plt.scatter(num_friends1, daily_minutes)
plt.axis([0, 105, 0, 16])
plt.xlabel("friends")
plt.ylabel("minutes")
plt.show()
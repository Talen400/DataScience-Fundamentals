"""

Learning teorem of probality: 
P(E, F) = P(E)P(F) => inconditional
P(E|F) = P(E, F)/P(F) => conditional 
 
This script is a problem if conditional probability about boy or girl.

Whats a probality a event "two girl" (B) be condicionality by "older kid is a girl"(G)?

P(B|G) = P (B, G)/P(G) = P (B)/ P (G) = 1/2

But what is probality when least a kid is a girl? (L)

P (B|L) = P(B,L)/P(Ç) = P (B)/ P(L) = 1/3

And this script respond this:

values:     P (B|G) = P(both | older)
            P (B|L) = P(both | either)

"""
import random

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl" :
        both_girls += 1
    if older == "girl" or younger == "girl" :
        either_girl += 1
print("P(both | older):", both_girls / older_girl)
print("P(both | either:)", both_girls / either_girl)
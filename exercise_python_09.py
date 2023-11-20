# 9) Given the number x (no matter if integer or float) compute and print out the greatest integer k
# such that k 2 is less than x.

import math

x = float(input("Inserisci numero\n"))
k = int(math.sqrt(x))
print(k)

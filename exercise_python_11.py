# 11) Given a float number x compute and print put the minimum integer value z such that x<z.
# (be careful on the case of negative values!)

import math

x = float(input("Inserisci un numero decimale x: "))
z = math.floor(x) if x >= 0 else math.ceil(x)
print(z)


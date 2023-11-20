"""

10) Given three numbers x,y and z (no matter if integer or float) compute and print out the
maximum, the minimum and the median of the three.


Dati tre numeri x, y e z (indipendentemente che siano interi o decimali), 
calcola e stampa il valore massimo, il valore minimo e la mediana tra i tre.

"""
from statistics import median

x_value = float(input("Inserisci il valore di x: "))
y_value = float(input("Inserisci il valore di y: "))
z_value = float(input("Inserisci il valore di z: "))
    
value_max = max(x_value, y_value, z_value)           #valore MAX
value_min = min(x_value, y_value, z_value)           #valore MIN
value_median = median([x_value, y_value, z_value])   #valore MEDIAN

print(f"Il valore MASSIMO dei 3 valori inseriti e': {value_max}")
print(f"Il valore MINIMO dei 3 valori inseriti e': {value_min}")
print(f"Il valore MEDIANO dei 3 valori inseriti e': {value_median}")

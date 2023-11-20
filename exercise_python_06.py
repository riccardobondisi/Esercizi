"""

6) Given two numbers x and y (no matter if integer or float) compute and print out how many times
x has to be doubled to get a value that exceeds y.


Dati due numeri x e y (indipendentemente che siano interi o decimali), 
calcola e stampa quante volte x deve essere raddoppiato per ottenere un valore che superi y.

"""

def doubled(x, y):
    count = 0
    while x < y:
        x *= 2
        count += 1
    return count

x_value = float(input("Inserisci il valore di x: "))
y_value = float(input("Inserisci il valore di y: "))

result = doubled(x_value, y_value)
print(f"x deve essere raddoppiato {result} volta/volte per ottenere un valore che superi y.")
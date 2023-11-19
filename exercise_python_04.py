"""

4) Given two numbers x and y (no matter if integer or float) compute and print out how many times
y can be substracted from x before x turns to be zero or negative. Of course do no use the “/” or
the “//” Python operator!

Dati due numeri x e y (indipendentemente che siano interi o decimali), 
calcola e stampa quante volte y può essere sottratto da x prima che x 
diventi zero o negativo. Naturalmente, non utilizzare l'operatore "/" o "//" in Python!

"""


def sottrazione(x, y):
    count = 0
    while x > 0:
        x -= y
        count += 1
    return count

x_value = float(input("Inserisci il valore di x: "))
y_value = float(input("Inserisci il valore di y: "))

result = sottrazione(x_value, y_value)
print(f"y puo' essere sottratto da x {result} volte prima che x diventi zero o negativo.")
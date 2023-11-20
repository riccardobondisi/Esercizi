"""

4a. Write a function that given an integer N returns the list of all of its proper divisors
Example: 18 → [1,2,3,6,9]
(hint: k is a proper divisor of N if N%k==0, you may use brute force to find all of them and try to
divide N by k=1,up to k=N/2 and checking the remainder)

4b. Write a function that given a list of integers L returns a dictionary whose keys are the 
integers in L and whose values are the lists of their proper divisors.
Example: [5,18,42]→ {5:[1,5], 18:[1,2,3,6,9],42:[1,2,3,6,7,14,21]}


4a. Scrivi una funzione che, dato un numero intero N, restituisca la lista di tutti 
i suoi divisori propri.
Esempio: 18 → [1, 2, 3, 6, 9]
(suggerimento: k è un divisore proprio di N se N%k==0, puoi utilizzare la forza 
bruta per trovarli tutti e provare a dividere N per k=1, fino a k=N/2 verificando il resto)

4b. Scrivi una funzione che, dato un elenco di numeri interi L, restituisca un dizionario 
le cui chiavi sono gli interi in L e i cui valori sono le liste dei loro divisori propri.
Esempio: [5, 18, 42] → {5: [1, 5], 18: [1, 2, 3, 6, 9], 42: [1, 2, 3, 6, 7, 14, 21]}

"""

#4a.
def proper_divisors(N):
    divisors = [i for i in range(1, N//2 + 1) if N % i == 0]     #list comprehension  #range(1, n//2 + 1) crea un iterabile che va da 1 fino alla metà di n inclusa. Questo è fatto per evitare di includere divisori duplicati, poiché i divisori oltre la metà di n sarebbero già inclusi nella parte inferiore di questa sequenza.
    return divisors

num = 18
result = proper_divisors(num)
print(f"I divisori propri di {num} sono: {result}")


#4b.
def proper_divisors_dict(L):
    result_dict = {}
    for num in L:
        result_dict[num] = proper_divisors(num)     # [5, 18, 42] → {5: [1, 5], 18: [1, 2, 3, 6, 9], 42: [1, 2, 3, 6, 7, 14, 21]}
    return result_dict
    
lst = [5, 18, 42]
result_dict = proper_divisors_dict(lst)
print(f"I divisori propri per ciascun numero in {lst} sono: {result_dict}")
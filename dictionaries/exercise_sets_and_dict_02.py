"""

Laboratory on Sets and Dictionaries

2. Write a function that given two strings S1 and S2 return the list, sorted in alphabetical order, of
all the characters that appear in both strings.
Example: S1=”peace”, S2=”patience” → [“a”,”c”,“e”,”p”]
Hint: from the strings obtain two sets of characters and then compute the intersection.


Scrivi una funzione che, dato due stringhe S1 e S2, restituisca la lista, 
ordinata in ordine alfabetico, di tutti i caratteri che compaiono in entrambe le stringhe.
Esempio: S1="peace", S2="patience" → ["a","c","e","p"]
Suggerimento: dalle stringhe ottieni due insiemi di caratteri e poi calcola l'intersezione.

"""
def intersection_characters(s1, s2):
    # ottengo gli insiemi dei caratteri da entrambe le stringhe
    set_s1 = set(s1)
    set_s2 = set(s2)
    
    # Calcolo l'intersezione degli insiemi
    intersection_chars = sorted(list(set_s1.intersection(set_s2)))
   
    return intersection_chars

string1 = "Francesco"
string2 = "Davide"

result = intersection_characters(string1, string2)
print(result)  
print(type(result)) #list
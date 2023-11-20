"""

8) Given an integer k compute and print out the truth value of the statement “k is a multiple of 7
and 11 but it is not a multiple of 13”.


Dato un numero intero k, calcola e stampa il valore di verità dell'affermazione 
"k è un multiplo di 7 e 11, ma non è un multiplo di 13".

"""

def check_multiples(k):
    #Verifico se k è multiplo di 7, 11 e non è multiplo di 13
    is_multiple_of_7_and_11 = (k % 7 == 0) and (k % 11 == 0)
    is_not_multiple_of_13 = k % 13 != 0
    
    return is_multiple_of_7_and_11 and is_not_multiple_of_13

k_value = int(input("Inserisci il valore di k: "))

result = check_multiples(k_value)
print(f"Il risultato dell'affermazione è: {result}")  #77 è multiplo di 7, 11 e non è multiplo di 13
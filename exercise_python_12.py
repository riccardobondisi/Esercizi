"""

12) Write code to read an integer in binary code (example ob111011) and prints out the value of the
number in decimals. You may use (but are not obliged to) any built-in function of Python, but your
code should not “crash” if the user inputs a badly formed string.


Scrivi del codice per leggere un numero intero in codice binario (ad esempio ob111011) 
e stampa il valore del numero in decimale. Puoi utilizzare (ma non sei obbligato a farlo) 
qualsiasi funzione incorporata di Python, ma il tuo codice non dovrebbe "bloccarsi" 
se l'utente inserisce una stringa malformata.

"""

#Output: 0b111011
def binary_to_decimal(binary_str):
    try:
        decimal_value = int(binary_str, 2)  #2 specifica che la stringa binary_str è in base 2 (binaria). Quindi, la funzione int() interpreta la stringa come un numero binario e restituisce l'equivalente decimale.
        return decimal_value
    except ValueError:
        print("Input non Valido. Assicurati di inserire un numero binario corretto!")
        return None
    
binary_input = input("Inserisci un numero binario (es. 0b111011): ")
decimal_result = binary_to_decimal(binary_input)

if decimal_result is not None:
    print(f"Il valore decimale del numero binario {binary_input} e': {decimal_result} ")

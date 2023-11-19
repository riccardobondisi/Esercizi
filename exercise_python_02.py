"""

2) Given a string s obtain and get printed out a new string s2 such that every character of the first
string is repeated twice in s2.

Data una stringa s, ottieni e stampa una nuova stringa s2 in cui ogni 
carattere della prima stringa è ripetuto due volte in s2.

es. 
s = "abc" => s2 = "aabbcc"

"""


s = "abc"
s2 = "".join([letter * 2 for letter in s])
print("La stringa risultante e': ", s2)
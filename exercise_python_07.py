# 7) Given an integer k compute and print out the truth value of the statement “k is a multiple of 7
# but it is not a multiple of 11”.

k = int(input("Inserisci il numero da controllare\n"))
result = k % 7 == 0 and k % 11 != 0
if(result):
    print("{} è multiplo di 7 ma non di 11".format(k))
else:
    print("{} non è multiplo di 7".format(k))

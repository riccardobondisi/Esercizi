# 3. Write a function that given a string S creates a dictionary whose keys are the characters from the
# string and the values the number of their occurrences.
# Example: S=”peace and love”→ {“p”:1, ”e”:3, ”a”:2, ”c”:1, ”n”:1, ”d”:1, ”l”:1, ”o”:1, ”v”:1}

def occurencies(S):
    keys=set(S[::1])
    D={}
    for key in keys:
        D[key]=S.count(key)
    return(D)

print(occurencies("peace and love"))
# 1. Write a function that given a string S and and integer k>0 generates a set M whose elements are
# all the substrings of length k of S.
# Example: S=”mamma mia”, k=2 → {“ma”,”am”,”mm”,”a “,” m”,”mi”,”ia”}

def fun_substring(s,k):
    M=set()
    for i in range(len(s)-k+1):
        substring=s[slice(i,i+k)]
        M.add(substring)
    return M

print(fun_substring("mamma mia",2))
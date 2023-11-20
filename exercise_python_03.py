# 3) Given two strings s and w print out the shortest string of the two or, if they have the same lenght
# print a message saying “a tie!”

def shortest_string(s, w):
    len_s = len(s)
    len_w = len(w)

    if len_s < len_w:
        print("Shortest string:", s)
    elif len_w < len_s:
        print("Shortest string:", w)
    else:
        print("It's a tie!")

# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

shortest_string(string1, string2)

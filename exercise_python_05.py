# 5) Given a string made of only one character s and a longer string w, compute and print out how
# many times character s occurs within w.

def count_occurrences(character, longer_string):
    # Use the count() method to count occurrences
    occurrences = longer_string.count(character)
    return occurrences

# Example usage:
s = input("Enter the character s: ")
w = input("Enter the longer string w: ")

result = count_occurrences(s, w)
print(f"The character '{s}' occurs {result} times in the longer string.")

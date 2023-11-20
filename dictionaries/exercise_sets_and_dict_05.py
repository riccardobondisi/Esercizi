# 5. The following is a table of the RGB component of some digital colors
# Color name R G B
# Cyan 0 255 255
# Pink 255 0 255
# Yellow 255 255 0
# Silver 128 128 128
# Ivory 225 204 79
# Pearl 234 230 202
# Cobalt 30 32 61
# Chartreuse 127 255 0
# Chestnut 221 173 175
# Mauve 131 51 102

# a. create a dictionary C whose keys are the color names and the values the triples of their RGB values.
# b. write a function that given C and a letter “R”,”G”,”B”, returns the name of the color with the
# highest value of R, G and B respectively.
# c. write a function that given C returns the mean value of R,G,B over all the row of the table.
# d. write a function that given C, a letter “R”,”G”,”B” and an integer k, returns a new dictionary with
# only the colors such that R,G, B respectively have value greater than k.
# e. write a function that given C returns a triple (r,g,b) such that
# - r is the number of colors where the R value is greater of both G and B
# - g is the number of colors where the G value is greater of both R and B
# - b is the number of colors where the B value is greater of both R and G
# f. creates a dictionary T whose keys are the strings “Color”,”R”,”G”,”B”, and whose values are the
# list containing the respective columns of the table above.

#a
colors_table = {
    "Cyan": (0, 255, 255),
    "Pink": (255, 0, 255),
    "Yellow": (255, 255, 0),
    "Silver": (128, 128, 128),
    "Ivory": (225, 204, 79),
    "Pearl": (234, 230, 202),
    "Cobalt": (30, 32, 61),
    "Chartreuse": (127, 255, 0),
    "Chestnut": (221, 173, 175),
    "Mauve": (131, 51, 102),
}

#b
def get_color_with_highest_value(colors, component):
    index = {"R": 0, "G": 1, "B": 2}[component]
    return max(colors, key=lambda color: colors[color][index])

#c
def get_mean_rgb(colors):
    total_colors = len(colors)
    total_r = sum(value[0] for value in colors.values())
    total_g = sum(value[1] for value in colors.values())
    total_b = sum(value[2] for value in colors.values())
    return total_r / total_colors, total_g / total_colors, total_b / total_colors

#d
def filter_colors_by_value(colors, component, k):
    index = {"R": 0, "G": 1, "B": 2}[component]
    return {color: value for color, value in colors.items() if value[index] > k}

#e
def count_colors_by_component_relation(colors):
    r_count = sum(value[0] > max(value[1], value[2]) for value in colors.values())
    g_count = sum(value[1] > max(value[0], value[2]) for value in colors.values())
    b_count = sum(value[2] > max(value[0], value[1]) for value in colors.values())
    return r_count, g_count, b_count

#f
colors_columns = {
    "Colors": list(colors_table.keys()),
    "R": [value[0] for value in colors_table.values()],
    "G": [value[1] for value in colors_table.values()],
    "B": [value[2] for value in colors_table.values()],
}


print("Esercizio a:")
print(colors_table)

print("\nEsercizio b:")
print("Colore con più Rosso:", get_color_with_highest_value(colors_table, "R"))
print("Colore con più Verde:", get_color_with_highest_value(colors_table, "G"))
print("Colore con più Blu:", get_color_with_highest_value(colors_table, "B"))

print("\nEserczio c:")
print("Media valori RGB :", get_mean_rgb(colors_table))

print("\nEsercizio d:")
print("Colori con Rosso > 100:", filter_colors_by_value(colors_table, "R", 100))

print("\nEsercizio e:")
print("Conteggio dei colori in base alla relazione dei componenti:", count_colors_by_component_relation(colors_table))

print("\nEsercizio f:")
print(colors_columns)


colour_to_code = {"azure2": "#e0eeee",  "firebrick1": "#ff3030", "beige": "beige"}

for key, value in colour_to_code.items():
    print(key, " - ", value)

sorted_colours = sorted(colour_to_code)

print(sorted_colours)
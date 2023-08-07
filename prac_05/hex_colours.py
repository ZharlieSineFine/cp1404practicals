NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                "Antique White": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}

color_name = input("Enter color name: ").title()
while color_name != "":
    try:
        print(f"{color_name}'s color code is {NAME_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid color code")

    color_name = input("Enter color name: ").title()

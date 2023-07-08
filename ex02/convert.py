def string_int(txt):
    for char in txt :
        if not char.isdigit():
            return "The string contains alphabetic letter"
    return int(txt)
print(string_int("000"))
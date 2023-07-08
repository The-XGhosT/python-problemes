def sum_polygon(n):
    if n > 2:
        return (n - 2) * 180
    else:
        return "Error : value will always be greater than 2"
print sum_polygon(3)
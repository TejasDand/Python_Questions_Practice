#  Use a tuple as a key in a dictionary.

points = {
    (0, 0) : "Origin",
    (1, 0) : "X-Axis",
    (0, 1) : "Y-Axis"
}

print(points[(0, 1)])
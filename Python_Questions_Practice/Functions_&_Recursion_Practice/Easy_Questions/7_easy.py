# Write a function to calculate the area of a rectangle.

def area_of_rectangle(length, width):
    return length * width

result = area_of_rectangle(float(input("Enter length: ")),
                           float(input("Enter width: ")))

print(f"Area of rectangle: {result}")
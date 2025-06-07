# How would you safely open and read a file in binary mode?

filename = "Text files/sample.pdf"

with open(filename, "rb") as file:
    content = file.read()

    for byte in content[:10]:
        print(f"{byte:07b}",end=" ")    # This converts it into the binary code

print(f"\n{content[:100]}") # Python displays bytes like this
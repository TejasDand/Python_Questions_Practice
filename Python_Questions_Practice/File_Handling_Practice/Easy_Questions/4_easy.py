# How do you check whether a file  sample.txt exists or not?

from pathlib import Path

file = Path("Text files/sample.txt")

if file.exists():
    print("The file exists.")
else:
    print("The file does not exist.")
# Write a Python script to read all lines from a file  quotes.txt into a list.

with open("Text files/quotes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    quotes = content.split("\n")
    
    cleaned_quotes = []
    for quote in quotes:
        cleaned = quote.replace("'", '') \
                        .replace('\n', '') 

        cleaned_quotes.append(cleaned)
    
    print(cleaned_quotes)
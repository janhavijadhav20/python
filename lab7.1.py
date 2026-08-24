

text = input("Enter the email text: ")

symbols = ["@", ".", "!"]

print("\n----- SYMBOL COUNT -----")

for symbol in symbols:
    count = text.count(symbol)
    print(f"'{symbol}' occurs {count} time(s)")

print("------------------------")
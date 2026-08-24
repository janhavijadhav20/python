
paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

count = words.count("python")

print("\n----- WORD COUNT -----")
print(f'The word "python" appears {count} time(s).')
print("---------------------")
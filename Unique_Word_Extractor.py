text = input("Enter sentence: ")

words = text.lower().split()
unique = set(words)

print("Unique words:")
for w in unique:
    print(w)

print("Total unique:", len(unique))

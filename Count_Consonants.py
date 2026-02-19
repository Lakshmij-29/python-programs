text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch.isalpha() and ch not in vowels:
        count += 1

print("Consonant count:", count)

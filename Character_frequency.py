text = input("Enter text: ")
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

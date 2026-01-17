contacts = {}

print("Contact Book")

for i in range(3):
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts[name] = number

print("\nSaved Contacts:")
for name, number in contacts.items():
    print(name, ":", number)
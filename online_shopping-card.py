cart = {}
products = {
    "Laptop": 50000,
    "Phone": 20000,
    "Headphones": 2000
}

def show_products():
    for p, price in products.items():
        print(p, "-", price)

def add_to_cart():
    item = input("Enter product: ")
    if item in products:
        cart[item] = cart.get(item, 0) + 1

def checkout():
    total = 0
    for item, qty in cart.items():
        total += products[item] * qty
    print("Total Bill:", total)

while True:
    print("1.Products 2.Add to Cart 3.Checkout 4.Exit")
    ch = input()

    if ch == "1":
        show_products()
    elif ch == "2":
        add_to_cart()
    elif ch == "3":
        checkout()
    else:
        break
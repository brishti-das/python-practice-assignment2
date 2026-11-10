c_name = input("Enter Customer name: ")

def get_products():
    products = []
    prices = []

    i = 1
    while i <= 3:
        product = input(f"Enter product {i} name: ")
        price = float(input(f"Enter price: "))

        products.append(product)
        prices.append(price)

        i += 1

    subtotal = sum(prices)

    discounts = {
        5000 : 0.20,
        3000 : 0.10,
        1000 : 0.05,
        0 : 0
    }

    discount_rate = 0

    for amount,rate in discounts.items():
        if subtotal >= amount:
            discount_rate = rate
            break

    discount = subtotal * discount_rate
    final_total = subtotal - discount

    print("\nCoustomer Name: ", c_name)

    i = 0
    while i < 3:
        print(f"\nProduct{i+1}: {products[i]}")
        print(f"Price: {prices[i]:g}")
        i += 1
    print(f"\nSubtotal: {subtotal:g}")
    print(f"Discount: {discount:g}")
    print(f"Final Total: {final_total:g}")

get_products()

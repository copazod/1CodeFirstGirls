def calculate_vat(amount):
    return amount * 1.2

x = float(input('Enter the price with no VAT:'))
total = calculate_vat(x)

print('Total price with VAT:', total)

# We need to return the function

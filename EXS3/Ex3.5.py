t = float(input("Enter temperature: "))

if t>200:
    print("The oven is too hot.")
elif t<150:
    print("The oven is too cold.")
elif t==180:
    print("The oven is at the perfect temperature.")
else:
    print("The temperature is close enough.")
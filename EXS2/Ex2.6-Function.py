# Modify your triangle function so that you can set the side length
# using an argument
# Extension: Use a second argument to set the colour of the triangle

def trian_area(base, heigth):
    return base*heigth/2

b= float(input("Introduce base: "))
h= float(input("Introduce heigth: "))
area1 = trian_area(b,h)
print("the area of the triangle is:", area1)
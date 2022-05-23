# def function - add the radius argument inside the brackets
def circle_area(radius):
    return 3.14 * (radius ** 2)

# return area here
r=float(input("put radius: "))
circle_1 = circle_area(r)
print("the area is: ", circle_1)
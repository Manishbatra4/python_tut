def mul(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("error hai bc aur main nhi bta rha kya error hai!")
    finally:
        print("Haan Kutta ye Wala Block Chalega Kuch Bhe Kar Le")


mul(20, 0)

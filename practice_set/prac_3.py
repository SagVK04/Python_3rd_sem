def zero_div(a,b):
    try:
        c=a/b
        print("Value of division:",int(c))
    except:
        print("Zero division error!")
    else:
        print("No error occured!")
a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
zero_div(a,b)
a1=int(input("Enter first value:"))
b1=int(input("Enter second value:"))
zero_div(a1,b1)
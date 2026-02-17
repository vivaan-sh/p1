def bill(x):
    if x <= 100:
        price = x*5
        print("price:",price)
    elif x<= 200:
        price = 500+(x-100) * 7
        print("price:",price)
    else:
        price = 1900+(x-100) * 10 
        print("price:",price)  
bill(450)        
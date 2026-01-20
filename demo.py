def getnum():
    num = int(input("Enter a number"))
    return num

def pr(num):
    if check(num)%2:
        print(f"{num} is Odd")
    else:
        print("{} is Even".format(num))
    return 

def fact(num):
    for i in range(1,num):
        num*=i
    return num

def check(num):
    return bool(num % 2)

def main():
    num = getnum()
    print(fact(num))

if __name__=="__main__":
    main()

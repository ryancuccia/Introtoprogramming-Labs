def main():
    a,b = 1,1
    n = eval(input("Please input a number: "))
    nn = int(n-2)
    for i in range(nn):
        a,b=b, a+b
    print(b)
main()

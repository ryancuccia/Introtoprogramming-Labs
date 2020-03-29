def main():
    n = int(input("Please enter a number: "))
    t = 0
    for i in range(1,n):
        t +=(-1)**(i+1)*(1)/(i+i+1)
    v = 4*(1-t)
    print(v)
    import math
    z = math.pi
    a = float(z - v)
    print("Variance:", a)
main()

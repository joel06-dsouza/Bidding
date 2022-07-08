# cook your dish here
while True:
    try:
        t=int(input())
        while(t):
            x, y, z = input().split()
            if (int(x) > int(y)):
                if (int(x) > int(z)):
                    print("Alice")
                else:
                    print("Charlie")
            elif (int(y) > int(z)):
                print("Bob")
            else:
                print("Charlie")
    except EOFError:
        break
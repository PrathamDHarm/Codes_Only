def numbers_to_strings(argument):
    u = n-1
    g = u-1
    if(argument==1): 
        k = n 
        for i in range(0, n):
            for j in range(0, i):
                print(end=" ")
            for j in range(0, k):
                print("*",end=" ")
            k = k - 1
            print("\r")
    elif(argument==2):
        k = n 
        for i in range(0, n):
            for j in range(0, i):
                print(end=" ")
            for j in range(0, k):
                print("*",end=" ")
            k = k - 1
            print("\r")
        for l in range(0,u):
            for m in range(0, g):
                print(end=" ")
            g = g-1
            for s in range(0, l+2):
                print("_",end="  ")
            print("\r")
            
        
n = 5

if __name__ == "__main__":
    argument=int(input("enter the number: 1 or 2"))
    if(argument==1 or argument==2):
        print (numbers_to_strings(argument))
    else:
        print("Invalid Input")

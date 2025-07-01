
for i in range(10):
    for  j in range(i):
        print(j+1,end=" ")
    print()

i = 0  
while i < 10:
    
    print(" " * (10 - i), end="")

    for j in range(i + 1):
        def nCr(n, r):
            if r > n:
                return 0
            if r == 0 or r == n:
                return 1
            return nCr(n - 1, r - 1) + nCr(n - 1, r)
        
        print(nCr(i, j), end=" ")
    print()  
    i += 1
def MillerRabin(n,k):
    c=0
    #Step 0
    s=0
    m=n-1
    while m%2==0:       #we find the biggest power of 2 for witch n-1=2^s*t, where t is odd
        m=m/2
        s=s+1
        t=m
    print("2^s=2^",s,"and t=",t)
    #Step 1
    while c<k:
        c = c + 1
        a = int(input("Choose a random number between 1 and n:"))  # we choose a
        while a >= n or a <= 1:
            print("a must be smaller than n and bigger than 1. Please try again. <3")  # we make sure a is between 1 and n
            a = int(input("Choose a smaller a: "))
        print("a =", a)
        # Step 2
        v = []       #we create an empty vector
        j = 0        #we raise the 2^s with l*2 for s times
        l = 1
        while j <= s:
            r=a ** (l * t)
            while r>n:
                r=r/n
            v.append(r)         #we put the numbers a^(2^s)*t in the vector
            print(v[r])
            l = l * 2
            j = j + 1             #j makes sure we don't cross s times
        # Step 3
        ok=1                      #ok is the index that lets us know if we find something that is mentioned in Step 3
        if v[0] % n == 1:
            print("Probably prime")
            ok=0
        else:
            for j in range(1, len(v)):
                if v[j]%n == 1 and v[j - 1]%n == -1:
                    print("Probably prime")
                    ok = 0

        if ok == 0:
            print(n, " is surely prime")
            break

    if ok==1:
        print(n, "is surely composite")       #if n isn't prime and reaches break, then it is composite





def main():
    n = int(input("Choose the odd number you want to use: "))   #we choose n
    while n%2==0:                   #we make sure n is odd
        print("n must be an odd number. Please try again. <3")
        n = int(input("Choose another n: "))
    if n<4:                          #we make sure n is bigger than 3
        n = int(input("n must be >3. Please choose another one: "))
    print("n =", n)
    k = int(input("Choose a random number: "))      #we choose k
    print("k =", k)
    return MillerRabin(n,k)
if __name__ == "__main__":
    main()
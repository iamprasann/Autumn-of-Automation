#To print all twin twin primes
def twin_primes(d):
    is_prime = [True for i in range(10**d)]
    is_prime[0]= False
    is_prime[1]= False
    p = 2
    while (p * p < 10**d):
        if (is_prime[p] == True):
            for i in range(p * 2, 10**d, p):
                is_prime[i] = False
        p += 1

    f = open("myFirstFile.txt", "w+")
    for p in range(10**(d-1)+2, 10**d):
        if is_prime[p-2] and is_prime[p]:
            res = str(p-2)+" "+str(p)+"\n"
            f.write(res)

if __name__=='__main__':
    d = int(input("enter digits - "))
    twin_primes(d)

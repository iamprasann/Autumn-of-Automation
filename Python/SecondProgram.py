#To find next palindromic number
import math

def next_palindrome(num):
    digits = []
    while(num>0):
        digits.append(num%10)
        num=int(num/10)

    n = len(digits)-1

    all_nines=True
    for x in digits:
        if(x!=9):
            all_nines=False

    if(all_nines):
        result = []
        for i in range(n+2):
            result.append(0)
        result[0]=1
        result[n+1]=1
        return result
                
    flag = True
    i = int(n/2)

    if(n%2!=0):
        while(flag):
            if(digits[i]!=9):
                flag=False
            digits[i]=(digits[i]+1)%10
            digits[n-i]=(digits[n-i]+1)%10
            i=i-1
    else:
        if(digits[i]!=9):
            flag=False
        digits[i]=(digits[i]+1)%10
        i=i-1
        while(flag):
            if(digits[i]!=9):
                flag=False
            digits[i]=(digits[i]+1)%10
            digits[n-i]=(digits[n-i]+1)%10

    return(digits)

if __name__=='__main__':
    num = int(input("Enter number - "))
    result=next_palindrome(num)
    for x in result:
        print(x, end="")

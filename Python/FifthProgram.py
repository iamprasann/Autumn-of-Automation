"""
Full disclosure, I've done almost all my coding in C++,
hence my handle over python syntax isn't the best.
I don't know how to optimally use it to shortnes my code,
My approach is translating what I would do in C++, to python.

The naive approach would be to set i-th entry as the buying date,
and iterate from i+1 to n as the selling date, hence selecting the
best solution.
This would be O(n^2).

But on closer inspection, if we create an array storing the differences
of the stock value on i+1 vs i-th dates, the problem reduces to finding
the largest sum of a continuous SubArray, which can be done in O(n)
Hence, we can solve it in O(n)

"""
def solve(p, n):
    diff = []
    for i in range(n-1):
        diff.append(p[i+1]-p[i])    #O(n)

    max_sum=diff[0]
    upp_idx = 0
    curr_sum=diff[0]

    for i in range(1, n-1):                #O(n)
        if(diff[i]>diff[i]+curr_sum):
            curr_sum=diff[i]
        else:
            curr_sum=diff[i]+curr_sum
        if(curr_sum>max_sum):
            max_sum=curr_sum
            upp_idx=i

    idx=0
    for i in range(n-1):
        if(p[i]==p[upp_idx+1]-max_sum):
            idx=i
            break

    print(max_sum)
    print(idx+1)

if __name__=="__main__":
    n = int(input())
    p = []
    for i in range(n):
        p.append(float(input()))

    solve(p, n)

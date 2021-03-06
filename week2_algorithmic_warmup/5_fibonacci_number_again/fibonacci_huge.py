# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_opt(n, m):
    num = calc_fib(n)
    


def get_fibonacci_opt(n):
    
    F = range(n+1)
    F.insert(0,0)
    F.insert(1,1)

    for i in range(2, n+1):
        F[i] = (F[i-1] + F[i-2]) % 10
    return F[n]

if __name__ == '__main__':
    #input = sys.stdin.read();
    #n, m = map(int, input.split())
    n = 2015
    m = 3 
    print(get_fibonacci_huge_naive(n, m))

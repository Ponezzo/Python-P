import sys
sys.stdin = open('2. input.txt')

N = 10

def solve(N):
    if N == 0:
        return 1
    return solve(N) * solve(N-1)

ans = solve(N)
print(ans)
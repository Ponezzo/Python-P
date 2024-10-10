import sys
sys.stdin = open('2. input.txt')

N, K = map(int, input().split())

def solve(N, K):
  if K == 0 or N == K:
    return 1
  return solve(N-1, K) + solve(N-1, K-1)

ans = solve(N, K)
print(ans)
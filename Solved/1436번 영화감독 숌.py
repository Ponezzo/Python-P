import sys
sys.stdin = open('2. input.txt')

N = int(input())-1
arr = []
for i in range(665, 10000000):
    if '666' in str(i):
        arr.append(str(i))

print(arr[N])
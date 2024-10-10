import sys
sys.stdin = open('2. input.txt')

N =  int(input())
arr = []
for n in range(N):
    word = str(input())
    arr.append(word)
arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))
for i in arr:
    print(i)

# Spaces 4칸 안하면 런타임 에러가 뜬다!
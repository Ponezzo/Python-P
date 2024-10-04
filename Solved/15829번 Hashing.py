import sys
sys.stdin = open('2. input.txt')

L = int(input())
arr = list(map(str, input()))
mod = 1234567891
alpha_list = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 
              'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
               'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21,
                'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

# 알파벳 * 31 ** arr 길이
alpha_num = []
M = 0
res = 0
for i in arr:
  if i in alpha_list:
    alpha_num.append(alpha_list[i])

for i in alpha_num:
  res += i * 31 ** M
  M += 1
print(res%mod)
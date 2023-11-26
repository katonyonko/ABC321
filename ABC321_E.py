import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
5
10 2 0
10 2 1
10 2 2
10 2 3
10 2 4
11
822981260158260522 52 20
760713016476190629 2314654 57
1312150450968417 1132551176249851 7
1000000000000000000 1083770654 79
234122432773361868 170290518806790 23
536187734191890310 61862 14
594688604155374934 53288633578 39
1000000000000000000 120160810 78
89013034180999835 14853481725739 94
463213054346948152 825589 73
463213054346948152 8 463213054346948152
"""

def tmp(N,X,K):
  K=min(K,60)
  return max(X*(2**K)-1,min(N,X*(2**K)+(2**K)-1))-X*(2**K)+1

def solve(test):
  T=int(input())
  for _ in range(T):
    N,X,K=map(int, input().split())
    ans=tmp(N,X,K)
    while X>1 and K>0:
      if X%2==0: o=0
      else: o=1
      X//=2
      K-=1
      if K==0: ans+=1
      else:
        if o==0: ans+=tmp(N,2*X+1,K-1)
        else: ans+=tmp(N,2*X,K-1)
      # print(X,ans)
    print(ans)

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)
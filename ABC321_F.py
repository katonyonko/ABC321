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
15 10
+ 5
+ 2
+ 3
- 2
+ 5
+ 10
- 3
+ 1
+ 3
+ 3
- 5
+ 1
+ 7
+ 4
- 3
"""

mod=998244353

def solve(test):
  Q,K=map(int, input().split())
  dp=[0]*(K+1)
  dp[0]=1
  for _ in range(Q):
    op,x=input().split()
    x=int(x)
    if op=='+':
      for i in range(K,-1,-1):
        if i+x<=K:
          dp[i+x]+=dp[i]
          dp[i+x]%=mod
    else:
      for i in range(K+1):
        if i+x<=K:
          dp[i+x]-=dp[i]
          dp[i+x]%=mod
    print(dp[K])

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
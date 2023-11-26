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
2 2 7
3 5
6 1
1 3 2
1
1 1 1
7 12 25514963
2436426 24979445 61648772 23690081 33933447 76190629 62703497
11047202 71407775 28894325 31963982 22804784 50968417 30302156 82631932 61735902 80895728 23078537 7723857
"""

def solve(test):
  N,M,P=map(int, input().split())
  A=list(map(int, input().split()))
  B=list(map(int, input().split()))
  B.sort()
  BB=[0]+list(accumulate(B))
  A.sort()
  ans=0
  now=M-1
  for i in range(N):
    while now>=0 and A[i]+B[now]>P:
      now-=1
    ans+=A[i]*(now+1)+BB[now+1]+(M-now-1)*P
  if test==0:
    print(ans)
  else:
    return None

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
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
5 180
40 60 80 50
3 100
100 100
5 200
0 0 99 99
10 480
59 98 88 54 70 24 8 94 46
"""

def solve(test):
  N,X=map(int, input().split())
  A=list(map(int, input().split()))
  A.sort()
  ans=-1
  for i in range(101):
    if i<A[0]:
      if sum(A[:-1])>=X:
        ans=i
        break
    elif i>=A[-1]:
      if sum(A[1:])>=X:
        ans=i
        break
    else:
      if sum(A[1:-1])+i>=X:
        ans=i
        break
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
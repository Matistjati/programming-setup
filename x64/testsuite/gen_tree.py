#!/usr/bin/python3

import sys
from random import randint
import math

# Stolen from https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/DisjointSetUnion.py
class UF:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

n = 5
uf = UF(n)
querys=[]
k = 1
for i in range(n-1):
    while True:
        a,b=randint(0,n-1),randint(0,n-1)
        if a==b:continue
        if uf.find(a)==uf.find(b):continue
        uf.union(a,b)
        querys.append(('S',a+1,b+1))
        break

for i in range(k):
    querys.append(('Q',randint(1,n),randint(1,n)))

print(n,k)
for query in querys:
    print(query[0],query[1],query[2])

#!/usr/bin/python3

from ast import mod
import sys
from random import randint
import random
import string
import math
ra = randint

n=4
print(n)
print(ra(1,n),ra(1,n))

for i in range(n):
    print(" ".join(str(ra(1,5)) for i in range(n)))
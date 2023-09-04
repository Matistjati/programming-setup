import io
import random
import os
import time
import subprocess

programA = 'corr.exe < in.txt'
programB = '"comp_prog.exe" < in.txt'

last = time.time()
for i in range(10000):
    # Generate input
    inp = os.popen("python gen.py > in.txt").read()
    
    # Read output
    a = os.popen(programA).read().strip()
    b = os.popen(programB).read().strip()

    if a!=b:
    #if abs(float(a)-float(b))>1e-5:
        print("Diff at attempt ", i)
        print("Program ", programA.split()[0], ":",a)
        print("Program ", programB.split()[0], ":",b)
        with open("in.txt","r") as f:
            print("For input:\n"+ f.read())
        break

    if time.time()-last>5:
        print(i)
        last = time.time()


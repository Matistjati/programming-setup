import io
import random
import os
import time
import subprocess

programB = 'comp_prog.exe < in.txt'

last = time.time()
for i in range(10000):
    # Generate input
    inp = os.popen("python gen.py > in.txt").read()
    
    # Read output
    b = os.popen(programB).read()
    
    
    if len(b)>1:
    #if abs(float(a)-float(b))>1e-5:
        print("Diff at attempt ", i)
        print("Program ", programB.split()[0], ":",b)
        with open("in.txt","r") as f:
            print("For input:\n"+ f.read())
        break

    if time.time()-last>5:
        print(i)
        last = time.time()


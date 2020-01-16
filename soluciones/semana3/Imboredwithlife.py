from sys import stdin
from math import *
import sys 
def main():
    n=int(stdin.readline().strip())
    m=int(stdin.readline().strip())
    
    if n>m:
        print(factorial(m))
    else:
        print(factorial(n)) 
main()

 

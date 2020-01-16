from sys import stdin
from math import *
def main():
    n=str(stdin.readline().strip())
    while n!="":
        X=factorial(int(n))
        print(X)
        n=str(stdin.readline().strip())
main()

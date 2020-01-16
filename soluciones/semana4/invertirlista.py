from sys import stdin
n=[str(xx)for xx in stdin.readline().strip().split(",")]
n=n[::-1]
n=str(n)
n=n.replace("[","")
n=n.replace("]","")
n=n.replace(" ","")
n=n.replace("'","")
print(n)

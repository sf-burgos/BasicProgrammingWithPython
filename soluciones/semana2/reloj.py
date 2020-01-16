from sys import stdin
def main():
    n=[str(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
    while n!=[""]:
        z=int(n[0])
        y=int(n[1])
        if z<0 or y<0:
            print("ERROR")
        else:
            print((z+y)%24)
        n=[str(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
main()

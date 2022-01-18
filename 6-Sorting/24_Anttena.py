import sys

n = int(input())

houses = list(map(int, sys.stdin.readline().split()))
houses.sort()

print(houses[(n-1)//2])
n,k = map(int, input().split())
count=0
while(n>=k):
    remain = n%k
    if(remain == 0):
        n = int(n/k)
        count+=1
    else:
        n-=remain
        count+=remain
count+=(n-1)
print(count)
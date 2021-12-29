n = int(input())

count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            '''
            if(h%10 == 3 or h//10 == 3 or m%10 == 3 or m//10 == 3 or s%10 == 3 or s//10 == 3):
                count+=1
            '''
            if '3' in str(h)+str(m)+str(s):
                count+=1
print(count)
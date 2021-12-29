pos = input()

# ascii of 'a' is 97 or just use ord('a')
row = int(pos[1])
col = ord(pos[0])-ord('a')+1
mapSize = 8

dr = [-2,-2,-1,1,2,2,-1,1]
dc = [-1,1,2,2,-1,1,-2,-2]

count = 0

for i in range(8):
    tmp_r = row+dr[i]
    tmp_c = col+dc[i]
    if(tmp_r<=mapSize and tmp_r>0 and tmp_c<=mapSize and tmp_c>0):
        count+=1
print(count)
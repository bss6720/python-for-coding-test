n = int(input())
arr = []
for i in range(n):
    inp = input().split()
    arr.append((inp[0],int(inp[1])))

arr.sort(key=lambda student: student[1])

for student in arr:
    print(student[0],end=' ')
print()
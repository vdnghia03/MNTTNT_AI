m = int(input("So canh "))
n = int(input("So dinh "))
a = int(input("Dinh xuat phat "))
b = int(input("Dinh ket thuc "))
w = 0
ke = []
for i in range(0, n + 1):
    ke.append(i)
    ke[i] = []
for i in range(0, m):
    u = int(input())
    v = int(input())
    w = int(input())
    ke[u].append([w, v])
    ke[v].append([w, u])
    print(" ")
#BFS
from collections import deque

# Khai báo một ngăn xếp hoặc hàng đợi.
dd = []
tr = []
d = []
for i in range(0, 1000):
    dd.append(1)
    tr.append(0)
    d.append(0)
from queue import PriorityQueue
S = PriorityQueue()
S.put((0, a))
dd[a] = 0
print(" ")
check = 0
while(S.qsize() != 0):
    v = S.get()
    dd[v[1]] = 0
    if(v[1] == b):
        check = 1
        break
    for i in range(0, len(ke[v[1]])):
       if(dd[ke[v[1]][i][1]] == 1):
           tr[ke[v[1]][i][1]] = v[1]
           d[ke[v[1]][i][1]] = d[v[1]] + ke[v[1]][i][0]
           S.put((d[ke[v[1]][i][1]], ke[v[1]][i][1]))

if(check == 0): print("Khong co duong di tu " + str(a) + " den diem " + str(b))
else:
    u = b
    print(str(u) + " <-- ", end = " ")
    while(u != a):
        print(str(tr[u]) + " <-- ", end = " ")
        u = tr[u]
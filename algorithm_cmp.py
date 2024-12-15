t = "лилила"

pi = [0]*len(t)
j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        pi[i] = j+1
        j += 1
        i += 1
    else:
        if j == 0:
            pi[i] = 0
            i += 1
        else:
            j = pi[j-1]
print(pi)

a = "лилось лилилась"
m = len(t)
n = len(a)

i = 0
j = 0

while i < n:
    if a[i] == t[j]:
        j += 1
        i += 1
        if j == m:
            print("find")
            break
    else:
        if j > 0:
            j = pi[j-1]
        else:
            i += 1
if i == n and j != m:
    print("not find")
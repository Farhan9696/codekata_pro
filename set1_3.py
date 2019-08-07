f,s=list(map(str,input().split()))
t=0
if f==s: print(t)
elif len(f)>len(s):
    f=list(f)
    s=list(s)
    for i in range(0,len(s)):
        for j in range(0,len(f)):
            if f[j]==s[i]:
                f.pop(j)
                break
    t=len(f)
    print(t)
else:
    for i in range(0, min(len(f), len(s))):
        if f[i] != s[i]:
            t = t + 1
        if i == min(len(f), len(s)) - 1:
            t = t + abs((i + 1) - max(len(f), len(s)))
    print(t)

 a,b=input().split()
char=abs(len(b)-len(a))
for c in range(len(a)):
  if(len(b)==1 and b[c] in a):
    break
  if(a[c]!=b[c]):
    char=char+1
print(char)

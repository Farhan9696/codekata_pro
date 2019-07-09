a = int(input())
b=[]
for i in range(0,a):
 c=input()
 b.append(c)
this=[]
for i in zip(*b):
 if(i.count(i[0])==len(i)):
  this.append(i[0])
 
 else:
  break
print(''.join(this))

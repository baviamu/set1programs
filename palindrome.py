ab=int(input())
temp=ab
val=0
while(ab>0):
     n=ab%10
     val=val*10+n
     ab=ab//10
if(temp==val):
     print("yes")
else:
     print("no")

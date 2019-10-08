#Program for FLAMES
print("**********       FLAMES      **********")
a=list(input('Enter 1st person name:'))
b=list(input('Enter 2nd person name:'))
for i in a:
    if i in b:
        a.remove(i)
        b.remove(i)
c=len(a)+len(b)
print(c)
d=['FRIENDS','LOVE','AFFECTION','MARRIAGE','ENEMY','SISTER']
while len(d)>1:
    e=(c%len(d)-1)
    if e>=0:
        r1=d[e+1:]
        r2=d[:e]
        d=r1+r2
    else:
        d=d[:len(d)-1]
print(d[0])
print("Its not true for all so don't feel sad ")

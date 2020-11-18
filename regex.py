import re
f=open("regex_sum_692533.txt")
y=list()
for line in f :
    x=re.findall('([0-9]+)',line)
    y=y+x
sum=0
c=0
for z in y:
    c=c+1
    sum=sum+int(z)
print(sum)
print(c)

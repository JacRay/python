
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x=0
s=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        p=line.find("0.")
        t=line[p: ].rstrip()
        x=x+1
        s=s+float(t)
print("Average spam confidence:",float(s)/float(x))
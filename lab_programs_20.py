#f=open("data.txt",'w')
#f.write("Aditya College Of Engineering")
#f.close()
w=0
lin=0
c=0
s=0
f=open("data.txt",'r')
for l in f:
    w+=len(l.split())
    lin+=1
    c+=len(l)
    s+=l.count(" ")
f.close()
print(w,lin,c,s)

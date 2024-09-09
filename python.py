f=open(".\abc.txt",'wt')
lines=["hi","how are you","good afternoon"]
f.writelines()
print("position after write",f.tell())
print("read after write",f.read())
f.seek(0,0)
print("read from beginning",f.read(10))
f.seek(3,1)
print("read:",f.read())

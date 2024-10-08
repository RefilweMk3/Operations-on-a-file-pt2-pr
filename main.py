print("Hey there welcome to reading py files in different ways")
file=open("ref.txt","r")
for x in file:
    print(x)
file.close

f1=open("main.txt","r")
f2=open("py.txt","w")

for line in f1.readlines():
    if not(line.startswith('Coding')):
        f2.write(line)
f1.close()
f2.close()

with open("ref.txt","w") as f:
    f.write("Soooo \n these are one of the different fundimentals to py")
f.close
with open("ref.txt","r")as f:
    data = f.readlines()
    for line in data:
        word = line.split()
        print(word)
f.close()
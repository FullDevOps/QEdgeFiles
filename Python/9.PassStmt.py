##Program PassStmt.py
#Program to demo pass-stmt in program with Loops

#inside loops
for x in range(1,101):
    if x%3!=0:
        pass;
    else:
        print(x)

print()
i=1;
while i<=100:
    if i%5!=0:
        pass;
    else:
        print(i)
    i=i+1

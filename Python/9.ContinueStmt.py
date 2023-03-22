##Program (ContinueStmt.py)
##Program to demo continue-stmt in Loops

#using while-loop
i=1
while(i<=100):
    if i%2==0:  #even
        print(i)
    else:
        i=i+1;
        continue;
    i=i+1


#using for loop
for x in range(1,101,1):
    if x%2!=0:  #odd
        print(x)
    else:
        continue;


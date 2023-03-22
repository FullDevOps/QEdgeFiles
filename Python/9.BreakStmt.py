##Program (BreakStmt.py)
##Program to demo break-stmt in Loops)


#using while loop
i=1
while i<=100:
    if i>=50:
        break;
    print(i)        #odd-nums
    i=i+2;
'''

'''    
#using infinite while loop
i=2
while True:
    if i==102:
        break;
    print(i)        #even-nums
    i=i+2;


#using for-loop
for x in range(0,1001,3):
    if x>500:
        break;
    print(x)


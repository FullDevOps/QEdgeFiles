
##Program (WhileLoopEx1.py)	
#Program to print N-Natural numbers using while-loop

i=1;
while i<=10:
	print(i);
	i=i+1;
print("End of While Loop");
'''

'''
#Printing SUM of N-Natural Numbers
sum=0;
n = int(input("Enter any num : "));
i=1;
while i<=n:
	sum=sum+i;
	i=i+1;
print("Sum : ",sum);
print("Sum of :",n,"Natural numbers is :",sum);


#while loop single suite stmt
n = int(input("Enter N-value :: "))
i=1;
while i<=n: print(i*i); i+=1;
print()
i=1;
while i<=n: print(i*i*i); i+=1;


##Program (InfiniteLoop.py)
#(Program to demo Infinite-Loop while)

i=1
while True:
    print(i)
    i=i+1;
    
print("End of While Loop"); 



i=1;
while i<=10:
	print(i);
	i=i+1;
else:		#here else-block is executed only once
	print("End of Natural-Nums");

print("\nEnd of While Loop")


# **sp-case**
# ==> Nested Loops:-
# = Using a particular loop inside another loop is called Nested-Loop
# (loop with-in loop)
# Ex:-
for i in range(3):		#outerloop(i=0,1,2) ---> rows
	for j in range(3):	#innerlloop(j=0,1,2) ---> cols
		print(i,",",j,end="\t");
	print();



##Program (NestedLoopEx1.py)
#Program to demo Nested-Loops

for i in range(3):			#outer-loop(0,1,2) => rows(i)
	for j in range(3):		#inner-loop(0,1,2) => cols(j)
		print(i,",",j,sep="",end="\t");
	print();
	
print("End of Program")


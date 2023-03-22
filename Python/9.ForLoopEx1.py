##Program ForLoopEx1.py)
# (Program to deme Python For Loop)
##Program (ForLoopEx1.py)
#Program to demo for-loop


#using str
s1 = "Hello";		#coll.of.chars
for x in s1:
	print(x);
print("End of For Loop")
'''

'''
#using str with indexes
s1 = "Hello";       #Hello(0,1,2,3,4)
i=0;
for x in s1:
	print("index",i,"char is",x);
	i=i+1;
print("End of For Loop")
'''

'''
#range()
for x in range(10):     #0 to 9
	print("Sai");
    
print()
for x in range(10):     #0 to 9
	print(x+1);
'''

'''
#sum of N-natural no's	
sum=0;
for x in range(1,11):   #1 to 10    
	sum=sum+x;
print("Sum :",sum);	
'''

'''
#for loop single suite stmt (header & suite in single-line)
for x in range(1,11): print(x*x);
print()
for x in range(1,11): print(x*x*x);


#using list-coll
for x in [11,22,33,44,55]:
    print(x)


##Program (ForLoopElseEx1.py)
#Program to demo for-loop with else-block

vals = [11,22,33,44,55];
for x in vals:
	print(x);
else:				#else is executed only 1-time
	print("End of the Vals");

print("End of For Loop");
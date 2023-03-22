##Program (IfElifElse.py)
#Program to accept 5 subject marks of a student and print the grade Distinction,1st-class,2nd-class,3rd-class or Fail
#Program to demo If-elif-else

print("Enter 5 Subject Marks :");
s1 = int(input("Sub1 : "));
s2 = int(input("Sub2 : "));
s3 = int(input("Sub3 : "));
s4 = int(input("Sub4 : "));
s5 = int(input("Sub5 : "));

total=s1+s2+s3+s4+s5;
avg = (total)/5;

print("Total-Marks : ",total);
print("Average-Marks : ",avg);

if (avg>=75):
	print("Distinction");
elif (avg>=65):
	print("1st-Class");
elif (avg>=50):
	print("2nd-Class");
elif (avg>=35):
	print("3rd-Class");
else:
	print("Failed");
	
print("End of Program");


#"Assignment"(if-elif-else)
#WAP to accept age of person and print following msgs
# (Baby, Kid, Teenage, Adult, Oldage)
"""
if personage >=65
elif personage>=18
elif personage>=12
elif personage>=5
else "Baby"
"""
#Assignment (if-elif-else)
#WAP to display given num is +ve, -ve, 0 (if-elif-else)
#WAP to display given num is even, odd, neither(if-elif-else)

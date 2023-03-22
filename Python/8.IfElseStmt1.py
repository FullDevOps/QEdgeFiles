
##Program IfElseStmt1.py
#Program to demo if-else stmt


#single-stmt
name = input("Enter any name : ");
if name=="Sai":
	print("Hello :",name);
else:
	print("Hello : New User!!");
	
print("End of Program!!");
'''

'''
#multi-stmts
name = input("Enter any name : ");
if name=="Sai":
	print("Hello :",name);
	print("Have a nice day!!");
else:
	print("Hello : New User!!");
	print("Register your Name...");

print("Take care n Bye!!");


#sp-case
#single-suite-stmt (Header & Suite in single-line)
num = int(input("Enter any Integer-Number : "));
if num==0: print("Given Number is 0");
else: print("Given Number is NON-Zero(+ve/-ve)");



# "Assignment"
#WAP to accept age of a person as input & display "Eligible for Voting or not"
##Program(IfElseStmt2.py)
#Program to demo if-else stmt (IfElseStmt1.py)


age = int(input("Enter your Age : "));
if (age>=18):
	print("Your are Eligible for Voting");
else:
	print("You are NOT-Eligible for Voting");
	
print("End of Program..!!");



# "Assignment"
#WAP to check for for eligibility for marraige
# (maleage>=21 and femaleage>=21) [T and T  ---> T]
#WAP to accept age of candidate & print eligibility for employement
# (personage >= 15 and personage <= 65) [T and T  ---> T]

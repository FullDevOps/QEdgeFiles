
##Program (StringEx2.py)
#Program to accept string and print its chars with indexes & slice-operator


#using index and [] oper
ss = "Hello";
print(ss[0]); 
print(ss[1]); 
print(ss[2]); 
print(ss[3]); 
print(ss[4]); 
print(ss[-1]); 
print(ss[-2]); 
print(ss[-3]); 
print(ss[-4]); 
print(ss[-5]); 
#print(ss[10]);	#IndexError 
'''

'''
#string access with loop
ss = input("Enter any String : ");
i=0;
for x in ss:
	print(i,"=====>",x)
	i=i+1;
'''
	
''' 
#using slicing operator
ss = "Welcome to Python Session";
print(ss[1:9:1]);
print(ss[1:9]);	
print(ss[1:9:2]);
print(ss[:9]);
print(ss[9:]);
print(ss[::]);
print(ss[:]);	
print(ss[::-1]);
print(ss[::-2]);
print(ss[-1:-9:-1]);
print(ss[-1:-9:-2]);	
print(ss[-9:-1:-1]);
print(ss[1:0:2]);	
'''

'''
#str addition(+) & repetition(*)
s1 = "Sai Ram";
s2 = " Kumar";
print(s1+s2);
print(s1*5);
print(s1*-5);
print(s1*0);


#len() func
ss = "Sai Ram Kumar";
ss="Hello"
print(len(ss));

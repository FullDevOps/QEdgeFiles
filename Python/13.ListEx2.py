
##Program...(ListEx2.py)
#Program to work with List DS (ListEx2.py)

#Using indexes (0 to n-1) or (-1 to -n)
list1 = [54,64,74,84,94];
print(list1[0]);
print(list1[1]);
print(list1[2]);
print(list1[3]);
print(list1[4]);
print()
print(list1[-1]);
print(list1[-2]);
print(list1[-3]);
print(list1[-4]);
print(list1[-5]);
#print(list1[10]);	#IndexError: list index out of range
'''

'''
#Using slice-operator(Slicing)
#list1[startindex:endindex:stepindex]
list1 = [11,22,33,44,55,66,77,88,99,110];
print(list1);
print(list1[2:7:2]);
print(list1[4::2]);	
print(list1[3:7]);
print(list1[8:2:-2]);
print(list1[4:100]);	#No-Error(for 100) but takes till last-index
'''

'''
#List is Mutable (org-data can be modified)
list1 = [11,22,33,44,55];
print(list1);
print(id(list1))
list1[1]=222;
print(list1);
print(type(list1))

'''

'''
#using for-loop:-
list1 = [11,22,33,44,55,66,77,88];
for x in list1:
	print(x);


#using while loop:-
list1 = [11,22,33,44,55,66,77,88];	#len=8
i=0;
while i<len(list1):
	print(list1[i]);
	i=i+1;


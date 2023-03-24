
##Program (ListEx4.py)
#Program to work with list DS


#list ordering (ASC/DESC)
#reverse()
#list1 = [11,22,33,44,55];
list1 = ["hi","hello","welcome"]
print(list1)
list1.reverse();
print(list1);
'''

'''
#sort() -> sorts elemnts ASC/DESC
list1 = [44,11,55,22,33];
print(list1);
list1.sort();	#sort() default-order is ASC(False)
print(list1);
print()
list1 = ["hyd","delhi","chennai","apple","ball"];
list1.sort();	#sort() default-order is ASC(False)
print(list1);
'''

#list1 = ["B",11,"C",22,"A"];
#list1.sort();	#Not-possible with diff-type of data
#print(list1); 

'''
#sort(reverse=True) #DESC-order
list1 = [44,11,55,22,33];
list1.sort(reverse=True);
print(list1);	#DESC
list1.sort(reverse=False);
print(list1);	#ASC
'''

'''
list1 = ["hyd","delhi","chennai","apple","ball"];
list1.sort(reverse=True);
print(list1);
list1.sort(reverse=False);
print(list1);
'''


'''
#Alias(alternate-name)
list1 = [11,22,33,44,55];       #org-list(list1)
list2 = list1;	#in memeory, list1 & list2 both points to same-location-values
print(id(list1));
print(id(list2));
print(list1);
print(list2);
#operation on alias-var-name
list2[0]=1111;	#mutable-object
print(list1);
print(list2);
'''

'''
#list-cloning(we get separate data for memory)
#dup-obj or separate-obj
list1 = [11,22,33,44,55];
list2 = list1[:];	#slicing-operator
print(id(list1));
print(id(list2));
list2[0]=1111;
print(list1);
print(list2);
'''
'''
#copy() for list-ds(we get new memory location)
#it is also cloning (new dup-obj or separate-obj)
list1 = [11,22,33,44,55];
list2 = list1.copy();
print(id(list1));
print(id(list2));
list2[0]=1111;
print(list1);
print(list2);
'''

'''
#list-concatenation(+)
#using concatenation-operator(+)
list1 = [11,22,33];
list2 = [44,55,66];
list3 = list1+list2;
print(list3);
print()
list1 = [11,22,33];
#list3 = list1+77;	#TypeError
list3 = list1+[77];	#Valid
print(list3);
list3 = list1+[77,88];	#Valid
print(list3);
'''

'''
#List Repeatition(*)
list1 = [11,22,33];
list2 = list1*3;
print(list2);
list2 = 5*list1;
print(list2);
'''

'''
#Listcomparisons (relational-oper) <,>,<=,>=,==,!=
list1 = [11,22,33];
list2 = [11,22,33];
list3 = [44,22,33];
print(list1==list2);
print(list1==list3);
print(list2!=list3);
print()
list1 = ["hi","hello","welcome"];
list2 = ["hi","hello","welcome"];
list3 = ["HI","HELLO","WELCOME"];
print(list1==list2);
print(list1==list3);
print(list2!=list3);
'''

'''
#membership operator (in, not in)
list1 = [11,22,33,44,55];
print(11 in list1);
print(11 not in list1);
print(111 in list1);
print(111 not in list1);
'''

'''
#clear() -> removes all elements at a time
list1 = [11,22,33,44,55];
print(list1);
list1.clear();
print(list1);	#empty-list


#Nested-List (sub-list) 
#list with-in list
list1 = [11,22,33,[44,55]];
print(list1[0]);
print(list1[1]);
print(list1[2]);
print(list1[3]);	#[44,55]
print(list1[3][0]);		#sub-index
print(list1[3][1]);





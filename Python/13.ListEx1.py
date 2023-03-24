##Program ListEx1.py
#Program to work with List DS (ListEx1.py)


#Empty-List (empty-[] brackets)
list1 = [];
print(list1);
print(type(list1));
'''

'''
#List with Elements
list1 = [10,20,30,40,50];
print(list1);
print(type(list1));
'''

'''
#List with Dynamic-Elements #given in [] sqr-brackets
list1 = [];
list1 = eval(input("Enter some list elements : "));
print(list1);
print(type(list1));
'''

'''
#using list() conversion-function and range() functions
list1 = list(range(0,20,2));
print(list1);
print(type(list1));

list1 = list(range(0,20,-2));
print(list1);	#empty-list
print(type(list1));

list1 = list(range(20,0,-2));
print(list1);
print(type(list1));
'''

'''
#using a string with list()
ss = "Sai Kumar";
list1 = list(ss); #each char is converted to list-values
print(list1);
'''

'''
#using a string with split()
ss = "Sai Ram Kumar have a nice day";
list1 = ss.split(" ");		#by default splits data wrt space
print(list1);
print(type(list1));


#Nested-List
list1 = [11,22,33,[99,88]];
print(list1);

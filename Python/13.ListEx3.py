
##Program ListEx3.py	
#Program to  work with list DS (ListEx3.py)


#len()
list1 = [11,22,33,44,55];	
print(len(list1));
list1 = [11,22,33];	
print(len(list1));
list1 = [];	
print(len(list1));
'''

'''
#count()
list1 = [11,22,33,11,22,33,44,55,55];	
print(list1.count(11));
print(list1.count(22));
print(list1.count(33));
print(list1.count(44));
print(list1.count(55));
'''

'''
#index() gives 1st-index-postion(Search)
list1 = [11,11,22,22,33,33,44,44,55];	
print(list1.index(11));
print(list1.index(22));
print(list1.index(33));
print(list1.index(44));
print(list1.index(55));
#print(list1.index(66));	#ValueError
##print(66 in list1);
'''

'''
#append() adds from last
list1=[];
print(list1);
list1.append("A");
list1.append("B");
list1.append("C");
print(list1);
list1.append("D");
list1.append("E");
print(list1);
'''

'''
#insert() -> inserts element in b/w(other moves to aside)
list1 = [11,22,33,44,55];
print(list1);
list1.insert(1,999);
print(list1);
list1.insert(10,987);	#inserted at last
print(list1);
list1.insert(-10,789);	#inserted at begin
print(list1);
'''

''' 
#extend() -> adds other-coll to our list-coll
list1 = [11,22,33];
list2 = ["Hi","Hello","Welcome"];
list1.extend(list2);
print(list1);
print()
list1 = [11,22,33];
list1.extend("World"); #here each-char is added as list-element
print(list1);
'''

'''
#remove() -> dels 1st-occurance element
list1 = [11,22,11,22,33,11];
print(list1)
list1.remove(11);
print(list1);
list1.remove(22);
print(list1);
# list1.remove(44);	#ValueError
'''

'''
#pop() removes last or random element o.w Error for empty
list1 = [11,22,33,44,55];
print(list1)
print(list1.pop());
print(list1.pop());
print(list1);
#list1=[];
#print(list1.pop());		#IndexError



#pop(index) remmoves elements using indexes
list1 = [11,22,33,44,55];
print(list1)
print(list1.pop());
print(list1.pop(0));
print(list1);
#print(list1.pop(10));	#IndexError (out of range)

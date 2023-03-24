
###Program... (TupleEx1.py)
#Program to work with Tuple DS


#creating a tuple(with & w.o ()brackets)
tup1 = 11,22,33,44,55;		#() are not-complusory(optional)
tup1 = (111,222,333,444,555);
print(tup1);
print(type(tup1));
'''

'''
#empty-tuple
tup1=();
print(tup1);
print(type(tup1));
'''

'''
#tuple with single-value(give , compulsory)
tup1=(10);	#Single-Value Tuple taken as int-value data-type
print(tup1);
print(type(tup1));
#sp-case
tup1=10,;			#(10,);	#Single-Value Tuple with , comma
print(tup1);
print(type(tup1));
'''

#Other Tuple Examples
'''
tup1=();    #empty-tuple
print(tup1);
print(type(tup1));
'''

'''
tup1=11,22,33; #tuple w.o ()
print(tup1);
print(type(tup1));
'''

'''
tup1=10;        #single-value(respective-dtype)
print(tup1);
print(type(tup1));
print()
tup1=10,;  #give ,(compulsory)
print(tup1);
print(type(tup1));
'''
'''
#single-value
tup1=(10);
print(tup1);
print(type(tup1));
print()
tup1=(10,);
print(tup1);
print(type(tup1));
'''
'''
tup1=(10,20,30);
print(tup1);
print(type(tup1));
'''

'''
#Creating Tuple with tuple()
list1 = [11,22,33];
tup1 = tuple(list1);	#converts list to tuple
print(tup1);
tup1 = tuple(range(0,20,2));	#converts range-values to tuple
print(tup1);
tup1 = tuple("hello") #str to tuple
print(tup1)
'''

'''
#Access Elements with indexes
tup1 = (11,22,33,44,55);
print(tup1[0]);
print(tup1[1]);
print(tup1[2]);
print(tup1[3]);
print(tup1[4]);
print(tup1[-1]);
print(tup1[-2]);
print(tup1[-3]);
print(tup1[-4]);
print(tup1[-5]);
# print(tup1[100]);	#IndexError (out-of-index-range)
# print(tup1[-100]);
'''

'''
#Using slice-operator [startindex:endindex:stepvalue]
tup1 = (11,22,33,44,55);
print(tup1[0]);
print(tup1[1:5]);
print(tup1[0::2]);
print(tup1[0:100:2]);
print(tup1[-1:-5:-2]);
'''

'''
#Tuple is Immutability
tup1 = (11,22,33,44,55);
print(tup1);
# tup1[0]=111;	#TypeError
print(tup1)
'''

'''
#Concatenation (using +)
tup1 = (11,22,33);
tup2 = (44,55,66);
tup3 = tup1+tup2;
print(tup3);
#Repetition (using *)
tup1 = (11,22,33);
tup2 = tup1*3;	#3*tup1
print(tup2);
'''

#Tuple-Functions
'''
#len()
#tup1 = (11,22,33);
tup1 = tuple("Welcome")
print(len(tup1));
'''

'''
#count()
tup1 = (11,22,33,44,55,11,22,11);
print(tup1.count(11));
print(tup1.count(22));
print(tup1.count(55));
print(tup1.count(99));
'''

'''

#index()
tup1 = (11,22,33,44,55,11,22,11);
print(tup1.index(11));
print(tup1.index(22));
# print(tup1.index(222));	#ValueError
'''

'''
#sorting (sorted())
tup1 = (11,22,33,44,55,11,22,11);
tup2 = sorted(tup1) #after sorting we get list
print(tup1);
print(tup2);	#Here we get list
print(tuple(tup2));	#list to tuple()
'''

'''
#sorted(tup1, revserve=True/Fase)
tup1 = (11,22,33,44,55,11,22,11);
tup2 = sorted(tup1,reverse=True);	#True means DESC-order (False(ASC))
print(tup1);
print(tuple(tup2));	#Here we get list #use tuple() to coverted it
'''

'''
#min() & max()
tup1 = (11,22,33,44,55,11,22,11);
print(min(tup1));
print(max(tup1));
'''

'''
#Tuple-packing (creating a tuple)
a=11;
b=22;
c=33;
d=44;
e=55;
tup1 = a,b,c,d,e;
print(tup1);
'''

'''
#Tuple-unpacking
tup1=(11,22,33,44,55);
a,b,c,d,e=tup1;
print(a);
print(b);
print(c);
print(d);
print(e);
'''

'''
tup1=(11,22,33,44,55);
# a,b,c=tup1;	#ValueError (5-values cannot be un-packed to 3-variables)

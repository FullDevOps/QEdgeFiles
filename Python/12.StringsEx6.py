##Program (StringsEx6.py)
##Program to work with string-functions or methods

#find() & rfind()
ss = "Hello Students, Welcome to Python Session, Hello by Sai sir";
print(ss.find("Hello"));    #gives only 1st occurance
print(ss.find("Java"));		#-1 on un-successful search
print(ss.rfind("Hello"));
print(ss.rfind("Java"));
#find(), rfind() we get -1 for un-successful search


#find(string,beg-ind,end-ind) & rfind(string,beg-ind,end-ind)
ss = "Hello Students, Welcome to Python, Hello all";
print(ss.find("Hello",6));	#From 6th-index to last-index
print(ss.find("Hello",6,20));
print(ss.rfind("Hello",0,30));
print(ss.rfind("Hello",6,len(ss)));
print(ss.rfind("Hello",-1,-10));	#Here indexes cant be -ve
'''

'''
#index() and rindex() #here we get ValueError for un-successful search
ss = input("Enter Main String : ");
subss = input("Enter Sub String : ");
print(ss.index(subss));
print(ss.index(subss,9,len(ss)));
print(ss.rindex(subss));		#0(begin) & len(end)
print(ss.rindex(subss,0,17));
'''

'''
#count()
#Counting all sub-strings in main-string
ss = "Hello Welcome to Python Hello users";
print(ss.count("Hello"));
print(ss.count("Hello",6));
print(ss.count("Hello",6,len(ss)));
print(ss.count("Welcome",6));
print(ss.count("Welcome",8));
'''

'''
#replace()
#Replacing old-str with new-str
ss = "Hello, Welcome to Python, Hello users";
#newss = ss.replace('e','*');
newss = ss.replace('Hello','Hi');
print(ss);
print(newss);


#Immutable str-obj
ss = "Hello Welcome";
newss = ss.replace('e','*');
print(ss,"===>",id(ss));
print(newss,"===>",id(newss));

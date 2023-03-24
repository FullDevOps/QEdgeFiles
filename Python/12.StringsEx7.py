##Program (StringsEx7.py)
#Program to work with string functions(operations)


#split()
ss = "Hello Students, Welcome to, Python Session";
listss = ss.split(' ');
listss = ss.split();
listss = ss.split(",");
print(listss);
'''

'''
#join()
listss = ['Hello', 'Students', 'Welcome', 'to', 'Python', 'Session'];
#Joining of strings
ss = " ".join(listss);
print(ss);
ss = "-".join(listss);
print(ss);
ss = "".join(listss);       #empty-string
print(ss);
ss = "-".join(["Sai","Ram","Ali"]);
print(ss);
listss = ["Hyd","Mum","Che","Delhi"];
ss = ":".join(listss);
print(ss);
'''

'''
##Changing-cases in string
ss = "Hello welcome to Python session";
print(ss.upper());
print(ss.lower());
print(ss.swapcase());
print(ss.title());
print(ss.capitalize());


#Starting & Ending strings
ss = "Hello Students, Welcome to Python Session";
print(ss.startswith("Hello"));
print(ss.endswith("Session"));
print(ss.startswith("Hi"));
print(ss.endswith("Bye"));

##Program (StringsEx1.py)
##Program to demo strings in python

#str-type
ch = 'A';
print(type(ch));
print(ch);

ch = "A";
print(type(ch));
print(ch);

ss='Sai Ram Kumar';
print(type(ss));
print(ss);

ss="Sai Ram Kumar";
print(type(ss));
print(ss);

print()
addr = """Sai Ram Kumar,
HimayathNagar,
Hyderabad.
"""; 
print(addr);
addr = """
    Sai Ram Kumar,
    
    HimayathNagar,
    
    Hyderabad.
"""; 
print(addr);

print()
#quotes with in quotes
#ss = 'Hi Hello's Welcome';	#Error
#ss = "Hi Hello's Welcome";
#ss = 'Hi Hello\'s Welcome';
#ss = 'Hi Hello"s Welcome';
#ss = "Hi Hello\"s Welcome";	#Error
#ss = 'Hi Iam "Sai Ram Kumar"';
#ss = 'Hi Iam "Sai Ram Kumar" and "Python" Trainer';
#ss = 'Hi Iam "Sai Ram Kumar" and \'Python\' Trainer';
#ss = '''#Hi Iam "Sai Ram Kumar" and 'Python' Trainer''';
ss = """Hi Iam "Sai Ram Kumar" and 'Python' Trainer""";
print(ss);

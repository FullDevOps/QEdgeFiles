##Program (StringsEx8.py)
#Program to work with string functions (Type of Characters)

ss="SaiRam123";
print(ss.isalnum());
print(ss.isalpha());

print()
ss="SaiRam";
print(ss.isalpha());
print(ss.isdigit());

print()
ss="123123";
print(ss.isdigit());

print()
ss="sairam";
print(ss.islower());
print(ss.isupper());

print()
ss="sairam123";
print(ss.islower());	#**sp-case(T)
print()
ss="SAI123";
print(ss.isupper());    ##**

print()
ss="Hello Students Welcome To Python";
print(ss.istitle());

print()
ss="Hello students Welcome to Python";
print(ss.istitle());

print()
ss=" ";
print(ss.isspace());
ss="\t";
print(ss.isspace());
ss="\n";
print(ss.isspace());
ss="\b";		#**sp-case
print(ss.isspace());
ss="\r";
print(ss.isspace());

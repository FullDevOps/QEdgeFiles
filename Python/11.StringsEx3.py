##Program (StringEx3.py)
#Program to work with strings(check/find/search)

'''
#case-1
ss ="Hello Students, Welcome to Python Class";
print("to" in ss);
print("," in ss);
print("hi" in ss);
print("Python" not in ss);
'''

#case-2
s1 = input("Enter any main or org. string : ");
s2 = input("Enter any searching string : ");
if s2 in s1:
	print(s2,": is found in org-string");
else:
	print(s2,": is NOT found in org-string");

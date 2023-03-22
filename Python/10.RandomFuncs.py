##Program RandomFuncs.py
#Program to work with Random-Functions


#choice() (works only on index-coll)
import random;
list1 = [11,22,33,44,55];
print(random.choice(list1));
s1 = "SaiRamKumar";
print(random.choice(s1));
tup1 = (10,20,30,40,50);
print(random.choice(tup1));
#set1 = {1,2,3,4,5};
#print(random.choice(set1));	#set does not have indexes
'''

'''
##randrange(start,end,step)
import random;
print(random.randrange(10,100,2));
print(random.randrange(3,100,3));
print(random.randrange(-20,-1));
#print(random.randrange(-1,-100));  #Empty-range
'''

'''
#random() #0 to 1(not-included)
import random;
print(random.random());
print(random.random());
'''

'''
#shuffle()
import random;
list1 = [10, 20, 30, 40,50];
random.shuffle(list1)
print(list1);
random.shuffle(list1)
print(list1);



#uniform()
import random
print(random.uniform(1,5));
print(random.uniform(11,15));




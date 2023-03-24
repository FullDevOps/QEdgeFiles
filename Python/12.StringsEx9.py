##Program (StringsEx9.py)
#Program to work with string formats with print() using {} & format()


#case-1
rno=1001;
name="Sai";
height=6.0;
print("RollNo : {}\nName: {}\nHeight: {}".format(rno,name,height));


#case-2
print();
rno=1001;
name="Sai";
height=6.0;
#using-indexes
print("RollNo : {0}\nName:{1}\nHeight: {2}".format(rno,name,height));

#case-3
#using-vars (we can change the order)
rno=1001;
name="Sai";
height=6.0;
print("RollNo : {x}\nName: {y}\nHeight: {z}".format(x=rno,y=name,z=height));
print("RollNo : {x}\nName: {y}\nHeight: {z}".format(y=name,z=height,x=rno));


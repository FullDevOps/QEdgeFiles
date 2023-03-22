##Program MathFuncs.py
##(Program to demo different Mathematical-Functions)

import math;

#abs() function
print(abs(-9));
print(abs(9));
print(abs(0));
print(abs(-0));
print(abs(-9.5));
print(abs(9.5));
print(abs(0.0));
print(abs(-0.0));
'''

'''
#ceil() function (upper/next int-value)
from math import ceil;  #.dot is not-req
print(ceil(9.8));
print(ceil(9.2));
print(ceil(9.0));
print(ceil(9));
print(ceil(-9));
'''

'''
import math;
print(math.ceil(-9.8));
print(math.ceil(-9.2));
print(math.ceil(-9.0));
print(math.pi);
print(math.ceil(math.pi));
'''

'''
#exp() function (e--->Euler's number)
import math;
print(math.exp(3));
print(math.exp(-3));
print(math.exp(3.5));
print(math.exp(-3.5));
print(math.exp(0));
print(math.exp(1));		
#We get exact e-value(2.718281828459045)
'''

'''
#fabs() function
import math;
print(math.fabs(3));
print(math.fabs(-3));
print(math.fabs(3.5));
print(math.fabs(-3.5));
print(math.fabs(0));
print(math.fabs(-0));
'''

'''
#floor() function (lower/prev int-value)
from math import floor;
print(floor(9.8));
print(floor(9.2));
print(floor(9.0));
print(floor(9));
print(floor(-9));
'''
'''
import math;
print(math.floor(-9.8));
print(math.floor(-9.2));
print(math.floor(-9.0));
print(math.pi);
print(math.floor(math.pi));
'''

'''
#log() function (base-e)
import math;
print(math.exp(1));		#We get exact e-value
print(math.log(math.exp(1)));	#e power 0 is 1
print(math.log(10));
#print(math.log(-10));	#Error
print(math.log(10.5));
'''

'''
#log10() function (log value to base-10)
import math;
print(math.log10(10));
#print(math.log10(-10));	#ValueError
print(math.log10(10.5));
print(math.log10(1));
'''

'''
#max() function
print(max(10,20,30));
print(max(-10,-20,-30));
print(max(10.5,20.5,30.5));
print(max(-10.5,-20.5,-30.5));
'''

'''
#min() function
print(min(10,20,30));
print(min(-10,-20,-30));
print(min(10.5,20.5,30.5));
print(min(-10.5,-20.5,-30.5));
'''

'''
#modf() function(tuple())
import math;
print(math.modf(10.56));
print(math.modf(-10.56));
print(math.modf(10));
print(math.modf(-10));
print(math.modf(0));
print(math.modf(0.0));
'''

'''
#pow() function
import math;
print(math.pow(10,3));
print(math.pow(10,-3));
print(math.pow(100,0.5));	#it is 10 power 0.5(1/2) i.e. sqrt(100)
'''

'''
#round() function
print(round(10.12345,3));
print(round(10.12345,4));
print(round(12345.12345,-3));
print(round(12345.12345,-2));	
print(round(12345.12345,-1));
print(round(12545.12345,-3));
print(round(10.123));
print(round(10.789));
'''

'''
#sqrt() function
import math;
print(math.sqrt(100));
print(math.sqrt(10.56));
print(math.sqrt(-10));		#ValueError


#factorial() function
import math
print(math.factorial(5))
print(math.factorial(6))


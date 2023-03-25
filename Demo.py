# D:\QEdgeFiles\DJango\Demo.py

print(__file__)	

print()
import os
print(os.path.abspath(__file__))

print()
print(os.path.dirname(os.path.abspath(__file__)))

print()

import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__)) 
TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
print(TEMPLATE_DIR)
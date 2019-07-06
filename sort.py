import os
import re
from more_itertools import consecutive_groups

current = os.getcwd()

files = os.listdir(current)

#Getting files with 4 or more digits 
pattern = re.compile("\d{4,}")
a = [int((pattern).search(x).group(0)) for x in files if pattern.search(x)]

#Getting other files
b = [x for x in files if not re.search(r'\d',x)]

#Getting the image folder name
c = os.path.split(current)

#Group consecutive numbers together
cons_groups = [list(group) for group in consecutive_groups(a)]

#Create result list
result = [[len(x), '{}-{}'.format(x[0], x[-1])] for x in cons_groups]

#Print the image file sequences
for item in result:
    print('{} {}.%04d.jpg {}'.format(item[0],c[-1], item[1]))

#printing other files 
for i in b:
    print(1, i) 



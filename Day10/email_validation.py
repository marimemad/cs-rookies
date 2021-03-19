 
import re

n=input()
for i in range(int(n)):
    line=input()
    name,email=line.split(' ')
    pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern,email)):
        print (name,email)

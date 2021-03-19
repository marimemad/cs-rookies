import random
import string
import re

if __name__=='__main__':
    
    choices= string.ascii_letters + string.digits +'@#$%&'
    password= ''.join([random.choice(choices) for i in range(10)])
    
    valid=False
    
    while not valid:
        validation={'lower_letters':re.findall("[a-z]", password), 'upper_letters':re.findall("[A-Z]", password), 'digits':re.findall("\d", password), 'characters': [i for i in password if i in  ['@','#', '%', '$', '&']]}
        
        if not (validation['lower_letters'] and  validation['upper_letters'] and  validation['digits'] and  validation['characters']):
            password= ''.join([random.choice(choices) for i in range(10)])
        else:
            valid=True
        
    print(password)
    
            

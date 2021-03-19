import re

if __name__=='__main__':
    passwword=input()
    
    valid=False
    while not valid:
        validation={'lower_letters':re.findall("[a-z]", passwword), 'upper_letters':re.findall("[A-Z]", passwword), 'digits':re.findall("\d", passwword), 'characters': [i for i in passwword if i in  ['@','#', '%', '$', '&']]}
        
        if not validation['lower_letters']:
            print('not valid! pleasc enter lower case letters')
            passwword=input()
            
        elif not validation['upper_letters']:
            print('not valid! pleasc enter upper case letters')
            passwword=input()
            
        elif not validation['digits']:
            print('not valid! pleasc enter numbers')
            passwword=input()
            
        elif not validation['characters']:
            print('not valid! pleasc enter characters like @ # % $ &')
            passwword=input()
            
        else:
            valid=True
            
        
        
    print('valid')

operator={'+':1, '-':1 ,'/':2 ,'*':2 ,'%':2 , '^':3}

def infix_to_postfix(exp_in_infix):
    stack=[]
    exp_in_postfix=''
    
    for char in exp_in_infix:
            
        if char=='(':
            stack.append('(')
        elif char==')':
            while (stack and stack[-1]!='('):
                exp_in_postfix+=stack.pop()
            stack.pop()
        
        
        elif char.isdigit() or char.isalpha() or char==' ':
            exp_in_postfix+=char 
        
        else :
            while (stack and stack[-1]!='(' and (not operator[char]>operator[stack[-1]] )):
                exp_in_postfix+=stack.pop()
                        
                
            stack.append(char)
                
                    
    while stack:
        exp_in_postfix+=stack.pop()
        
    return(exp_in_postfix)


def postfix_to_infix(exp):
    stack=[]
    for char in exp:
        
        if char not in operator:
            stack.append(char)
        
        else:
            
            operand1=stack.pop()
            operand2=stack.pop()
            
            stack.append('('+operand2+char+operand1+')')
            
    return(stack[0]) 



def evaluation_exp_in_postfix(exp):
    stack=[]
    for char in exp:
        
        if char not in operator:
            stack.append(char)
        
        else:
            
            operand1=stack.pop()
            operand2=stack.pop()
            
            stack.append(str(eval(operand2+char+operand1)))
            
    return(stack[0]) 




if __name__=='__main__': 
    x=postfix_to_infix('382/+5-')
    print(x)
    print(evaluation_exp_in_postfix('382/+5-'))

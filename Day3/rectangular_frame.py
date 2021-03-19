
if __name__ == '__main__':
    
    string=input('Enter your sentence : ')
    string=string.split()
    words_len=[len(word) for word in string]
    width='*'*(max(words_len)+4)
    
    print(width)
    
    for word in string:
        x=word.ljust(max(words_len)+1)
        print('* '+x+'*')
    
    print(width)
    

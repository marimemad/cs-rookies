from googlesearch import search

if __name__=='__main__':
    query=input()
    result=search(query,tld="co.in", num=10, stop=10,pause=2)
    for i in result:
        print(i)

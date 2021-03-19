#include <iostream>
#include <cstring>

using namespace std;


int main()
{
    string word;
    cin>>word;
    int len =word.length();
    
    char letters[len+1];
    strcpy(letters, word.c_str());
    
    string re_word;
    
    for(int i = len-1; i>=0; i--){
        re_word=re_word+letters[i];
   }
    cout<<re_word<<endl;
    if (word==re_word){
        cout<<"the word palindrome"<<endl;
    }
    else{
        cout<<"the word not palindrome"<<endl;
    }
    return 0;
}

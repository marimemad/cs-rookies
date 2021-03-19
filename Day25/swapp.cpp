#include <iostream>
#include <cstring>

using namespace std;


int main()
{
    int x,y;
    cout<<"x: ";
    cin>>x;
    
    cout<<"y: ";
    cin>>y;
    
    int *p_x=&x , *p_y=&y;
    int temp=x;
    x=*p_y;
    y=temp;
    
    
    cout<<"afer swapping"<<endl;
    cout<<"x: "<<x<<endl;
    cout<<"y: "<<y<<endl;
    
    return 0;
}
 

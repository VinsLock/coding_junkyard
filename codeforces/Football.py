n = input()
if '1111111' in n or '0000000' in n:
    print("YES")
else:
    print("NO")
    
"""
C++

#include<iostream>

using namespace std;

int main(){
    string s1;
    cin>>s1;
    int condition = 1;
    for(int i=1; i<=s1.length(); i++){
        if(s1[i] == s1[i-1]){
            condition++;
            if(condition==7){
                cout<<"YES"<<endl;
                return 0;
            }
        }else{
            condition=1;
        }
        
    }
    cout<<"NO"<<endl;
    return 0;
}
"""
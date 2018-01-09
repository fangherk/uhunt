#include <iostream>
using namespace std;

int main(){

    ios::sync_with_stdio(false);
    int TC, a, b, c, count;
    cin >> TC;

    count = 1;
    
    while(TC--){
        cin >> a >> b >> c;

        if ( (a > b && b > c) ||(a < b && b < c) ){
            cout << "Case " << count  << ": " << b << endl;
        } else if ( (b > a && a > c) || (b < a && a < c)){
            cout << "Case " << count  << ": " << a << endl;
        } else{
            cout << "Case " << count << ": " << c << endl;
        }
        ++ count;
        
    }

    return 0;
}

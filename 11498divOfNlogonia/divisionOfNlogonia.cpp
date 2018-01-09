#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    
    int TC, x, y, px, py;
    cin >> TC;
    
    while(TC !=0)
    {
        cin >> x >> y;
        while(TC--){
            cin >> px >> py;
            if (x == px|| y ==py){
                cout << "divisa\n";
            }else if ( px > x && py > y){
                cout << "NE\n";
            }else if ( px > x && py < y){
                cout << "SE\n";
            }else if ( px < x && py > y){
                cout <<"NO\n";
            }else if ( px < x && py < y){
                cout <<"SO\n";
            }
        }
        cin >> TC;
    }
        
    return 0;
    
}


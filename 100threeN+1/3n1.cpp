#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int cycle(int n)
{
    int cycle = 0;
    while (n != 1){
        if(n%2 == 1){
            n = 3*n + 1;
        }else{
            n = n >> 1 ;
        }
        ++cycle;
    }
    return ++cycle;
}


int main(){
    unsigned int i, j, ccLength, placeHolder;

    while(cin >> i >> j){
        unsigned int i2, j2;
        i2 = i <=j ? i: j;
        j2 = i <=j ? j: i;
        ccLength = 0;
        for(int val = i2; val <= j2; ++val){
            placeHolder = cycle(val);
            if(placeHolder > ccLength){
                ccLength = placeHolder;
            }
        }

        cout << i << " " << j << " " << ccLength << "\n";
    }
    

    // while( scanf("%d %d", &i, &j) != EOF){
    //     int temp_i = i;
    //     int temp_j = j;
        
    //     if (temp_i > temp_j) swap(temp_i,temp_j);
        
    //     ccLength = 0;
        
    //     for(int vals = temp_i; vals <= temp_j; ++vals){
    //         placeHolder = cycle(vals);
    //         if (placeHolder > ccLength){
    //             ccLength = placeHolder;
    //         }
    //     }
    //     printf("%d %d %d\n", i, j, ccLength);
    // }

    
    return 0;
}



// int main(){
//     int n;
//     cin >> n;
//     cout << n << " ";

//     while (n!=1)
//         if(n%2!=0){
//             n = 3*n + 1;
//         }else{
//             n = n/2;
//         }
//         cout << n << " ";
//     }
// }


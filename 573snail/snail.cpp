#include <iostream>
using namespace std;

int main(){

  float H, U, D, F;
  cin >> H >> U >> D >> F;  
  while(H){
    int day = 0;
    double climbed = 0;
    bool succeeded = 0;
    double drop = (F/100)*U;

    // cout << drop << endl;
    // cout << "H: "<< H << " U: "<< U << " D: "<<  D << " F: " << F << endl;
    do{
      day += 1;
      // cout << "day " << day << endl;
      climbed += U;
      // cout << "distance climbed: " << climbed << endl;
      if(climbed > H){
        succeeded = 1;
        cout << "success on day " << day << endl;
        break;
      }

      climbed -= D;
      // cout << "after drop: " << climbed << endl;
      if(climbed < 0){
        cout << "failure on day " << day << endl;        
        break;
      }
      U -= drop;
      // cout << "distance chaange: " << U << endl;
      if(U <0){
        U = 0;
      }


    }while(true);
    
    cin >> H >> U >> D >> F;
  }
  
  return 0;
}


#include <iostream>
#include <cstdio>

using namespace std;

int main(){
  int ppl,budget, numHotels, numWeeks;
  while(scanf("%d %d %d %d", &ppl, &budget, &numHotels, &numWeeks) !=EOF){
    int minCost = budget + 1;
    while(numHotels--){
      int price, weekend;
      scanf("%d", &price);
      for(int i=0; i<numWeeks; ++i){
        scanf("%d", &weekend);

        if(ppl <= weekend && price * ppl <= budget){
          if( price * ppl <= minCost){
            minCost = price*ppl;
          }
        }
      }
    }
    if(minCost == budget + 1){
      printf("stay home\n");
    }else{
      printf("%d\n", minCost);
    }
  }
}

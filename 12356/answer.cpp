#include <cstdio>

int leftBuddies[100005];
int rightBuddies[100005];
int soldiers, tests;
int l, r;

int main(){

    
    while(scanf("%d %d", &soldiers, &tests), (soldiers || tests)){
        
        for(int i = 0; i < soldiers + 1; i++){
           leftBuddies[i] = i - 1; 
           rightBuddies[i] = i + 1; 
        }

        for(int j = 0; j < tests; j++){
            scanf("%d %d", &l, &r);
            // printf("%d %d", l, r);

            if(leftBuddies[l] < 1){
                printf("* ");
            }else{
                printf("%d ", leftBuddies[l]);
            }
                
            if(rightBuddies[r] > soldiers){
                printf("*\n");
            }else{
                printf("%d\n", rightBuddies[r]);
            }

            leftBuddies[rightBuddies[r]] = leftBuddies[l];
            rightBuddies[leftBuddies[l]] = rightBuddies[r];

        }
        printf("-\n");
    }

}

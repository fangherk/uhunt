#include <cstdio>
#include <cstring>

int main(){

    int start, num1, num2, num3;
    while( scanf("%d %d %d %d", &start, &num1, &num2, &num3) && (start || num1 || num2 || num3)){

        int two_full_turns = 720;
        int first_angle = (start - num1 > 0) ? (start-num1):(start +40-num1);
        first_angle = first_angle * 9;
        int counter_clockwise = 360;
        int second_angle = (num2 - num1 > 0) ? (num2-num1):(num2+40-num1);
        second_angle = second_angle * 9;
        int third_angle = (num2 - num3 > 0) ? (num2-num3):(num2+40-num3);
        third_angle = third_angle * 9;
        int total_sum = two_full_turns + first_angle + counter_clockwise + second_angle + third_angle;
//        printf("1:%d 2:%d 3:%d", first_angle, second_angle, third_angle);
        printf("%d\n", total_sum);
    }



    return 0;
}

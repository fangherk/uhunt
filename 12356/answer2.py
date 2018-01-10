from sys import stdin 


def main():
   
    test_case = stdin.readline().split()
    
    while test_case != ["0", "0"]:
        num_soldiers, tests = test_case 
        num_soldiers = int(num_soldiers)
        left_buddies = list(range(0, num_soldiers+10))
        right_buddies = list(range(2, num_soldiers+12))

        for i in range(int(tests)):
            # Get soldier losses
            left_loss, right_loss = stdin.readline().split()
            left_loss = int(left_loss)
            right_loss = int(right_loss)

            # Update soldiers
            buddy_l = left_loss - 1
            buddy_r = right_loss + 1
            
            soldiers_length = range(1, num_soldiers+1)
            
            left_most = left_buddies[left_loss-1]
            right_most = right_buddies[right_loss-1]
            if buddy_l not in soldiers_length or left_most not in soldiers_length:
                left_survive = "*"
            else:
                left_survive = left_most 
            
            if buddy_r not in soldiers_length or right_most not in soldiers_length:
                right_survive = "*"
            else:
                right_survive = right_most 
            
            left_buddies[right_buddies[right_loss-1]-1] = left_buddies[left_loss-1]
            right_buddies[left_buddies[left_loss-1]-1] = right_buddies[right_loss-1]


            loss_report = "{} {}".format(left_survive, right_survive)
            print(loss_report)
                

        print("-")
        test_case = stdin.readline().split()

if __name__ == "__main__":
    main()

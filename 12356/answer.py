from sys import stdin 


def remaining(soldiers: list, direction: str, buddy: int):
    soldiers_length = range(0, len(soldiers))
    counter = buddy - 1

    if direction == "LEFT":
        while counter in soldiers_length:
           if soldiers[counter] == True:
               return counter + 1
           counter -= 1 
        return "*"
    elif direction == "RIGHT":
        while counter in soldiers_length:
           if soldiers[counter] == True:
               return counter + 1
           counter += 1 
        return "*"
    else:
        print("oops")


def main():
   
    test_case = stdin.readline().split()
    
    while test_case != ["0", "0"]:
        num_soldiers, tests = test_case 
        soldiers = [True] * int(num_soldiers)
        
        for i in range(int(tests)):
            # Get soldier losses
            left_loss, right_loss = stdin.readline().split()
            left_loss = int(left_loss)
            right_loss = int(right_loss)

            # Remove soldiers
            for idx in range(left_loss - 1, right_loss):
                soldiers[idx] = False

            # Find remaining soldier
            buddy_l = left_loss - 1
            buddy_r = right_loss + 1
            

            soldiers_length = range(1, len(soldiers)+1)
            if buddy_l not in soldiers_length:
                left_survive = "*"
            else:
                left_survive = remaining(soldiers, "LEFT", buddy_l)
            
            if buddy_r not in soldiers_length:
                right_survive = "*"
            else:
                right_survive = remaining(soldiers, "RIGHT", buddy_r)

            loss_report = "{} {}".format(left_survive, right_survive)
            print(loss_report)
                

        print("-")
        test_case = stdin.readline().split()

if __name__ == "__main__":
    main()

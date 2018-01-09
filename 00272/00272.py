from sys import stdin

def main():

    coin = True
    for line in stdin:
        for word in line:
            for char in word:
                if char == '"':
                    if coin:
                        print('``', end = '')
                    else:
                        print("''", end = '')
                    coin = not coin 
                else:
                    print(char, end = '')

if __name__ == "__main__":
    main()

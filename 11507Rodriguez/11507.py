from sys import stdin


def main():
    length = int(stdin.readline())

    while length != 0:
        directions = stdin.readline().split()
        final = '+x'
        for val in directions:
            if val == "No":
                final = final
            # x hardcoded
            elif final == '+x' and val == "+y":
                final = '+y'
            elif final == '+x' and val == "-y":
                final = '-y'
            elif final == '+x' and val == "+z":
                final = '+z'
            elif final == '+x' and val == "-z":
                final = '-z'
            # -x hardcoded
            elif final == '-x' and val == "+y":
                final = '-y'
            elif final == '-x' and val == "-y":
                final = '+y'
            elif final == '-x' and val == "+z":
                final = '-z'
            elif final == '-x' and val == "-z":
                final = '+z'
            # -y hardcoded
            elif final == '-y' and val == "+y":
                final = '+x'
            elif final == '-y' and val == "-y":
                final = '-x'
            elif final == '-y' and val == "+z":
                final = '-y'
            elif final == '-y' and val == "-z":
                final = '-y'
            # +y hardcoded
            elif final == '+y' and val == "+y":
                final = '-x'
            elif final == '+y' and val == "-y":
                final = '+x'
            elif final == '+y' and val == "+z":
                final = '+y'
            elif final == '+y' and val == "-z":
                final = '+y'
            # -z hardcoded
            elif final == '-z' and val == "+y":
                final = '-z'
            elif final == '-z' and val == "-y":
                final = '-z'
            elif final == '-z' and val == "+z":
                final = '+x'
            elif final == '-z' and val == "-z":
                final = '-x'
            # +z hardcoded
            elif final == '+z' and val == "+y":
                final = '+z'
            elif final == '+z' and val == "-y":
                final = '+z'
            elif final == '+z' and val == "+z":
                final = '-x'
            elif final == '+z' and val == "-z":
                final = '+x'
        print(final)

        length = int(stdin.readline())


if __name__ == "__main__":
    main()
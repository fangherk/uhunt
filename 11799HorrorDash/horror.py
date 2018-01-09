from sys import stdin, stdout


def main():
    cases = stdin.readline()

    for case in range(int(cases)):
        line = stdin.readline().split()
        largest = 0

        for vals in line[1:]:
            if int(vals) > int(largest):
                largest = vals
        stdout.write("Case {}: {}\n".format(case + 1, largest))


if __name__ == "__main__":
    main()

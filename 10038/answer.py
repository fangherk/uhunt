from sys import stdin

def jollyCheck(size: int, inputs: list):
    diffs = []
    for idx, val in enumerate(inputs[:-1]):
        abs_diff = int(val) - int(inputs[idx+1])
        diffs.append(abs(abs_diff))

    diffs = sorted(diffs)

    counter = 0 
    while counter < len(diffs):
        if counter + 1  != diffs[counter]:
            return False
        counter += 1

    return True

def main():
    lines = stdin.readline()

    while lines:
        lines = lines.split()
        num_elem = int(lines[0])
        solution = jollyCheck(num_elem, lines[1:])
        if solution:
            print("Jolly")
        else:
            print("Not jolly")
        lines = stdin.readline()

if __name__ == "__main__":
    main()

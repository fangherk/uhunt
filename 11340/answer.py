from sys import stdin


def parse_line(sentence: list, costs: dict):
    temp_cost = 0
    for word in sentence:
        for char in word:
            if char in costs:
                temp_cost += costs[char]  
    return temp_cost
                

def article_format(line_cost):
    temp = str(line_cost)
    
    if len(temp) == 1:
        return "0.0{}$".format(line_cost)
    elif len(temp) == 2:
        return "0.{}$".format(line_cost)
    else:
        return "{}.{}{}$".format(temp[:-2], temp[-2], temp[-1])
         
def main():

    tests = int(stdin.readline())
    
    while tests != 0:
        total_cost = 0
        num_costs = int(stdin.readline())
        fresh_costs = {}
        
        # get the dictionary values
        for i in range(num_costs):
            word, val = stdin.readline().split()
            fresh_costs[word] = int(val)

        
        num_lines = int(stdin.readline())
        
        for i in range(num_lines):
            sentence = stdin.readline().split()
            line_cost = parse_line(sentence, fresh_costs)
            total_cost += line_cost
        
        print(article_format(total_cost))

        tests -= 1

        

if __name__ == "__main__":
    main()

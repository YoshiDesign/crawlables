#! /usr/env/bin/python3.7

def main():


    fp  = open("US.txt", "r")
    fw  = open("US_norepeat.txt", "a+")

    already_visited = {}

    for line in fp.readlines():
        ar = line.split('\t')
        state = ar[3]
        try:    
            err = already_visited[state]
        except KeyError:
            already_visited[state] = []
       
        city = ar[2]

        if city in already_visited[state]:
            pass
        else:
            fw.write(line)
            already_visited[state].append(city)


    fp.close()
    fw.close()

if __name__ == "__main__":
    main()
#! /usr/env/bin/python3.7
from os import listdir

def old():

    for s_name in listdir("SCR_1"):
        check = s_name.split("_")
        for i in range(len(check)):
            if check[i] == "SCR.html":
                check[i] = "TAB.html"
        
        find_me = "_".join(check)


        for t_name in listdir("TAB_1"):
            found = False

            if t_name == find_me:
                found = True
                break
        
        if found:
            found = False
        else:
            print(f"Failed to find {find_me}")


def main():

    


if __name__ == "__main__":
    main()
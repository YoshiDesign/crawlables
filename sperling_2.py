#! /usr/env/bin/python3.7
from os import listdir
def main():

    tdir = "./TEST"
    sort_files = sorted(listdir(tdir))

    for f in sort_files:
        segs = f.split('_')

        if len(segs) > 4:
            if segs[1] == "district":
                current_state = "district_of_columbia"
                current_city = segs[4]
            else:
                state_name = f"{segs[1]}_{segs[2]}"
                print(state_name)

if __name__ == "__main__":
    main()
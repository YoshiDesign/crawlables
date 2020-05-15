#! /usr/env/bin/python3.7

# Generated json_scr_REDUX

from os import listdir
def main():

    scr_fp = open("json_scr_REDUX.json", "a+")

    states_visited = []
    current_state = "BEGIN"
    s_key = "|-|-| "
    j_app = ""
    tdir = "SCR_1/"
    sort_files = sorted(listdir(tdir))
    checks = ['new', 'north', 'south', 'west', 'rhode']

    # For each file_name
    for name in sort_files:

        segs = name.split('_')
        if len(segs) > 4:

            if len(segs) == 5 and segs[1] not in checks:
                # SINGLE STATE NAME, 2-PART CITY NAME
                current_state = f"{segs[1]}"
                current_city = f"{segs[2]}_{segs[3]}"
                pass
            elif len(segs) == 5:
                # MULTI STATE NAME, SINGLE CITY NAME
                current_state = f"{segs[1]}_{segs[2]}"
                current_city = f"{segs[3]}"
                pass

            if len(segs) == 6 and segs[1] not in checks:
                # SINGLE STATE NAME, 3-PART CITY NAME
                current_state = f"{segs[1]}"
                current_city = f"{segs[2]}_{segs[3]}_{segs[4]}"
                pass
            elif len(segs) == 6:
                # 2-PART STATE NAME, 2-PART CITY NAME
                current_state = f"{segs[1]}_{segs[2]}"
                current_city = f"{segs[3]}_{segs[4]}"
                pass

            if len(segs) == 7 and segs[1] not in checks:
                # SINGLE STATE NAME, 4-PART CITY NAME
                current_state = f"{segs[1]}"
                current_city = f"{segs[2]}_{segs[3]}_{segs[4]}_{segs[5]}"
                pass
            elif len(segs) == 7:
                # 2-PART STATE NAME, 3 PART CITY NAME
                current_state = f"{segs[1]}_{segs[2]}"
                current_city = f"{segs[3]}_{segs[4]}_{segs[5]}"
                pass

            if len(segs) == 8 and segs[1] not in checks:
                # King and Queen Court House - VA
                # print("KING AND QUEEN")
                current_state = f"{segs[1]}"
                current_city = f"{segs[2]}_{segs[3]}_{segs[4]}_{segs[5]}_{segs[6]}"
                pass
            elif len(segs) == 8 :
                # print("8 LEN")
                # 2 PART STATE NAME, 4 PART CITY NAME
                current_state = f"{segs[1]}_{segs[2]}"
                current_city = f"{segs[3]}_{segs[4]}_{segs[5]}_{segs[6]}"
                print(current_city)
                pass

        else:
            current_city = name.split('_')[2].lower()
            current_state = name.split('_')[1].lower()

        # print(f"Current city : {current_city}")

        # Get our current state key
        if current_state not in states_visited:
        
            if not states_visited :
                # OPEN
                print("EMPTY")
                scr_fp.write("{" +'\"' + current_state + '\"' + ": [")
            
            else : 
                # NEXT
                scr_fp.write("] ,\n " +'\"' + current_state + '\"' + ": [")

            states_visited.append(current_state)
            # print(f"Switching States to {current_state}")
            # print("All States Visited")
            # print(states_visited)

        with open("./" + tdir + name, "r") as fp:
            for line in fp.readlines():

                check_city = current_city.split("_")
                if len(check_city) > 1:
                    current_city = " ".join(check_city)

                if current_city.title() in line:
                    scr_fp.write(s_key + line.lstrip() + "|;|,")

    # CLOSE
    scr_fp.write("]}")
    scr_fp.close()
    # with open("./TEST/ww_alabama_abbeville_TAB.html") as fp:
    #    for line in fp.readlines():
    #     if "" in line:


if __name__ == "__main__":
    main()
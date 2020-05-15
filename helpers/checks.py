#! /usr/env/bin/python3.7
def check_s(f):

    checks = ['new', 'north', 'south', 'west', 'rhode']

    segs = f.split("_")
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

            current_state = f"{segs[1]}"
            current_city = f"{segs[2]}_{segs[3]}_{segs[4]}_{segs[5]}_{segs[6]}"
            pass
        elif len(segs) == 8 :

            # 2 PART STATE NAME, 4 PART CITY NAME
            current_state = f"{segs[1]}_{segs[2]}"
            current_city = f"{segs[3]}_{segs[4]}_{segs[5]}_{segs[6]}"
            print(current_city)
            pass

    else:
        current_city = f.split('_')[2].lower()
        current_state = f.split('_')[1].lower()

    return [current_city, current_state]
    
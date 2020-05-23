#! /usr/bin/env/python3.7

import json

def main():

    j = open("col_5.json", "r")
    col_json = json.loads(j.read())

    us = open("US_norepeat.txt", "r")
    for line in us.readlines():

        items = line.split("\t")
        latt = items[9]
        lon = items[10]
        city = items[2]
        abbr = items[4]
        stat = items[3]

        norm_stat_1 = stat.split(" ")
        if len(norm_stat_1) > 1:
            stat = "_".join(norm_stat_1)
        stat = stat.lower()

        if stat == "district_of_columbia" or abbr == "FM" or stat == "":
            continue

        norm_city_1 = city.split(" ")
        if len(norm_city_1) > 1:
            city = "_".join(norm_city_1)
        city = city.lower()

        current_state = col_json[stat]
        print(f"Updating: {current_state['meta']['name']} - {current_state['meta']['abrv']} - {current_state['meta']['id']}")
        for c in current_state['cities']:
            if c["c_name"] == city:
                c["coord"] = {
                    "lat" : latt,
                    "lon" : lon
                }
                print(f"{city}, {stat}\t{latt}\t{lon}")

        # except Exception as e:
        #     j.close()
        #     print(f"OH NOES----------------------\n{e}")
        #     exit()

    fw = open("col_6.json","w")
    fw.write(json.dumps(col_json,indent=4))
    fw.close()
    j.close()

if __name__ == "__main__":
    main()
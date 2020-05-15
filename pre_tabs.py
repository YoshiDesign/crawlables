#! /usr/env/bin/python3.7
from os import listdir
from random import randint
from helpers import check_s

import json

n = 1
count = 0

def main():

    """

    This file will construct:
        State Meta and rent values
        City Meta and rent values


    #
    # # STATES AND CITIES COST OF LIVING
    #
        {
            "alabama" : {
                "meta" : {
                    "id" : 0,
                    "abrv" : AL,
                    "name" : "name"
                },
                "avgs" : {
                    "col" : 000,
                    "rnt" : [],
                },
                "cities" : [
                    {
                        "c_name" : "city_name", 
                        "c_id" : "abc123",
                        "state_id" : 0,
                        "scr_rent" : [],
                        "tab_col" : {
                            "gro" : 000,        # groceries
                            "hea" : 000,        # healthcare
                            "hou" : 000,        # Housing
                            "uti" : 000,        # Utilities
                            "tra" : 000,        # Transportation
                            "ent" : 000         # Miscellaneous, entertainment and whatnot
                        },
                        "tab_m" : {
                            "ove" : 000,        # Overall CoL index score compared to 100 (US Average)
                            "mhc" : 000,        # Median Home Cost $00.0000
                        },
                        "" : 
                    },
                    [...],
                    [...]
                ]
            }
        }

    #
    # # BLS DATA
    #

    {

    }

    """

    # <u>Overall</u>
    # <u>Grocery</u>
    # <u>Health</u>
    # <u>Housing</u>
    # <u>Median Home Cost</u>
    # <u>Utilities</u>
    # <u>Transportation</u>
    # <u>Miscellaneous</u>


    states = {
        "alabama" : [1,"AL", "alabama"],
        "alaska" : [2,"AK", "alaska"],
        "arizona" : [3,"AZ", "arizona"],
        "arkansas" : [4,"AR", "arkansas"],
        "california" : [5,"CA", "california"],
        "colorado" : [6,"CO", "colorado"],
        "connecticut" : [7,"CT", "connecticut"],
        "delaware" : [8,"DE", "delaware"],
        "district_of_columbia" : [9,"DC", "district_of_columbia"],
        "florida" : [10,"FL", "florida"],
        "georgia" : [11,"GA", "georgia"],
        "hawaii" : [12,"HI", "hawaii"],
        "idaho" : [13,"ID", "idaho"],
        "illinois" : [14,"IL", "illinois"],
        "indiana" : [15,"IN", "indiana"],
        "iowa" : [16,"IA", "iowa"],
        "kansas" : [17,"KS", "kansas"],
        "kentucky" : [18,"KY", "kentucky"],
        "louisiana" : [19,"LA", "louisiana"],
        "maine" : [20,"ME", "maine"],
        "maryland" : [21,"MD", "maryland"],
        "massachusetts" : [22,"MA", "massachusetts"],
        "michigan" : [23,"MI", "michigan"],
        "minnesota" : [24,"MN", "minnesota"],
        "mississippi" : [25,"MS", "mississippi"],
        "missouri" : [26,"MO", "missouri"],
        "montana" : [27,"MT", "montana"],
        "nebraska" : [28,"NE", "nebraska"],
        "nevada" : [29,"NV", "nevada"],
        "new_hampshire" : [30,"NH", "new_hampshire"],
        "new_jersey" : [31,"NJ", "new_jersey"],
        "new_mexico" : [32,"NM", "new_mexico"],
        "new_york" : [33,"NY", "new_york"],
        "north_carolina" : [34,"NC", "north_carolina"],
        "north_dakota" : [35,"ND", "north_dakota"],
        "ohio" : [36,"OH", "ohio"],
        "oklahoma" : [37,"OK", "oklahoma"],
        "oregon" : [38,"OR", "oregon"],
        "pennsylvania" : [39,"PA", "pennsylvania"],
        "puerto_rico" : [40,"PR", "puerto_rico"],
        "rhode_island" : [41,"RI", "rhode_island"],
        "south_carolina" : [42,"SC", "south_carolina"],
        "south_dakota" : [43,"SD", "south_dakota"],
        "tennessee" : [44,"TN", "tennessee"],
        "texas" : [45,"TX", "texas"],
        "utah" : [46,"UT", "utah"],
        "vermont" : [47,"VT", "vermont"],
        "virginia" : [48,"VA", "virginia"],
        "washington" : [49,"WA", "washington"],
        "west_virginia" : [50,"WV", "west_virginia"],
        "wisconsin" : [51,"WI", "wisconsin"],
        "wyoming" : [52,"WY", "wyoming"]
    }

    global n
    global count
    fp_redux = open("json_scr_REDUX.json", "r")
    file_names = listdir("SCR_1/")
    bads = {}
    bajo = json.loads(fp_redux.read())
    already_visited = []
    pf = ["a", "b", "c", "d", "e", "x", "f"]
    
    for name in file_names:

        c_s = check_s(name)
        city  = c_s[0]
        state = c_s[1]

        # If we haven't looked at this state yet
        if visit(already_visited, state):
            pass
        else: # set-up us its data

            # Base object per state entry
            bads[state] = {"meta":{},"avgs":{},"cities":[]}

            if state == "district":
                continue

            ## GET DATAS STATE META
            bads[state]["meta"]["id"]   = states[state.lower()][0]
            bads[state]["meta"]["abrv"] = states[state.lower()][1]
            bads[state]["meta"]["name"] = states[state.lower()][2]
            find_avg = bajo[state][0]

            # find the state data from our bigg ass json obj.
            for j in find_avg:
                norm_name = j["name"].split(" ")
                if len(norm_name) > 1:
                    n_name = "_".join(norm_name).lower()
                else:
                    n_name = j["name"].lower()

                if n_name == state.lower():
                    bads[state]["avgs"]["rnt"] = j["data"]
                    bads[state]["avgs"]["col"] =  "TODO" # TODO

        ## GET DATAS CITYS
        cur_id = states[state.lower()][0]
        for c in bajo[state]:

            count = count + 1

            obj_buffer = {
                "c_name"   : "",
                "c_id"     : 0,
                "state_id" : cur_id,
                "scr_rent" : [],
                "tab_col" : {
                    "gro" : 0,        # groceries
                    "hea" : 0,        # healthcare
                    "hou" : 0,        # Housing
                    "uti" : 0,        # Utilities
                    "tra" : 0,        # Transportation
                    "ent" : 0         # Miscellaneous, entertainment and whatnot
                },
                "tab_m" : {
                    "ove" : 0,        # Overall CoL index score compared to 100 (US Average)
                    "mhc" : 0,        # Median Home Cost $00.0000
                }
            }
            
            # Get the city data
            for item in c:
                
                check_city = city.split("_")
                if len(check_city) > 1:
                    city = " ".join(check_city)

                if item["name"].lower() == city.lower():
                    obj_buffer["c_name"] = city.lower()
                    obj_buffer["scr_rent"] = item["data"]
                    obj_buffer["c_id"] = gen_id(pf)
                    bads[state]["cities"].append(obj_buffer)
            
    # print(bads)
    outp = json.dumps(bads, indent=4, sort_keys=True)
    fp = open("pre_tabs.json", "w")
    fp.write(outp)
    print(":D")

def visit(data, check):
    if check in data:
        return True
    else:
        data.append(check)
        return False

def gen_id(pf):

    global n

    gen = str(pf[randint(0,6)]) + str(pf[randint(0,6)]) + str(pf[randint(0,6)]) + str(n)
    fin = gen.zfill(10)
    n = n + 1
    return str(fin)

if __name__ == "__main__":
    main()
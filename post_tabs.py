#! /usr/env/bin/python3.7
from os import listdir
from helpers import check_s
import json

count = 0

# 05/15/2020
# INPUT > pre_tabs.json
# OUTPT > col_5.json

def main():

    # TAB_1 File Delimiters for titles
    # <u>Overall</u>
    # <u>Grocery</u>
    # <u>Health</u>
    # <u>Housing</u>
    # <u>Median Home Cost</u>
    # <u>Utilities</u>
    # <u>Transportation</u>
    # <u>Miscellaneous</u>

    # collector = {
    #     "overall" : [],
    #     "grocery" : [],
    #     "health"  : [],
    #     "housing" : [],
    #     "median"  : [],
    #     "utilities" : [],
    #     "transportation" : [],
    #     "misc" : [],
    # }

    global count
    fp_json = open("pre_tabs_new.json", "r")
    pre_tabs = json.loads(fp_json.read())
    file_names = sorted(listdir("TAB_1/"))

    for s in pre_tabs:
        pre_tabs[s]["avgs"]["tab_col"] = {}

    for name in file_names:
        
        c_s   = check_s(name)
        city  = c_s[0]
        state = c_s[1]

        if state == "district":
            continue

        cur_file = open("TAB_1/" + name, "r")
        first_key = "" # City or state json layer
        key = ""       # Specific value in json
        splitt = "</td><td>"
        state_key   = False
        tabm        = False

        for line in cur_file.readlines():
            if "<u>Overall</u>" in line:
                row = line.split(splitt)
                cv  = row[1]
                sv  = row[2]

                # collector["overall"].append(cv)
                # collector["overall"].append(sv)

                if pre_tabs[state]["avgs"]["col"] == "TODO":
                    pre_tabs[state]["avgs"]["col"] = sv

                for i in range(len(pre_tabs[state]["cities"])):
                    get_c = pre_tabs[state]["cities"][i]["c_name"].split(" ")
                    if len(get_c) > 1:
                        city_name = "_".join(get_c)
                    else:
                        city_name = pre_tabs[state]["cities"][i]["c_name"]
                    if city_name == city:
                        count = count+1
                        pre_tabs[state]["cities"][i]["tab_m"]["ove"] = cv

            if "<u>Grocery</u>" in line:
                row = line.split(splitt)
                cv  = row[1]
                sv = row[2]

                pre_tabs[state]["avgs"]["tab_col"]["gro"] = sv

                for i in range(len(pre_tabs[state]["cities"])):
                    get_c = pre_tabs[state]["cities"][i]["c_name"].split(" ")
                    if len(get_c) > 1:
                        city_name = "_".join(get_c)
                    else:
                        city_name = pre_tabs[state]["cities"][i]["c_name"]
                    if city_name == city:
                        pre_tabs[state]["cities"][i]["tab_col"]["gro"] = cv
                # collector["grocery"].append(cv)
                # collector["grocery"].append(sv)

                key = "gro"
            if "<u>Health</u>" in line:
                row = line.split(splitt)
                cv  = row[1]
                sv = row[2]

                pre_tabs[state]["avgs"]["tab_col"]["hea"] = sv

                for i in range(len(pre_tabs[state]["cities"])):
                    get_c = pre_tabs[state]["cities"][i]["c_name"].split(" ")
                    if len(get_c) > 1:
                        city_name = "_".join(get_c)
                    else:
                        city_name = pre_tabs[state]["cities"][i]["c_name"]
                    if city_name == city:
                        pre_tabs[state]["cities"][i]["tab_col"]["hea"] = cv
                # collector["health"].append(cv)
                # collector["health"].append(sv)

                key = "hea"
            if "<u>Housing</u>" in line:
                row = line.split(splitt)
                cv  = row[1]
                sv = row[2]

                pre_tabs[state]["avgs"]["tab_col"]["hou"] = sv

                for i in range(len(pre_tabs[state]["cities"])):
                    get_c = pre_tabs[state]["cities"][i]["c_name"].split(" ")
                    if len(get_c) > 1:
                        city_name = "_".join(get_c)
                    else:
                        city_name = pre_tabs[state]["cities"][i]["c_name"]
                    if city_name == city:
                        pre_tabs[state]["cities"][i]["tab_col"]["hou"] = cv
                        
                # collector["housing"].append(cv)
                # collector["housing"].append(sv)

            if "<u>Median Home Cost</u>" in line:
                _row = line.split("</u></a>")

                first = _row[0].split("<u>")
                dirty_mhc_val = first[3]
                no_dol = dirty_mhc_val.split("$")[1]
                al_dol = no_dol.split(",")
                cv = "".join(al_dol)      # This one

                second = _row[1].split("<u>")[1]
                sr = second.split("$")[1]
                sl_dol = sr.split(",")
                sv = "".join(sl_dol)        # And this one

                pre_tabs[state]["avgs"]["mhc"] = sv
                for i in range(len(pre_tabs[state]["cities"])):
                    get_c = pre_tabs[state]["cities"][i]["c_name"].split(" ")
                    if len(get_c) > 1:
                        city_name = "_".join(get_c)
                    else:
                        city_name = pre_tabs[state]["cities"][i]["c_name"]
                    if city_name == city:
                        pre_tabs[state]["cities"][i]["tab_m"]["mhc"] = cv
                # collector["median"].append(cv)
                # collector["median"].append(sv)

            if "<u>Utilities</u>" in line:
                row = line.split(splitt)
                cv  = row[1]
                sv = row[2]

                pre_tabs[state]["avgs"]["tab_col"]["uti"] = sv

                for i in range(len(pre_tabs[state]["cities"])):
                    get_c = pre_tabs[state]["cities"][i]["c_name"].split(" ")
                    if len(get_c) > 1:
                        city_name = "_".join(get_c)
                    else:
                        city_name = pre_tabs[state]["cities"][i]["c_name"]
                    if city_name == city:
                        pre_tabs[state]["cities"][i]["tab_col"]["uti"] = cv
                # collector["utilities"].append(cv)
                # collector["utilities"].append(sv)

                key = "uti"
            if "<u>Transportation</u>" in line:
                row = line.split(splitt)
                cv  = row[1]
                sv = row[2]

                pre_tabs[state]["avgs"]["tab_col"]["tra"] = sv

                for i in range(len(pre_tabs[state]["cities"])):
                    get_c = pre_tabs[state]["cities"][i]["c_name"].split(" ")
                    if len(get_c) > 1:
                        city_name = "_".join(get_c)
                    else:
                        city_name = pre_tabs[state]["cities"][i]["c_name"]
                    if city_name == city:
                        pre_tabs[state]["cities"][i]["tab_col"]["tra"] = cv
                # collector["transportation"].append(cv)
                # collector["transportation"].append(sv)

                key = "tra"
            if "<u>Miscellaneous</u>" in line:
                row = line.split(splitt)
                cv  = row[1]
                sv = row[2]

                pre_tabs[state]["avgs"]["tab_col"]["ent"] = sv

                for i in range(len(pre_tabs[state]["cities"])):
                    get_c = pre_tabs[state]["cities"][i]["c_name"].split(" ")
                    if len(get_c) > 1:
                        city_name = "_".join(get_c)
                    else:
                        city_name = pre_tabs[state]["cities"][i]["c_name"]
                    if city_name == city:
                        pre_tabs[state]["cities"][i]["tab_col"]["ent"] = cv
                        
                # collector["misc"].append(cv)
                # collector["misc"].append(sv)

                key = "ent"

        cur_file.close()

    print(pre_tabs)

if __name__ == "__main__":
    main()
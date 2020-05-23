#! /usr/env/bin/python3.7

import json
import os
from helpers import get_series
from helpers import generate_key
from helpers import norm_name

# OPT -- pass open file pointers to functions instead of opening in functions

def main():
    count_obj = 0
    count_ser = 0
    count_err = 0
    all_values = {}
    all_iso_info = False
    last_object = {}
    _obj = None
    k_visited = []
    current_area_code = 0
    reroute = 0
    last_line = []
    last_area_code = 0
    last_occ_code = 0
    exclusions = []

    my_states = {
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

    vals_fp  = open("./value_set.csv", "r")
    build_values_into_json(vals_fp, all_values)
    vals_fp.close()

    file_stamp = 1
    fw = open(f'./finals_out/series_data_{file_stamp}.json', "a+")
    fw.write("[")

    # 05/21/2020
    # fw = open("bls_series_values.json", "w")
    # fw.write(json.dumps(all_values, indent=4))
    # fw.close()
    # exit()

    for filename in sorted(os.listdir("./split_series/")):

        c_fp = open(f"./split_series/{filename}", "r")
        print(f"Reading: {filename}")
        
        for line in c_fp.readlines():

            # if not reroute:
            count_ser = count_ser+1
            c_line          = line.split("\t")
            area_code       = c_line[7] # becomes redundant
            state_code      = c_line[6] # Redundant
            series_id       = c_line[0].strip(" ")
            industry_code   = c_line[3]
            occupation_code = c_line[4]
            sector_code     = c_line[8]
            title           = c_line[9] # Parse the sh*t out of this

            # if area_code in exclusions:
            #     continue

            # vals = [area_code,state_code,series_id,industry_code,occupation_code,sector_code,title]
            # with open("./debug_1.json", "a+") as fw_1:
            #     fw_1.write("--------------------------- NEW VALUES --------------------------------\n")
            #     fw_1.write(f"{vals}\n")
            #     fw_1.write(f"Current Area Code: {area_code}\nPrev Area Code: {last_area_code}\ncurrent occ code: {occupation_code}\nlast occ code: {last_occ_code}")
            #     fw_1.write("\n-----------------------------------------------------------------------\n")
            try:
                if last_area_code != area_code or last_occ_code != occupation_code:
                    
                    count_obj = count_obj + 1
                    if count_obj % 600 == 0 and count_obj > 1:
                        fw.write(str(json.dumps(_obj,indent=4)))
                        fw.write("]")
                        fw.close()
                        fw = None
                        file_stamp = file_stamp + 1
                    elif _obj:
                        fw.write(str(json.dumps(_obj,indent=4)) + ",")

                    if fw == None:
                        fw = open(f"./finals_out/series_data_{str(file_stamp)}.json", "a+")
                        fw.write("[")
                    
                    last_object = _obj
                    last_area_code = area_code
                    last_occ_code = occupation_code
                    k_visited = []
                    _obj = None

                    # Write to file

            except Exception as e:
                c_fp.close()
                vals_fp.close()
                fw.close()
                print("Error: {e.message}")
                exit()

            # [1] Initialize this object
            if _obj == None:

                p_series = get_series(str(area_code))
                # print(p_series)
                # p_series {
                #     "t" : t,
                #     "state_id" : str(the_line[0]),
                #     "area_code" : str(code),
                #     "name" : str(the_line[3])
                # }

                if not p_series: # Improbability alert
                    c_fp.close()
                    vals_fp.close()
                    fw.close()
                    exit()

                _obj = reset_structures(p_series["t"])

                # Initialize immediately resolvable parameters
                if p_series["t"] == "city":
                    _obj["ids"]["name"] = norm_name(p_series["name"][0])
                    _obj["ids"]["state_id"] = p_series["state_id"]

                if p_series["t"] == "metro":
                    if _obj == None:
                        print("WTF???")
                        exit()
                    _obj["ids"]["name"] = norm_name(p_series["name"][0])
                    _obj["ids"]["state_id"] = p_series["state_id"]
                    _obj["ids"]["netro_uid"] = p_series["area_code"]

                if p_series["t"] == "state":
                    _obj["ids"]["name"] = norm_name(p_series["name"][0])
                    _obj["ids"]["state_id"] = p_series["state_id"]

                if p_series["t"] == "nation":
                    _obj["ids"]["name"] = "united_states_of_america"


            # [2] Initialize object general info
            if len(_obj['ww_info']) == 0:
                next_step = {
                    "series_id" : series_id,
                    "industry_code" : industry_code,
                    "occupation_code" : occupation_code,
                    "sector_code" : sector_code,
                    "title" : title
                }

                # return {
                # "sector_info" : [code, name], "occupation_info" : [code, name], "industry_info" : [code, name]
                # }
                all_info = get_all_infos(next_step["sector_code"], \
                    next_step["occupation_code"], \
                    next_step["industry_code"])

                # Final "ww_info" values √
                ww_info = {
                    "sec" : all_info['sector_info'],
                    "occ" : all_info['occupation_info'], 
                    "ind" : all_info['industry_info'], 
                    "ae" : area_code
                }
                _obj["ww_info"] = ww_info

            # Ex. "[per_tile, hrly, atfp]"
            cur_key_info = generate_key(title)

            k_buffer = []
            for k in cur_key_info:
                if k != None:
                    k_buffer.append(k)

            ser_value = all_values[series_id]["val"]
            if ser_value == "-":
                ser_value = "NOTE_" + all_values[series_id]['note'].rstrip('\n')

            if len(k_buffer) == 2:
                _obj[k_buffer[0]][k_buffer[1]] = ser_value
            if len(k_buffer) == 3:
                _obj[k_buffer[0]][k_buffer[1]][k_buffer[2]] = ser_value

            if "".join(k_buffer) not in k_visited:
                k_visited.append("".join(k_buffer))
            else :
                print("--------- STOP ----------")
                count_err=count_err+1
                print(f"Duplicate: {''.join(k_buffer)}\nSeries: {series_id}\nError: {count_err}\n")
                k_visited = []
                k_visited.append("".join(k_buffer))
                print(f"counted {count_obj} objects")
                print(f"counted {count_ser} series")
                print(f"counted {count_err} errors")

                exit()

        c_fp.close()
        
    # Reference Chunk
    # Key           Title
	# [emp]         Employment for Management Occupations in All Industries in Abilene, TX
	# [e_std_err]   Employment percent relative standard error for Management Occupations in All Industries in Abilene, TX
	# [hmean]       Hourly mean wage for Management Occupations in All Industries in Abilene, TX
	# [amean]       Annual mean wage for Management Occupations in All Industries in Abilene, TX
	# [wp_std_err]  Wage percent relative standard error for Management Occupations in All Industries in Abilene, TX
	# [htp]         Hourly 10th percentile wage for Management Occupations in All Industries in Abilene, TX
	# [htfp]        Hourly 25th percentile wage for Management Occupations in All Industries in Abilene, TX
	# [hmp]         Hourly median wage for Management Occupations in All Industries in Abilene, TX
	# [hsfp]        Hourly 75th percentile wage for Management Occupations in All Industries in Abilene, TX
	# [hnp]         Hourly 90th percentile wage for Management Occupations in All Industries in Abilene, TX
	# [atp]         Annual 10th percentile wage for Management Occupations in All Industries in Abilene, TX
	# [atfp]        Annual 25th percentile wage for Management Occupations in All Industries in Abilene, TX
	# [amp]         Annual median wage for Management Occupations in All Industries in Abilene, TX
	# [asfp]        Annual 75th percentile wage for Management Occupations in All Industries in Abilene, TX
	# [anp]         Annual 90th percentile wage for Management Occupations in All Industries in Abilene, TX
	# [pk]          Employment per 1,000 jobs for Management Occupations in All Industries in Abilene, TX
	# [quo]         Location Quotient for Management Occupations in All Industries in Abilene, TX

    # Write the last object
    fw.write(str(json.dumps(_obj,indent=4)))
    fw.write("]")
    vals_fp.close()
    fw.close()

    print(f"counted {count_obj} objects")
    print(f"counted {count_ser} series")
    print(f"counted {count_err} errors")

#####################

def has_emptys(_obj):
    """
        Tell us, oh wise one, is the object complete?
    """

    for k in _obj:
        
        try:
            if not _obj[k]:
                return k
            if _obj[k] == "null":
                return k

            for e in _obj[k]:
                if not _obj[k][e]:
                    return e
                if _obj[k][e] == "null": # "stats"
                    return e
                if type(_obj[k][e]) == dict:
                    
                    for y in _obj[k][e]:
                        
                        if _obj[k][e][y] == "null":
                            return y 
                
        except AttributeError:
            
            continue

    return False


###################### First Steps ######################
def build_values_into_json(fp, all_values):
    print("Loading values...")
    for line in fp.readlines():
        split_line = line.split("\t")
        series_id = split_line[0].strip(" ")
        value = split_line[3].strip(" ")
        note = 0
        if value == "-":
            note = split_line[4]
        
        add_obj = {
            "id"   : series_id,
            "val"  : value,
            "note" : note
        }
        all_values[str(series_id)] = add_obj

    print("Done!")

    
###################### INFO GETTERS ######################
def get_all_infos(S,O,I):
    return {
        "sector_info"       : get_sector_info(S),
        "occupation_info"   : get_occupation_info(O),
        "industry_info"     : get_industry_info(I)
    }

def get_sector_info(S):
    sec_fp   = open("./bls_data/sectors.csv", "r")
    for line in sec_fp.readlines():
        split_line = line.split('\t')
        if split_line[0] == S:
            sec_fp.close()
            return [split_line[0], split_line[1].rstrip("\n")]
    print("debug me -- get_sector_info")

    sec_fp.close()
    return False

def get_occupation_info(O):

    occ_fp   = open("./bls_data/occupations.csv", "r")
    for line in occ_fp.readlines():
        split_line = line.split("\t")
        if split_line[0] == O:
            occ_fp.close()
            return [split_line[0], split_line[1].rstrip("\n")] # id, name
    print("debug me -- get_occupation_info")

    occ_fp.close()

def get_industry_info(I):
    ind_fp  = open("./bls_data/industries.csv", "r")
    for line in ind_fp.readlines():
        split_line = line.split("\t")
        if split_line[0] == I:
            ind_fp.close()
            return [split_line[0], split_line[1].rstrip("\n")]
    print("debug me -- get_industry_info")

    ind_fp.close()

## DATA ##

def reset_structures(t):
    """
    They're the same, but different...Ya know?
    """
    if t == "metro":
        return {
            "ids"    : {
                "type_" : "metro"
            },
            "per_tile" : {
                "hrly" : {
                    "htp"    : "null",
                    "htfp"   : "null",
                    "hmp"    : "null",
                    "hsfp"   : "null",
                    "hnp"    : "null",
                },
                "anny" : {
                    "atp"    : "null",
                    "atfp"   : "null",
                    "amp"    : "null",
                    "asfp"   : "null",
                    "anp"    : "null",
                }
            },
            "stat" : {
                "pk"     : "null",
                "quo"     : "null",
                "emp"        : "null",
                "e_std_err"  : "null",
                "hmean"      : "null",
                "amean"      : "null",
                "wp_std_err" : "null"
            },
            "ww_info" : {}
        }
    elif t == "state":
        return {
            "ids"    : {
                "type_" : "state"
            },
            "per_tile" : {
                "hrly" : {
                    "htp"    : "null",
                    "htfp"   : "null",
                    "hmp"    : "null",
                    "hsfp"   : "null",
                    "hnp"    : "null",
                },
                "anny" : {
                    "atp"    : "null",
                    "atfp"   : "null",
                    "amp"    : "null",
                    "asfp"   : "null",
                    "anp"    : "null",
                }
            },
            "stat" : {
                "pk"     : "null",
                "quo"     : "null",
                "emp"        : "null",
                "e_std_err"  : "null",
                "hmean"      : "null",
                "amean"      : "null",
                "wp_std_err" : "null"
            },
            "ww_info" : {}
        }
    elif t == "city":
        return {
            "ids"    : {
                "type_" : "city"
            },
            "per_tile" : {
                "hrly" : {
                    "htp"    : "null",
                    "htfp"   : "null",
                    "hmp"    : "null",
                    "hsfp"   : "null",
                    "hnp"    : "null",
                },
                "anny" : {
                    "atp"    : "null",
                    "atfp"   : "null",
                    "amp"    : "null",
                    "asfp"   : "null",
                    "anp"    : "null",
                }
            },
            "stat" : {
                "pk"         : "null",
                "quo"     : "null",
                "emp"        : "null",
                "e_std_err"  : "null",
                "hmean"      : "null",
                "amean"      : "null",
                "wp_std_err" : "null"
            },
            "ww_info" : {}
        }
    elif t == "nation":
        return {
            "ids"    : {
                "type_" : "nation"
            },
            "per_tile" : {
                "hrly" : {
                    "htp"    : "null",
                    "htfp"   : "null",
                    "hmp"    : "null",
                    "hsfp"   : "null",
                    "hnp"    : "null",
                },
                "anny" : {
                    "atp"    : "null",
                    "atfp"   : "null",
                    "amp"    : "null",
                    "asfp"   : "null",
                    "anp"    : "null",
                }
            },
            "stat" : {
                "pk"         : "null",
                "quo"     : "null",
                "emp"        : "null",
                "e_std_err"  : "null",
                "hmean"      : "null",
                "amean"      : "null",
                "wp_std_err" : "null"
            },
            "ww_info" : {}
        }


if __name__ == "__main__":
    main()
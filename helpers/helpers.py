def get_series(area_code):

    """
    Determine the geographical scope of the area code
    """

    state = open("./bls_data/state_as_area_series.csv", "r") 
    metro = open("./bls_data/metro_as_area_series.csv", "r") 
    city = open("./bls_data/city_as_area_series.csv", "r")
    nation = open("./bls_data/nation_as_area_series.csv", "r")

    found = 0

    # s_count = 0
    # c_count = 0
    # m_count = 0
    # n_count = 0

    bls_mapping = { \
                    '01': 1, '02': 2, '04': 3, '05': 4, '06': 5, '08': 6, '09': 7, '10': 8, '12': 10, \
                    '13': 11, '15': 12, '16': 13, '17': 14, '18': 15, '19': 16, '20': 17, '21': 18, \
                    '22': 19, '23': 20, '24': 21, '25': 22, '26': 23, '27': 24, '28': 25, '29': 26, \
                    '30': 27, '31': 28, '32': 29, '33': 30, '34': 31, '35': 32, '36': 33, '37': 34, \
                    '38': 35, '39': 36, '40': 37, '41': 38, '42': 39, '44': 41, '45': 42, '46': 43, \
                    '47': 44, '48': 45, '49': 46, '50': 47, '51': 48, '53': 49, '54': 50, '55': 51, \
                    '56': 52, '72': 72, '78':78, '11':11, '66': 66
                }

    for line in state.readlines():
        # s_count = s_count+1

        the_line = line.split("\t")
        code = the_line[1]
        t = "state"

        if str(code) == str(area_code):
            found = 1
            res = {
                "t" : t,
                "state_id" : str(the_line[0]),
                "area_code" : str(code),
                "name" : str(the_line[3]).rstrip("\n").split(",")
            }
            break

    for line in metro.readlines():
        # m_count = m_count+1
        
        if found:
            break

        the_line = line.split("\t")
        code = the_line[1]
        t = "metro"
        
        if str(code) == str(area_code):
            found = 1
            res = {
                "t" : t,
                "state_id" : str(bls_mapping[the_line[0]]),
                "area_code" : str(code),
                "name" : str(the_line[3]).rstrip("\n").split(" nonmetropolitan area")
            }

    for line in city.readlines():
        # c_count = c_count+1

        if found:
            break

        t = "city"
        the_line = line.split("\t")
        code = the_line[1]
        if str(code) == str(area_code):
            found = 1
            res = {
                "t" : t,
                "state_id" : str(bls_mapping[the_line[0]]),
                "area_code" : str(code),
                "name" : str(the_line[3]).rstrip("\n").split(",")
            }

    for line in nation.readlines():
        # c_count = c_count+1
        
        if found:
            break

        t = "nation"
        the_line = line.split("\t")
        code = the_line[1]
        if str(code) == str(area_code):
            found = 1
            res = {
                "t" : t,
                "state_id" : None,
                "area_code" : str(code),
                "name" : str(the_line[3]).rstrip("\n").split(",")
            }

    state.close()
    metro.close()
    city.close()
    nation.close()

    if found == 0:
        print(f"Nothing found for code {area_code}")
        print(f"Tried:\n{c_count} Cities\n{m_count} Metro's\n{s_count} States")
        return False
    # print(res)
    return res

# Tells us how to traverse the JSON object to add values
def generate_key(title):

    split_title = title.split(" ")

    id_by = " ".join([split_title[0],split_title[1]])

    __key = None
    if id_by == "Employment for":
        _key = "stat"
        key = str("emp")
    if id_by == "Employment percent":
        _key = "stat"
        key = str("e_std_err")
    if id_by == "Hourly mean" :
        _key = "stat"
        key = str("hmean")
    if id_by == "Annual mean"  :
        _key = "stat"
        key = str("amean")
    if id_by == "Wage percent" :
        _key = "stat"
        key = str("wp_std_err")
    if id_by == "Hourly 10th" :
        _key = "per_tile"
        __key = "hrly"
        key = str("htp")
    if id_by == "Hourly 25th" :
        _key = "per_tile"
        __key = "hrly"
        key = str("htfp")
    if id_by == "Hourly median" :
        _key = "per_tile"
        __key = "hrly"
        key = str("hmp")
    if id_by == "Hourly 75th" :
        _key = "per_tile"
        __key = "hrly"
        key = str("hsfp")
    if id_by == "Hourly 90th" :
        _key = "per_tile"
        __key = "hrly"
        key = str("hnp")
    if id_by == "Annual 10th" :
        _key = "per_tile"
        __key = "anny"
        key = str("atp")
    if id_by == "Annual 25th" :
        _key = "per_tile"
        __key = "anny"
        key = str("atfp")
    if id_by == "Annual median" :
        _key = "per_tile"
        __key = "anny"
        key = str("amp")
    if id_by == "Annual 75th" :
        _key = "per_tile"
        __key = "anny"
        key = str("asfp")
    if id_by == "Annual 90th" :
        _key = "per_tile"
        __key = "anny"
        key = str("anp")
    if id_by == "Employment per" :
        _key = "stat"
        key = str("pk")
    if id_by == "Location Quotient" :
        _key = "stat"
        key = str("quo")

    return [_key, __key, key]


def norm_name(name):
    name = name.split(" ")
    if len(name) > 1:
        name = "_".join(name)
    else:
        name = name[0]
    return name.lower()


if __name__ == "__main__":
    # 1200000 state
    # 5100004 metro
    # 0013380 city
    print(get_series("5100004"))
    print(generate_key("Annual median wage for Management Occupations in All Industries in Abilene, TX"))
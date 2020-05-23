def todo():
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

    bls_mapping {'01': 1, '02': 2, '04': 3, '05': 4, '06': 5, '08': 6, '09': 7, '10': 8, '12': 10, '13': 11, '15': 12, '16': 13, '17': 14, '18': 15, '19': 16, '20': 17, '21': 18, '22': 19, '23': 20, '24': 21, '25': 22, '26': 23, '27': 24, '28': 25, '29': 26, '30': 27, '31': 28, '32': 29, '33': 30, '34': 31, '35': 32, '36': 33, '37': 34, '38': 35, '39': 36, '40': 37, '41': 38, '42': 39, '44': 41, '45': 42, '46': 43, '47': 44, '48': 45, '49': 46, '50': 47, '51': 48, '53': 49, '54': 50, '55': 51, '56': 52}

    for line in bls_states.readlines():
        newline = line.split("\t")
        st = newline[1].rstrip("\n")

        n_st = st.split(" ")
        if len(n_st) > 1:
            norm_state = "_".join(n_st).lower()
        else:
            norm_state = st.lower()

        if norm_state == "virgin_islands" or norm_state == "puerto_rico" or norm_state == "district_of_columbia":
            continue
        
        my_id = my_states[norm_state][0] # My state ID
        th_id = newline[0]

        blsMapping[str(th_id)] = my_id

    print(blsMapping)
        
if __name__ == "__main__":
    todo()
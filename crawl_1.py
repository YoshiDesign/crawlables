#! /usr/env/bin/python3.7

import bs4 as bs
import urllib.request
import ssl
import os

# from time import time

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
context = ssl._create_unverified_context()
i=0

def locate():

    locations = {}
    x = "_" # Concatenator

    with open(str(os.getcwd()) + "/US_norepeat.txt", "r") as us:
        
        for line in us.readlines():
            
            line = line.split("\t")

            state = line[3].lower()
            city  = line[2].lower()
            
            # Set up the state's array of its cities
            try :

                if len(city.split(' ')) > 1:
                    city = x.join(city.split(' ')).lower()

                if len(state.split(' ')) > 1:
                    state = x.join(state.split(' ')).lower()

            except Exception as err:
                print(err)

            try:
                check = locations[state]

            except KeyError:
                locations[state] = []

            if city not in locations[state]:
                locations[state].append(city)

    
    return locations


def crawl(url, f_name):

    print(f"URL : {url}\nFNAME : {f_name}\n\n")

    global i
    i = i + 1
    sauce = urllib.request.Request(url,headers={'User-Agent':user_agent})
    res   = urllib.request.urlopen(sauce, context=context)
    soup  = bs.BeautifulSoup(res, 'html.parser')

    try:

        # scripts = soup.find_all('script')
        tables  = soup.find_all(id="mainContent_dgCostOfLiving")
        buffer  = []

        # # Collect a list of scripts as strings
        # for s in scripts:
        #     buffer.append(str(s.text))
        # for b in buffer:
        #     if "series" in b:
        #         with open(str(os.getcwd()) + "/SCR/" + f_name + "_SCR.html", 'w') as fw :
        #             fw.write(b)

        buffer = []
        # Collect a list of the costOfLiving tables
        for t in tables:
            buffer.append(str(t))
        for b in buffer:
            with open(str(os.getcwd()) + "/TAB_1/" + f_name + "_TAB.html", 'w') as fw :
                fw.write(b)

    except Exception as e:
        print("ERROR")
        print(e)

def main():

    url = 'https://www.bestplaces.net/cost_of_living/city/'
    locations = locate()
    f_name = str()
    x = "_"

    # locations = {"new_york" : ["albany"], "alaska" : ["unalaska", "akutan"]}
    
    for s in locations:
        
        if len(s.split(' ')) > 1:
            s = x.join(s.split(' '))

        for c in locations[s]:
            f_name = "ww_"
            # Create new f_name
            for i in s:
                f_name+=i
            f_name += "_"

            for i in c:
                f_name+=i

            # print(f_name + "\n\n")

            crawl(str(url + s + "/" + c), f_name)


if __name__ == "__main__":
    main()
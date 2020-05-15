#! /usr/env/bin/python3.7
import json

def main():

    j_fp = open("json_scr.json","r")
    all_data = json.loads(j_fp.read())

    for e, state in enumerate(all_data):
        print(str(e) + " " + state)

if __name__ == "__main__":
    main()
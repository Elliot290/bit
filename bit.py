import requests
import sys
#sys.argv = ["","bit.do","/sdcard/new"]

file = open(sys.argv[2],"r").read().split("\n")

print("Total links to test :"+str(len(file)))

for link in file:
    try:
        url = requests.get("https://"+sys.argv[1]+"/"+link,timeout=4)
        if url.history:
        	print("\033[92mhttps://"+sys.argv[1]+"/"+link)
        else:
        	print("\033[91mhttps://"+sys.argv[1]+"/"+link)
        	

    except Exception as e:
        print("\033[92mhttps://"+sys.argv[1]+"/"+link)

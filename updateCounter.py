## you need a python3 installation on your system - luckly there is one in the microsoft store.
##
## $python3 updateCounter.py TZ 1 to update your terran games with 1 gg
## other combinations are TT, TP, TZ, PT, PP, PZ, ZT, ZP, ZZ - your probally get it :)
## but there are batch files for it. so no need to use commandline arguments while playing sc2
##
## pyrrrrr //  dev@postwendend.com  (tobias hoffmann) 

## imports  - just default modules - no need to install anything else via pip
import json
import sys


## load json dict
with open('database.json') as fdb:
   db = json.load(fdb)


matchup = sys.argv[1] if (len(sys.argv) == 3) else ""
wasgg   = sys.argv[2] if (len(sys.argv) == 3) else 0



if db:
	gamesCounter = 0
	goodGamesCounter = 0
	for m in db:
		if m.lower() in matchup.lower():
			db[m]["games"] += 1
			db[m]["gg"] += min(1,max(0,int(wasgg)))
			
		gamesCounter += int(db[m]["games"])
		goodGamesCounter += int(db[m]["gg"])
	
	print(gamesCounter,goodGamesCounter)


with open('database.json', 'w') as fdb:
    json.dump(db, fdb,indent=4)

with open("ggCounter.txt", "w") as f:
	
	txt = "GGCOUNTER: %s/%s" % ( gamesCounter,goodGamesCounter)
	f.write(txt)


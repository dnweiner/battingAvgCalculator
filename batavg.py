import sys, os, re
from player import Player

#####
#following code taken from wiki to check for command line arguments
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]
 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])
#####

name_pattern = re.compile(r"([A-Z]{1}[A-Za-z']+\s{1})+") #check for one capital letter followed by at least one lowercase letter or apostrophe and a space
at_bats_pattern = re.compile(r"(batted\s{1})(\d*?)(\s{1}times)") #check for clusters of "batted # times" 
hits_pattern = re.compile(r"(with\s{1})(\d*?)(\s{1}hits)") #check for clusters of "with # hits"
runs_pattern = re.compile(r"(and\s{1})(\d*?)(\s{1}runs)") #check for clusters of "and # runs"

players = {} #create a dictionary to hold players. will be populated after file is opened

with open(filename, "r") as f:

	for line in f:
		r_name = re.match(name_pattern, line) #match, because we only check beginning of string
		r_at_bats = re.search(at_bats_pattern, line) 
		r_hits = re.search(hits_pattern, line)
		r_runs = re.search(runs_pattern, line)

		if r_name is not None and r_at_bats is not None and r_hits is not None and r_runs is not None:
			name = str(r_name.group()) #cast regex-recognized name to a str variable
			firstname = name.split()[0] 
			lastname = name.split()[1] #index by lastname
			index = firstname + "-" + lastname #because names are not all unique, we index by fullnames, hyphenated
			if index in players.keys():
				players[index].at_bats = float(players[index].get_at_bats()) + float(r_at_bats.group(2)) #add on this game's at_bats
				players[index].hits = float(players[index].get_hits()) + float(r_hits.group(2)) #add on this game's hits
				players[index].runs = float(players[index].get_runs()) + float(r_runs.group(2)) #add on this game's runs
			else:
				players[index] = Player(r_name.group(), float(r_hits.group(2)), float(r_at_bats.group(2)), float(r_runs.group(2)), 0)
			
for index in players: #for all players, by name
	players[index].batavg = players[index].avg() #replace placeholder batting average with actual average

descending_players = sorted(players.values(), key=lambda player: player.get_batavg(), reverse=True) #sort in descending order

for player in descending_players: #print, properly sorted
	print "%s: %1.3f" % (player.get_name(), player.get_batavg())

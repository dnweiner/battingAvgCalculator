#define class to hold and compute information for each player, as recommended in wiki instructions
class Player:
	#constructor
	def __init__(self, name, hits, at_bats, runs, batavg):
		self.name = name
		self.hits = float(hits)
		self.at_bats = float(at_bats)
		self.runs = float(runs)
		self.batavg = float(batavg)
		
	def get_name(self):
		return self.name
	
	def get_hits(self):
		return self.hits
	
	def get_at_bats(self):
		return self.at_bats
	
	def get_runs(self):
		return self.runs
	
	def get_batavg(self):
		return self.batavg 

	def avg(self):
		return round(float(self.hits)/float(self.at_bats),3)
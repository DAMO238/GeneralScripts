# Written with the aid of documentation made by dwavesys

#import all needed libraries and apis
import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import networkx as nx
import matplotlib.pyplot as plt

# Our problem is to colour a map of canada with 4 colours such that no two neighboring provinces have the same colour
# I will be using postal codes for ease of coding:

# AB = Alberta
# BC = British Columbia
# MB = Manitoba
# NB = New Brunswick
# NL = Newfoundland and Labrador
# NS = Nova Scotia
# NT = Northwest Territories
# NU = Nunavut
# ON = Ontario
# PE = Prince Edward Island
# QC = Quebec
# SK = Saskatchewan
# YT = Yuton

print("Setting up problem")

#Store an array of all provinces in postal code format in memory
provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

#Store an array of tuplets representing borders between provinces in memory
neighbors = [('AB', 'BC'), ('AB', 'NT'), ('AB', 'SK'), ('BC', 'NT'), ('BC', 'YT'), ('MB', 'NU'), ('MB', 'ON'), ('MB', 'SK'), ('NB', 'NS'), ('NB', 'QC'), ('NL', 'QC'), ('NT', 'NU'), ('NT', 'SK'), ('NT', 'YT'), ('ON', 'QC')]

# Utility function to check if have a shared edge, we do not pick the same colour
def not_both_1(v, u):
	return not (v and u)

# Each colour will be represented by a channel from 0 to 1 where will pick 0 or 1, 
# hence our colours are given as follows
one_color_configurations = {(0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0)}
colors = len(one_color_configurations)

print("Setting up quantum problem")

# Use the dwave api to set up a binary constraint problem (ie we enforce a true or false constraint)
csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)

# Now we need to use our provinces array to add in our constraint that a node can only be one colour
for province in provinces:
	variables = [province+str(i) for i in range(colors)] # Labels for the dwavesys api to use
	csp.add_constraint(one_color_configurations, variables) # Actually add the constraint
	
# Now we can add in out constraint for borders not sharing a colour and so we will need our neighbers array
for neighbor in neighbors:
	v, u = neighbor # Get out the values from the tuplet
	for i in range(colors):
		variables = [v+str(i), u+str(i)]
		csp.add_constraint(not_both_1, variables)
		
# Now the problem is set up, we need to convert this into a quadratic model that the QPU can handle
bqm = dwavebinarycsp.stitch(csp)

print("Sending request")

# Set up my sampler with my credentials from config file and sample 50 times (as QM is probabilistic)
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(bqm, num_reads=500)

# At this point, the problem is theoretically solved, but it doesn't look very easy to understand so we are
# going to plot it with matplotlib
def plot_map(sample):
	
	# Set up graph with nodes and edges
	G = nx.Graph()
	G.add_nodes_from(provinces)
	G.add_edges_from(neighbors)
	
	# Now we need to convert from our binary representation from output to colours which we can draw
	color_map = {}
	for province in provinces:
		for i in range(colors):
			if sample[province+str(i)]:
				color_map[province] = i # If the flag is the same as what we put in, then this is the colour we need
				
	# Plot with the colours we just found
	node_colors = [color_map.get(node) for node in G.nodes()]
	nx.draw_circular(G, with_labels=True, node_color=node_colors, node_size=3000, cmap=plt.cm.rainbow)
	plt.show()
	

# Check if the lowest energy sample (one that got closest to best solution) meet the constraints (QM not deterministic so we might be wrong) and if so plot it
sample = next(response.samples()) #< Get lowest energy solution
if not csp.check(sample):
	print('Lowest energy sample failed to meet requirements to colour map!')
else:
	print("Displaying Map")
	plot_map(sample)

import networkx as nx
import itertools
import random
from my_functions import *

print "running"
cabs = [1,2]
users = ['A','B','C']
destinations = ['a','b','c']

G = getDiGraph(users, destinations, cabs)
G = addRandomWeight(G)

G_sub = G.subgraph(users+destinations)
logIt(G_sub, "G_sub: Created")

cases = setCases(cabs, users, destinations)



import networkx as nx
import itertools
import random
import ast

def logIt(G, message_string):
    print message_string
    print "Nodes: ", G.number_of_nodes()
    print "Edges: ", G.number_of_edges()
    print "Self loop edges: ", G.number_of_selfloops()
    print "-----------------------------------------------------"


def getDiGraph(users, destinations, cabs):
    G = nx.DiGraph()
    G.add_nodes_from(users)
    G.add_nodes_from(destinations)
    G.add_nodes_from(cabs)
    logIt(G, "G: Nodes Added")

    G.add_edges_from(list(itertools.product(cabs, users)))
    logIt(G, "G: Added edges from cabs to users")
    G.add_edges_from(list(itertools.product(users, destinations)))
    logIt(G, "G: Added edges from users to destinations")
    G.add_edges_from(list(itertools.product(users, users)))
    logIt(G, "G: Added edges from users to users")
    G.add_edges_from(list(itertools.product(destinations, destinations)))
    logIt(G, "G: Added edges from destinations to destinations")
    G.add_edges_from(list(itertools.product(destinations, users)))
    logIt(G, "G: Added edges from destinations to users")
    # G.add_edges_from(list(itertools.product()))

    for i in range(len(users)):
        G.remove_edge(destinations[i], users[i])
    logIt(G, "G: Removed edges from destination(k) to user(k)")

    self_loops = G.selfloop_edges()
    G.remove_edges_from(self_loops)
    logIt(G, "G: Removed self loops")

    return G


def addRandomWeight(G):
    for edge in G.edges(data=True):
        edge[2]['weight'] = random.randint(1, 20)
    logIt(G, "G: Added weight")
    print G.edges(data=True)
    print "-----------------------------------------------------"
    return G


def setCases(cabs, users, destinations):

    #All the permutations of each list of nodes
    cabperm_list = []
    userperm_list = []
    destperm_list = []
    print "Permutations for cabs, users, and destinations:"
    for i in range(1, len(cabs)+1):
        cabperm = list(itertools.permutations(cabs, i))
        cabperm_list.append(cabperm)
    for i in range(1, len(users)+1):
        userperm  =list(itertools.permutations(users, i))
        userperm_list.append(userperm)
    temp_list = []
    for item in userperm_list:
        temp_list+=item
    userperm_list = temp_list
    for i in range(1, len(destinations)+1):
        destperm = list(itertools.permutations(destinations, i))
        destperm_list.append(destperm)
    temp_list = []
    for item in destperm_list:
        temp_list+=item
    destperm_list = temp_list

    print userperm_list
    print destperm_list
    print "-----------------------------------------------------"
    print "-----------------------------------------------------"
    print "-----------------------------------------------------"

    #All the products

    cabs_to_people = [list(itertools.product(cabs, x)) for x in userperm_list]
    print cabs_to_people
    cabs_to_people = str(cabs_to_people).replace("('", "'").replace(',)', ')')
    cabs_to_people = cabs_to_people.replace("))", ")")
    print cabs_to_people
    print "-----------------------------------------------------"
    print "-----------------------------------------------------"

    #People to destination can go either way so it's a permutation?
    #people_to_dest = list(itertools.product(userperm_list, destperm_list))
    people_to_dest = [list(itertools.product(userperm_list, x)) for x in destperm_list]
    print people_to_dest
    new_people_to_dest = []
    for dimension in people_to_dest:
        new_dimension = []
        for path in dimension:
            new_path = tuple()
            for item in path:
                try:
                    for y in item.__iter__():
                        new_path+=tuple(y)
                except:
                    new_path+=tuple(item)

            new_dimension.append(new_path)
        new_people_to_dest.append(new_dimension)
    temp_list = []
    for item in new_people_to_dest:
        temp_list+=item
    new_people_to_dest = temp_list
    print new_people_to_dest
    print len(people_to_dest)
    print len(new_people_to_dest)

    people_to_dest = new_people_to_dest

    people_to_dest = set(people_to_dest)
    print len(people_to_dest)
    people_to_dest = list(people_to_dest)

    for path in people_to_dest:
        if len(path)%2 != 0:
            people_to_dest.remove(path)

    print people_to_dest
    print len(people_to_dest)

    for path in people_to_dest:
        try:
            if path[0].lower() not in path:
                pass
                #people_to_dest.remove(path)
            elif path[1].lower() not in path:
                pass
                #people_to_dest.remove(path)
            elif path[2].lower() not in path:
                pass
                #people_to_dest.remove(path)
            else:
                print path
                people_to_dest.remove(path)
        except: pass

    print people_to_dest
    print len(people_to_dest)


    #final_list = list(itertools.product(cabs_to_people, people_to_dest)
    #for path in final_list: print path
    #print len(final_list)
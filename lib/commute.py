
import networkx as nx
import pickle
import os

# TODO: write documentation
def commute_search(stop, time):
    time = float(time)
    subway = pickle.load(open('subway_network','r'))  # networkx graph with subway stops and times
    schools = pickle.load(open('school_stops'))  # dictionary with list of subway stop for a school
    potential_schools = []
    for school in schools:
        for school_stop in schools[school]:
            try:
                if subway_time(subway, stop, school_stop) < time:
                    potential_schools.append(school)
                    break
            except nx.exception.NetworkXError:
                #print "stop not in subway network? :",school_stop
                pass
    return potential_schools

def subway_time(subway, stop1, stop2):
    try:
        path = nx.shortest_path(subway,stop1,stop2)
    except nx.exception.NetworkXNoPath:
        return 1000  # inf
    time = 0
    previous = path[0]
    for stop in path[1:]:
        time+=subway[previous][stop]['time']
        previous = stop
    return time/60.0


#=========SCRIPT STARTS HERE===============#
if __name__ == '__main__':
    import sys
    if len(sys.argv)==2:
        if sys.argv[1] == 'stops':
            subway = pickle.load(open(os.path.dirname(os.path.realpath(__file__))+'/subway_network','r'))  # networkx graph with subway stops and times
            print(subway.nodes())
        elif sys.argv[1] == 'schools':
            schools = pickle.load(open(os.path.dirname(os.path.realpath(__file__))+'/school_stops'))  # dictionary with list of subway stop for a school
            print(schools.keys())
        else:
            print('Unknown parameter options supplied:',sys.argv,'Try "stops" or "schools"')
    elif len(sys.argv) == 3:
        try:
            print(commute_search(sys.argv[1], sys.argv[2]))
        except:
            print('Something went wrong. Try supplying a known stop and time')

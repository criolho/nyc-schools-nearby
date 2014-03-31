# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 12:46:36 2014

@author: Lucio
"""
import networkx as nx
import pickle

def time_difference(time1, time2):
    t1 = time1.split(':')
    t2 = time2.split(':')
    
    time = 0
    time += (int(t1[0])-int(t2[0]))*3600
    time += (int(t1[1])-int(t2[1]))*60
    time += (int(t1[2])-int(t2[2]))
    return time

#Go through trips.csv, grab a single trip for each unique route
#f = open('mta_data/trips.csv','r')
#f.readline()
#trip = {}  # { route_id : trip_id }  # one of the trips made on a route
#route = {}  # { trip_id : route_id }
#for l in f:
#    line = l.strip().split(",")
#    
#    route_id = line[0]
#    trip_id = line[2]
#    trip_headsign = line[3]
#
#    if trip_headsign not in trip:
#        trip[trip_headsign] = trip_id
#        route[trip_id] = trip_headsign

#go through stop_times.csv, add stops with time for each trip in trips
subway = nx.Graph()
f = open('mta_data/stop_times.csv','r')
f.readline()
previous_stop = None
previous_depart = None
for l in f:
    line = l.strip().split(",")
    
    trip_id = line[0]
#    if trip_id not in trip.values():
#        continue
    arrive = line[1]
    depart = line[2]
    stop = line[3].replace('S','').replace('N','')
    stop_sequence = int(line[4])
    
    if stop_sequence != 1:
        time = time_difference(arrive,previous_depart)
        subway.add_edge(stop,previous_stop,{'time':time})
        
    previous_stop = stop
    previous_depart = depart
    
    
#pickle the resulting subway network
f = open('subway_network','w')
pickle.dump(subway,f)
f.close()
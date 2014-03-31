# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 13:29:06 2014

@author: Lucio

Script for processing school data. Read data from pediacities and save to
local csv file.

"""
import pickle

#go through stops.csv and get the name for stops
names = {}  # {stop_name : stop_id}
f = open('mta_data/stops.csv','r')
f.readline()
for l in f:
    line = l.strip().split(",")
    
    stop_id = line[0]
    stop_name = line[2]
    if stop_name in names:
        continue
    names[stop_name] = stop_id

#go through schools and pick out subway stops
schools = {}  # {school_name : [stop1, stop2, ...]}

#http://nycdoe.pediacities.com
f = open('doe_data/schools20131023.csv','r')
f.readline()
for l in f:
    line = l.strip().split(",")
    
    school_id = line[0]
    school_name = line[1]
    buses = line[2]
    subway_stops = [stop.split(" to ")[-1] for stop in line[3].split(";")]
    
    schools[school_name] = []
    for s in subway_stops:        
        try:
            schools[school_name].append(names[s])
        except KeyError:
            print "stop",s,"school",school_name,"other stops",schools[school_name]

print "match rate:",sum([len(schools[school_name])>0 for s in schools])/float(len(schools))

pickle.dump(schools,open('school_stops','w'))
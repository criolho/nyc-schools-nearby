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
stops_for = {}  # {school_name : [stop1, stop2, ...]}

#http://nycdoe.pediacities.com
f = open('doe_data/schools20131023.csv','r')
f.readline()
for l in f:
    line = l.strip().split(",")
    
    school_id = line[0]
    school_name = line[1]
    buses = line[2]
    subway_stops = [stop.split(" to ")[-1] for stop in line[3].split(";")]
    
    stops_for[school_name] = []
    for s in subway_stops:        
        try:
            stops_for[school_name].append(names[s])
        except KeyError:
            print "stop",s,"school",school_name,"other stops",stops_for[school_name]

print "match rate:",sum([len(stops_for[s])>0 for s in stops_for])/float(len(stops_for))

#pickle.dump(stops_for,open('school_stops','w'))
"""
THINGS I HAD TO MANUALLY DO:
th --> ''
Port Auority --> Port Authority  *
Winrop --> Winthrop
Norern --> Northern
Central Park Nor (110 St) --> Central Park North (110 St)

rd --> ''
Bedfo --> Bedford
Gaen --> Garden
Foham Road --> Fordham Rd

Square --> Sq
Street --> St
Bouleva --> Blvd

EastBroadway --> East Broadway
1stAve --> 1 Av
1StAv --> 1 Av
Astor Place --> Astor Pl
Whitehall St - Sou Ferry--> Whitehall
Broadway - Lafayette St-->Broadway-Lafayette St
Van Wyck Blvd --> Briarwood - Van Wyck Blvd
Atlantic Av - Barclays Center - 4 Av --> Atlantic Av - Barclays Ctr
Sutphin Blvd -  Archer Avenue --> Sutphin Blvd - Archer Av - JFK Airport
Broadway Junction --> Broadway Jct
ForeStAve --> Forest Av
Neptune Av - Van Siclen --> Neptune Av
WeSt8 St --> W 8 St - NY Aquarium
Union Turnpike - Kew Gardens --> Kew Gardens - Union Tpke
Kings Highway --> Kings Hwy
Beach 105 St - Seaside --> Beach 105 St
179 St --> Jamaica - 179 St


disambiguation needed:
Bay Pkwy
Bedford Park
Broadway Jct

High School for Construction Trades
Stephen T. Mather Building Arts & Craftsmanship High School
High School for Law Enforcement and Public Safety


"""
def commute_search(stop, time):
    return [s for s in school if set(reachable(s)) & set(trains[stop])]


def reachable(school):
    """
    return the trains of a school
    """
    trains = []
    routes = subways[school].split(';  ')
    for r in routes:
        trains+=r.split(' to ')[0].split(', ')
    return trains

#=========READ IN SCHOOL AND TRANSIT DATA========#

#read in schools from pediacities
import urllib
import ast
url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22BUS%22,%22SUBWAY%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22'
s = urllib.urlopen(url).read()
list_string = s[s.index('['):s.index(']')+1]
data = ast.literal_eval(list_string)  # [ {'BUS':'M14AD, ...',
subways = {}
buses = {}
for d in data:
    buses[d['Printed_Name']] = d['BUS']
    subways[d['Printed_Name']] = d['SUBWAY']
school = buses.keys()

#read in subway lines from csv
f = open('mta_subways.csv','r')
f.readline()
trains = {}  # {stop : [ line1 , line2 , ... ]}
for line in f:
    line = line.strip().split(",")
    stop = line[2]
    lines = line[5:16]
    while '' in lines:
        lines.remove('')

    trains[stop] = lines
stop = trains.keys()

#=========SCRIPT STARTS HERE===============#
import sys
print commute_search(sys.argv[1], sys.argv[2])

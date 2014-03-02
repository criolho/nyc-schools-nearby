import urllib
import ast

# TODO: write documentation
def commute_search(stop, time):
    time = float(time)
    return [s for s in schools() if set(reachable(s)) & set(trains[stop])]

# TODO: write documentation
def reachable(school):
    """
    return the trains of a school
    """
    trains = []
    routes = subways_near_school()[school].split(';  ')
    for r in routes:
        trains+=r.split(' to ')[0].split(', ')
    return trains


#=========READ IN SCHOOL AND TRANSIT DATA========#
def transit_data():
    """
        Read in schools from pediacities
    """
    url = 'http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT%20%22Printed_Name%22,%22BUS%22,%22SUBWAY%22%20from%20%2245f6a257-c13a-431b-acb9-b1468c3ff1e9%22'
    s = urllib.urlopen(url).read()
    list_string = s[s.index('['):s.index(']')+1]
    return ast.literal_eval(list_string)  # [ {'BUS':'M14AD, ...',

# TODO: improve documentation
def schools():
    names = []
    for d in transit_data():
        names.append(d['Printed_Name'])
    return names

def buses_near_school():
    buses = {}
    for d in transit_data():
        buses[d['Printed_Name']] = d['BUS']
    return buses

def subways_near_school():
    subways = {}
    for d in transit_data():
        subways[d['Printed_Name']] = d['SUBWAY']
    return subways

# TODO: improve documentation
def subway_stops():
    #read in subway lines from csv
    f = open('lib/mta_subways.csv','r')
    f.readline()
    trains = {}  # {stop : [ line1 , line2 , ... ]}
    for line in f:
        line = line.strip().split(",")
        stop = line[2]
        lines = line[5:16]
        while '' in lines:
            lines.remove('')
        trains[stop] = lines
    return trains.keys()


#=========SCRIPT STARTS HERE===============#
if __name__ == '__main__':
    import sys
    if len(sys.argv)==2:
        if sys.argv[1] == 'stops':
            print(subway_stops())
        elif sys.argv[1] == 'schools':
            print(schools())
        else:
            print('Unknown parameter options supplied:',sys.argv,'Try "stops" or "schools"')
    else:
        try:
            print(commute_search(sys.argv[1], sys.argv[2]))
        except:
            print('Unknown parameter options supplied:',sys.argv,'Try stop and time')

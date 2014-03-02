nyc-schools-nearby
=============

Every year 80,000 middle-school students and their families choose a high school to attend. In Fall 2012, the NYC Department of Education (NYCDOE) released its first-ever API for high school data to help them choose. Already, six developers have built apps with the data, but many students and parents want to narrow down their school options by geography: commute time, a given route, or other transportation considerations (i.e. I only want to take the subway).  This is a JavaScript API to distill geographic information about high schools.

Current Status
-------------

This project is currently not yet functioning.

Goal
-------------

Help NYC 8th graders pick their high school based on commute times.

Proposed Solutions
-------------
Two different use cases were proposed.
1. Students/parents with no preferred schools in mind wants to see which schools are within xx minutes to narrow down options.
2. Use Case #2 - Students/parents with a small list of preferred schools want to compare specific commuting routes.

### Implementation options for Use Case #1:
* Calculate time between nearest stop to address and nearest stop to school using GTFS. Implement as a javascript web worker in browser or API backend.
* Use an existing trip planner API (Google Transit, Mapbox, OpenTripPlanner, rrrr) for time from every subway/bus stop or intersection to every school then just find closest point to address. Implement as API querying a database of cached transit times.

### Implementation options for Use Case #2:
* Provide individual links to trips planners (e.g. Google, third-party) for each school selected. Would provide ability to select more granluar transportation options (bike, car, alternative times)

Resources
=============
* [BetaNYC School Choice Wiki](https://github.com/BetaNYC/Tools-for-NYC-Council-and-Community-Boards/wiki/School-choice---transit-hacknight)
* [IZone DOE Data Sets](http://nycdoe.pediacities.com/)
* [Public Policy Lab Design Discovery](http://publicpolicylab.org/2014/02/the-school-choice-experience/)

Trip Planners
-------------
* Mapnificent
* OpenTripPlanner
* rrrr - https://github.com/bliksemlabs/rrrr

### Mapnificent
* [Site](http://www.mapnificent.net/)
* [Source](https://github.com/stefanw/Mapnificent)
* [API](http://www.mapnificent.net/docs/)

### OpenTripPlanner
* [Site](http://opentripplanner.com/)
* [Docs](http://opentripplanner.com/users-developers/)
* [Wiki](https://github.com/opentripplanner/OpenTripPlanner/wiki)
* [Tri-state implementation](https://docs.google.com/document/d/1n8wkqiRFMAxmgu-MYpCTriCokSzunKbeErfmnm1WyRI/edit)
* [Developer](https://twitter.com/globalvoid) - He's blogged/worked? for Open Plans

### GTFS Data Exchange
* [Site](http://www.gtfs-data-exchange.com/)
* [Source](https://github.com/jehiah/gtfs-data-exchange)
* [API](http://www.gtfs-data-exchange.com/api)
* [Developer](https://github.com/jehiah) - Based in NYC

### GTFS - Google Transit Feed Specification
* [Reference](https://developers.google.com/transit/gtfs/reference)
* [MTA Developers Site](http://web.mta.info/developers/)


Setup
===========

The following instructions assume that you already have Python 2.7 and pip installed on your computer. If not, please do so now. Then, install the required software by executing the following line:

```python
  sudo pip install -r requirements.txt
```

Usage
===========

There are two ways you can run the software.

### Commandline

```
  python lib/commute.py
```

Or:

### API

```
  python app.py
```




**LICENSE**
------------
**Parts of this project are based on code from [Mapnificent](http://www.mapnificent.net/) by [Stephan Wehrymeyer](http://stefanwehrmeyer.com/).The framework and layers are released under [Creative Commons by-nc-sa](http://creativecommons.org/licenses/by-nc-sa/3.0).**

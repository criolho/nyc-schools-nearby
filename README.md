nyc-schools-nearby
=============

App to help prospective NYC high school students filter a list of high schools within a set commute time.

Current Status
-------------

This project is currently not yet functioning. Please check out notes from the 

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

**LICENSE**
------------
**Parts of this project are based on code from [Mapnificent](http://www.mapnificent.net/) by [Stephan Wehrymeyer](http://stefanwehrmeyer.com/).The framework and layers are released under [Creative Commons by-nc-sa](http://creativecommons.org/licenses/by-nc-sa/3.0).**
**Analyzes EZproxy-generated log files and spits out a CSV with this info:**

* Filename of log being analyzed
* # total connections
* # on-campus connections (as determined by IP addresses starting with "10." -- may be different for your campus)
* % on-campus connections of total
* # off-campus connections
* % off-campus connections of total
* # library connections (as determined by IP addresses starting with "10.11" and "10.12" -- will almost certainly be different for your campus)
* % library of on-campus connections
* % library of total connections
* # student sessions off-campus
* % student sessions of total off-campus
* # fac/staff sessions off-campus
* % fac/staff sessions of total off-campus

Use it on the command line like so: 

**python ezp-analysis.py [directory to analyze -- should be SPU logs] [desired output filename.csv]**


"Sessions" are different from "connections." Sessions are when someone logs into EZproxy and does several things; a connection is a single HTTP request. Sessions can only be tracked if they're off-campus, as they rely on a session ID. On-campus EZproxy use can only be tracked with connections, which are less accurate. 


Make sure to change the IP address specifications as noted above. This is a pretty hacky script. I make no guarantees as to the accuracy of this script. Go over it with a fine-toothed comb and make sure your output lines up with what you see in your other data sources.

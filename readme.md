**Analyzes EZproxy-generated log files and spits out a CSV with this info:**

* Filename of log being analyzed
* Number of total connections
* Number of on-campus connections (as determined by IP addresses starting with "10." -- may be different for your campus)
* Percentage of on-campus connections out of total
* Number of off-campus connections
* Percentage of off-campus connections out of total
* Number of library connections (as determined by IP addresses starting with "10.11" and "10.12" -- will almost certainly be different for your campus)
* Percentage of on-campus connections (out of total connections)
* Percentage of library connections (out of total connections)
* Number of student sessions off-campus
* Percentage of student sessions out of total off-campus
* Number of fac/staff sessions off-campus
* Percentage of fac/staff sessions out of total off-campus

Use it on the command line like so: 

**python ezp-analysis.py [directory to analyze -- should be SPU logs] [desired output filename.csv]**


## Please note

* "Sessions" are different from "connections." Sessions are when someone logs into EZproxy and does several things; a connection is a single HTTP request. Sessions can only be tracked if they're off-campus, as they rely on a session ID. On-campus EZproxy use doesn't get a session ID and so can only be tracked with connections, which are less useful. On-campus use doesn't tell us anything about student vs. faculty use, for instance.
* Make sure to change the IP address specifications within the script. As it is, it counts "on campus" as IP addresses beginning with "10." and in-library as beginning with "10.11." or "10.12."
* This is a pretty hacky script. I make no guarantees as to the accuracy of this script. Go over it with a fine-toothed comb and make sure your output lines up with what you see in your other data sources.
* This output is only a sketch of how EZproxy may be used on your campus.
* Please take a good look at the logs you're analyzing and familiarize yourself with them — otherwise you may get the wrong idea about this script's output!

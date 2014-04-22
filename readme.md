Analyzes EZproxy-generated log files and spits out a CSV with this info: 

* Filename of log being analyzed
* total connections
* # on-campus connections
* % on-campus connections of total
* # off-campus connections
* % off-campus connections of total
* # library connections
* % library of on-campus connections
* % library of total connections
* # student sessions off-campus
* % student sessions of total off-campus
* # fac/staff sessions off-campus
* % fac/staff sessions of total off-campus

Use it on the command line like so: 

python ezp-analysis.py [directory to analyze] [desired output filename.csv]

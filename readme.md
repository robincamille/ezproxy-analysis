## About the Project
This Python 3 script analyzes Starting Point URL (SPU) logs from EZproxy to create a CSV file with aggregate data about EZproxy use.

**NOTE:** SPUs are the combined proxy prefix and target resource URL the user clicked to enter the resource.

## Getting Started
Before you run the script, you'll need to change the IP address range specifications within the script to match your institution.

This is done using a regular expression. For instance, let's say that all of the computers in your library have IP addresses that begin with *10.1.11*. Then in the script, you'll have this on line 67:

`libip = re.search(r'10\.1\.11\.\d+?\s-', line)`

**Tip:** In order to protect patron privacy, you shouldn't keep patron IP addresses for a long time. I first strip out the last 2 blocks in the IP address, so I can see whether users are on or off campus before using this script.

## Running the Script

Open the command-line or terminal and type:

`python ezp-analysis.py [directory of SPU logs to analyze] [desired output filename].csv`

The command line output will probably look like this:

![Screenshot of command line output](http://robincamille.com/assets/ezp-screenshot1.png)

## Output File

The CSV file contains the following information:

* Filename of the log being analyzed
* Number of total connections
* Number of on-campus connections (as determined by IP address range, **which you must edit before running the script**)
* Percentage of on-campus connections out of total
* Number of off-campus connections
* Percentage of off-campus connections out of total
* Number of library connections (as determined by IP address range, **which you must edit before running the script**)
* Percentage of on-campus connections (out of total connections)
* Percentage of library connections (out of total connections)
* Number of student sessions off-campus
* Percentage of student sessions out of total off-campus
* Number of faculty/staff sessions off-campus
* Percentage of faculty/staff sessions out of total off-campus

Screenshot of an output CSV:

![Screenshot of CSV output](http://robincamille.com/assets/ezp-screenshot2.png)

## Additional Information

* **Sessions** are different from *connections*. Sessions are when someone logs into EZproxy and does several things; a connection is a single HTTP request. Sessions can only be tracked if they're off-campus, as they rely on a session ID. On-campus EZproxy use doesn't get a session ID and so can only be tracked with connections, which are less useful. On-campus use doesn't tell us anything about student vs. faculty use, for instance.
* **SPU logs:** Run it over the SPU logs that EZproxy generates, not the full logs, as these shorter SPU logs take much less time to analyze and will give you a more useful connection count. SPU logs only count the "Starting Point URL" connections, rather than every single connection (javascript, .asp, favicon, etc.), which may not tell you much.

### Caveats

* This is a pretty hacky script. I make no guarantees as to its accuracy. Go over it with a fine-toothed comb and make sure your output lines up with what you see in your other data sources.
* This output is only a sketch of how EZproxy may be used on your campus.
* Please take a good look at the logs you're analyzing and familiarize yourself with them — otherwise you may get the wrong idea about this script's output!

## More details

My blog post about this script: http://robincamille.com/2014-04-22-analyzing-ezproxy-logs-python/

This script is also mentioned (briefly) in [*Coding for Librarians: Learning by Example*](https://www.alastore.ala.org/content/coding-librarians-learning-example) by Andromeda Yelton (2015).

## See also

A more ambitious EZproxy parsing project with a nice interface: https://github.com/ezpaarse-project/ezpaarse

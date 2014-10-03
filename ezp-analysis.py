# Robin Camille Davis
# 2014-03-28

## Script runs over all EZproxy-generated logs in a given directory.

## Must be edited with your organization's internal IP ranges. See two commented locations.

## Must be called on command line with this structure:
## python ezp-analysis.py [directory to analyze] [desired output filename.csv]

## Outputs a file with these columns:
    ## Filename of log
    ## total connections
    ## # on-campus connections
    ## % on-campus connections of total
    ## # off-campus connections
    ## % off-campus connections of total
    ## # library connections
    ## % library of on-campus connections
    ## % library of total connections
    ## # student sessions off-campus
    ## % student sessions of total off-campus
    ## # fac/staff sessions off-campus
    ## % fac/staff sessions of total off-campus

import re, sys, glob, os

def main():
    """EZproxy log analysis: count up student and faculty/staff sessions"""

    print 'EZproxy analysis beginning... This may take a few minutes.\n'

    dirname = sys.argv[1] #must be a directory
    output = sys.argv[2] #must be CSV

    outfile = open(output,"w")

    outfile.write('filename,total connections, # on-campus connections, % on-campus connections of total, \
# off-campus connections, % off-campus connections of total, # library connections, \
% library of on-campus connections, % library of total connections, # student sessions off-campus, \
% student sessions of total off-campus, # fac/staff sessions off-campus, % fac/staff sessions of \
total off-campus')

    for filename in glob.glob(os.path.join(dirname, '*.log')): #opens all log files in directory

        print 'Now analyzing', filename
        
        lines = [line.strip() for line in open(filename)] #reads file
        
        studcount = 0 #initialize counters 
        faccount = 0
        sessions = []
        oncampus = 0
        offcampus = 0
        libraryconnections = 0
        
        for line in lines:
            
            ipaddr = re.search(r'10\.\d+?\.\d+?\.\d+?\s-', line) # Edit this IP range
            if ipaddr:
                oncampus = oncampus + 1 #this counts all on-campus connections from 10.x.x.x
            else:
                offcampus = offcampus + 1 #this counts all other connections (off-campus)
                
            libip = re.search(r'10\.1\.11|2\.\d+?\s-', line) # Edit this IP range
                #this counts all connections from the library (10.1.11... or 10.1.12...)
            if libip:
                libraryconnections = libraryconnections + 1
                
            sessionid = re.search(r'.* - ([0-9A-Z].*?)\s', line)
                #session IDs are ONLY assigned to off-campus connections!
                #there may be multiple connections to multiple databases per session.
                #this counts all sessions.
                #note that on-campus sessions aren't tagged as student/faculty
            
            if sessionid:
                session = re.search(r'- .*', sessionid.group())
                session = session.group()[2:]
                if session not in sessions:
                    sessions.append(session)
                
                    stud = re.search( r'(Default\+OPAC\+Student)', line)
                    fac = re.search(r'(Default\+OPAC\+Staff)', line)
                    if stud:
                        studcount = studcount + 1 #counts all off-campus student sessions
                    if fac:
                        faccount = faccount + 1 #counts all off-campus faculty/staff sessions
                else:
                    pass
            else:
                pass

        total = offcampus + oncampus #all connections
        totalcountoffcamp = studcount + faccount #all offcampus sessions
        
        if totalcountoffcamp is not 0: #2008 logs issue
            studfrac = (float(studcount)/totalcountoffcamp) * 100 #students/total offcampus sessions
            facfrac = (float(faccount)/totalcountoffcamp) * 100 #faculty-staff/total offcampus sessions
        else:
            studfrac = 'n/a'
            facfrac = 'n/a'
            
        libfraccamp = (float(libraryconnections)/oncampus) * 100 # library/total oncampus connections
        libfrac = (float(libraryconnections)/total) * 100 #library/total connections
        offcampfrac = (float(offcampus)/total) * 100 #oncampus/total connections
        oncampfrac = (float(oncampus)/total) * 100 #offcampus/total connections

        outfile.write('\n')
        outfile.write(str(filename)  + ',' + str(total)  + ',' + str(oncampus) \
                      + ',' + str(oncampfrac)  + ',' + str(offcampus)  + ',' + \
                      str(offcampfrac)  + ',' + str(libraryconnections)  + ',' + \
                      str(libfraccamp)  + ',' + str(libfrac)  + ',' + \
                      str(studcount)  + ',' + str(studfrac)  + ',' + \
                      str(faccount)  + ',' + str(facfrac))


    outfile.close
    print '\nOutput:', outfile

main()



#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#import sys
import sys
import datetime
import my_class
import helgdagar as h

this_year = int(sys.argv[1])

def add_built_in_events(year):
    flaggdagar = h.Flaggdagar(year)
    helgdagar = h.Helgdagar(year)
    svarta_dagar = h.SvartaDagar(year)

    filename = "flaggdagar_".append(year).append(".ics")
    print filename
    f = open(filename, "w")
    for event_name, event_date in flaggdagar:
        f.write(event_name,",",event_date)
    f.close()
    
    f = open("flaggdagar_".append(year).append(".ics"), "w")
    for event_name, event_date in helgdagar:
        f.write(event_name,",",event_date)
    f.close()
    
    f = open("flaggdagar_".append(year).append(".ics"), "w")
    for event_name, event_date in svarta_dagar:
        f.write(event_name,",",event_date)
    f.close()

    return 0

add_built_in_events(this_year)


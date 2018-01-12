#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import my_class
import datetime
import calendar
import vobject
import pickle

#YEAR = 2009
this_year = int(sys.argv[1])
print this_year


def recurring_event(event):
    for child in event.getChildren():
	if child.name == "RRULE":
            return True
    return False


def parse_ics_file(source_type, event_name, filename, color, symbol):
    print "Parsing file for " + event_name + ":", filename
    ics_file = file(filename)
    ical = vobject.readOne(ics_file)

    #add each event to calendar
    for event in ical.vevent_list:
    	date = event.dtstart.value
	if isinstance(date, datetime.datetime): date = date.date()

        #fetch leap day
	if date.month == 2 and date.day == 29 and not calendar.isleap(this_year): continue

        # calculate anniversaries
        if event_name == "anniversary":
            age = this_year - date.year
            event.summary.value += " " + str(age)

        #check if events not belonging to current year are recurrent and should be applied anyway
	if date.year != this_year:
            if recurring_event(event):
                date = date.replace(year=this_year)
            else:
                continue

        #create a new field, content is taken from the event summary
        new_event = my_class.event(event_name, event.summary.value, color, symbol)
	my_container.get_day_by_date(date).add_event(new_event)
    return 0


def add_event(source_type, event_name, date, color, symbol):
    date = date.split('-')
    event_date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    new_event = my_class.event(event_name, event_name, color, symbol)
    my_container.get_day_by_date(event_date).add_event(new_event)
    return 0


#Create event_container object to host all events
my_container = my_class.event_container("My calendar", this_year)

#Construct calendar template for current year
for month in range(1,13):
    for date in range(1, 1+calendar.monthrange(this_year, month)[1]):
        this_day = datetime.datetime(this_year, month, date)
#        print date, this_day, this_day.weekday(), this_day.date()
	new_day = my_class.day(this_day.weekday(), this_day.date())
       	my_container.add_day(new_day)

#Read configuration file and load event sources
print "Parsing configuration file..."
conf_file = file("mycalendar.conf")
for line in conf_file:
    if line[0]=='#' or line=='\n': continue
    line=line.rstrip('\n').split()
    if line[0] == "calendar_name":
        calendar_name = ' '.join(line[1:])
        my_container.title = calendar_name
        print "Calendar name is changed to: "+ calendar_name
    elif line[0] == "ics": parse_ics_file(*line)
    elif line[0] == "single_event": add_event(*line)
conf_file.close()

print "Writing calendar to file \"myevents.cal\" ..."
cal_file = file("myevents.cal","w")
pickle.dump(my_container, cal_file)
cal_file.close()

#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import calendar
import pickle
import my_class

import sys

#YEAR = 2009
#YEAR = int(sys.argv[1])


print "Reading calendar from file..."
cal_file = file("myevents.cal")
my_container = pickle.load(cal_file)
cal_file.close()

calendar_name = my_container.title
year = my_container.year
print "Building calendar: " + calendar_name
template = calendar.Calendar()
my_cal = my_class.calendar(calendar_name, year)

for month in range(1,13):
    new_month = my_class.month(month)
    template_month = template.monthdatescalendar(year, month)
    for template_week in template_month:
        #A little bit of tinkering to get the week number
        new_week = my_class.week(template_week[0].isocalendar()[1])
	for template_day in template_week:
            if template_day.month == month:
                new_day = my_container.get_day_by_date(template_day)
#                print "Template_day.date:", template_day, my_container.get_day_by_date(template_day)
            else:
                new_day = my_class.day(template_day.weekday(), template_day)
            new_week.add_day(new_day)
        new_month.add_week(new_week)
#        sys.exit()
    my_cal.add_month(new_month)


print "Writing calendar to file \"mycalendar.cal\" ..."
cal_file = file("mycalendar.cal","w")
pickle.dump(my_cal, cal_file)
cal_file.close()

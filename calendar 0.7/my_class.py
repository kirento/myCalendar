#!/usr/local/bin/python
# -*- coding: utf-8 -*-


class event_container:
    def __init__(self, title, year):
	self.title = title
	self.year = year
	self.days = []

    def add_day(self, day):
	self.days.append(day)

    def get_day_by_date(self, date):
	for day in self.days:
            if day.date == date:
		return day
	return False


class calendar:
    def __init__(self, name, year):
	self.name = name
        self.year = year
	self.months = []

    def add_month(self, new_month):
	self.months.append(new_month)

    def get_month_by_number(self, month_nr):
	for month in self.months:
            if month.month_nr == month_nr:
		return month
	return False
	

class month:
    def __init__(self, month_nr):
        self.month_nr = month_nr
        self.weeks = []

    def add_week(self,new_week):
        self.weeks.append(new_week)

    def get_week_by_nr(self, week_nr):
	for week in self.weeks:
            if week.week_nr == week_nr:
		return week
	return False


class week:
    def __init__(self, week_nr):
	self.week_nr = week_nr
	self.days = []

    def add_day(self, new_day):
        self.days.append(new_day)

    def get_day_by_nr(self, weekday):
	for day in self.days:
            if day.weekday == weekday:
		return day
	return False


class day:
    def __init__(self, weekday, date):
	self.weekday = weekday
        self.date = date
	self.events = []

    def add_event(self, new_event, append=False):
        if append:
            # Look for existing event of same type
            existing_event = self.get_event_by_name(new_event.name)
            if not existing_event == False:
                print "Adding to existing event"
                content = []
                content.append(existing_event.content)
                content.append(', ')
                content.append(new_event.content)
                existing_event.content = ''.join(content)
                return False
        print "Creating new event: ", new_event.content
        self.events.append(new_event)
        return True

    def get_event_by_name(self, event_name):
	for event in self.events:
            if event.name == event_name:
		return event
        return False

    def find_event_double(self, new_event):
        for event in self.events:
            if new_event.name == "Namnsdagar": print new_event.name, event.name
            if (event.name_hash == hash(new_event.name)) and (event.content_hash == hash(new_event.content)):
                print "Dublett!", event.content
                return event
            #No double found
            if hash(event.name) == hash(new_event.name): print "Same name!"
            if hash(event.content) == hash(new_event.content):
                print "Same content!"
                print new_event.name
                print event.name
            return False
        #Event list is empty
        return False

class event:
    def __init__(self, name, content, color, symbol):
	self.name = name
        self.name_hash = hash(name)
	self.content = content
        self.content_hash = hash(content)
	self.text_color = color
	self.symbol = symbol
    
    def print_all(self):
        print "Name            :", self.name
        print "Name hash       :", self.name_hash
        print "Content         :", self.content
        print "Content hash    :", self.content_hash
        print "Color           :", self.text_color
        print "Symbol          :", self.symbol
        print ""


#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#import sys
import datetime
import my_class
import helgdagar


def add_built_in_events(year, event_container):
    flaggdagar = helgdagar.Flaggdagar(year)
    helgdagar = helgdagar.Helgdagar(year)
    svarta_dagar = helgdagar.SvartaDagar(year)

    for event_name, event_date in flaggdagar:
        new_event = my_class.event(event_name, event_name, black, symbol)
        event_container.get_day_by_date(event_date).add_event(new_event)
    
    for event_name, event_date in helgdagar:
        new_event = my_class.event(event_name, event_name, red, symbol)
        event_container.get_day_by_date(event_date).add_event(new_event)
    
    for event_name, event_date in svarta_dagar:
        new_event = my_class.event(event_name, event_name, black, symbol)
        event_container.get_day_by_date(event_date).add_event(new_event)
    return 0

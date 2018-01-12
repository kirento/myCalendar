#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime
import calendar
import pickle

MT_CORSIVA = "MTCORSVA.TTF"
MT_CORSIVA = "MonotypeCorsiva"
TAHOMA = "Tahoma"

#title = "Nora och Tims kalender"
#YEAR=2009
#YEAR=2010
#MONTH=1

PSP = 2.83464567

ORI_X = 10
ORI_Y = 20

PAGE_W = 297     #page width in mm
PAGE_H = 210     #page height in mm

TITLE_PAGE_NAME_X = PAGE_W/2
TITLE_PAGE_NAME_Y = PAGE_H/3
TITLE_PAGE_YEAR_X = PAGE_W/2
TITLE_PAGE_YEAR_Y = TITLE_PAGE_NAME_Y + 40

TILE_W = 35      #tile width in mm
TILE_H = 20	 #tile height in mm
TILE_SP_W = 4 
TILE_SP_H = 2
TITLE_H = 25
COL_HDR_H = 15   #height of 'column header line' i.e. weekday names
WEEK_NR_W = 5    #width of 'week number column'

# Offsets inside the cells
DATE_OFFS_X = 4  #x offset for date
DATE_OFFS_Y = 5  #y offset for date
EVENT_OFFS_X = 10 #x offset for events
EVENT_OFFS_Y = 3 #y offset for 1st row of events
EVENT_SPACING_Y = 2.5 #y spacing between events
SYMB_OFFS_X = 28.5 #x offset for symbol
SYMB_OFFS_Y = 0  #y offset for symbol
SYMB_SPACING_X = -20

#Text size definitions
TITLE_PAGE_YEAR_SIZE = 28
TITLE_PAGE_TEXT_SIZE = 18
TITLE_SIZE = 14
LARGE = 7
SMALL = 4
TINY = 3
PICO = 2.3

#Origin for objects

#Title
TITLE_X = PAGE_W/2
TITLE_Y = ORI_Y + TITLE_H

#Column header
COL_HDR_X = ORI_X + WEEK_NR_W
COL_HDR_Y = ORI_Y + TITLE_H


TILE_X = ORI_X + WEEK_NR_W
TILE_Y = ORI_Y + TITLE_H + COL_HDR_H

#Color definitions
BLACK = [0, 0, 0]
GRAY = [0.7, 0.7, 0.7]
RED = [1, 0, 0]
PURPLE = [1, 0, 0.1]

color_code = {'black': [0, 0, 0], 'gray': [0.7, 0.7, 0.7], 'red': [1, 0, 0], 'purple': [1, 0, .8], 'blue': [0, 0.5, 0.9]}

month_name = {1:'Januari', 2:'Februari', 3:'Mars', 4:'April', 5:'Maj', 6:'Juni', 7:'Juli', 8:'Augusti', 9:'September', 10:'Oktober', 11:'November', 12:'December'}

#weekday_name = {0:'M\345ndag', 1:'Tisdag', 2:'Onsdag', 3:'Torsdag', 4:'Fredag', 5:'L\366rdag', 6:'S\366ndag'}
#weekday_name = {0:'Mandag', 1:'Tisdag', 2:'Onsdag', 3:'Torsdag', 4:'Fredag', 5:'Lordag', 6:'Sondag'}
weekday_name = {0:u'Måndag', 1:u'Tisdag', 2:u'Onsdag', 3:u'Torsdag', 4:u'Fredag', 5:u'Lördag', 6:u'Söndag'}


class TextObject:
    def __init__(self, x, y, string, font, size, color, align="left"):
        self.x = x
        self.y = y
        self.string = string
        self.font = font
        self.size = size
        self.color = color
        self.align = align

class PathObject:
    def __init__(self, x, y, color, intensity, width):
        self.x = x
        self.y = y
        self.color = color
        self.intensity = intensity
        self.width = width

class EPSObject:
    def __init__(self, x, y, file_name):
        self.x = x
        self.y = y
        self.file_name = file_name

class PathObjectTemplates:
    def __init__(self, ID):
        self.ID = ID
        self.objects = []

    def add_object(self, name, object):
        self.objects.append(name, object)

    def get_object_by_name(self, name):
        for object in objects:
           if object[0] == name: return object.object
           return False

class CalendarSheet:
    def __init__(self, SheetID):
        self.SheetID = SheetID
        self.objects = []
#        self.text_objects = []
#        self.path_objects = []

    def add_object(self, object):
#        if isinstance(object, TextObject): self.text_objects.append(object)
#        if isinstance(object, PathObject): self.path_objects.append(object)
        self.objects.append(object)
        
#----------------------------------------------------------------------------------
# PS functions
#
# Post Script text typing "macros"
#
#----------------------------------------------------------------------------------

def PS_move(x, y):
    return str(x) + " " + str(-y) + " moveto\n"


def PS_rmove(x, y):
    return str(x) + " " + str(y) + " rmoveto\n"


def PS_line(x, y):
    return str(x) + " " + str(-y) + " lineto\n"


def PS_rline(x, y):
    return str(x) + " " + str(y) + " rlineto\n"


def PS_set_color(color):
    seq = []
    seq.append(str(color_code[color][0])+" "+str(color_code[color][1])+" "+str(color_code[color][2])+" setrgbcolor\n")
    return ''.join(seq)


def PS_set_intensity(intensity):
    seq = []
    seq.append(str(intensity)+" setgray\n")
    return ''.join(seq)


def PS_set_font(font, size):
    seq = []
    seq.append("/"+font+" findfont "+str(size)+" scalefont setfont\n")
    return ''.join(seq)
    
    
def PS_set_line_width(width):
    seq = []
    seq.append(str(width)+" setlinewidth\n")
    return ''.join(seq)


def PS_align_l(string):
    return "("+string+")"


def PS_align_c(string):
    return "("+string+") dup stringwidth pop 2 div neg 0 rmoveto"


def PS_print_text(text):
    seq = []
    seq.append(PS_set_color(text.color))
    seq.append(PS_set_font(text.font, text.size))
    seq.append(PS_move(text.x, text.y))
    if text.align == "left":
        seq.append(PS_align_l(text.string))
    elif text.align == "center":
        seq.append(PS_align_c(text.string))
    else: # default is left aligned
        seq.append(PS_align_l(string))
    seq.append(" show\n")
    """
    seq.append(PS_move(text.x - 12, text.y))
    seq.append(PS_align_l(str(len(text.string))))
    seq.append(" show\n")
    """

    if len(text.string) > 22: print len(text.string), text.string

    return ''.join(seq)


def PS_draw_path(path):
    seq = []
    seq.append("newpath\n")
    seq.append(PS_set_color(path.color))
    seq.append(PS_set_line_width(path.width))
    seq.append(PS_move(path.x[0], path.y[0]))
    for n in range(1, len(path.x)):
        seq.append(PS_rline(path.x[n], path.y[n]))
    seq.append("stroke\n")
    return ''.join(seq)


def PS_draw_EPSObject(object):
    seq = []

    seq.append("gsave\n")
    seq.append(str(object.x) + " " +  str(-object.y) + " translate\n")
    seq.append(str(1/PSP) + " " + str(1/PSP) + " scale\n")
    EPS_file = open(object.file_name, 'r')
    seq.append(''.join(EPS_file.readlines()))
    EPS_file.close ()
    seq.append("grestore\n")
    return ''.join(seq)

#----------------------------------------------------------------------------------


def draw_title_page(Sheet, title, year):
    font = MT_CORSIVA
    color = 'black'

    #Print calendar title
    size = TITLE_PAGE_TEXT_SIZE
    x = TITLE_PAGE_NAME_X
    y = TITLE_PAGE_NAME_Y
    Sheet.add_object(TextObject(x, y, title, font, size, color, "center"))

    #Print year
    size = TITLE_PAGE_YEAR_SIZE
    x = TITLE_PAGE_YEAR_X
    y = TITLE_PAGE_YEAR_Y
    Sheet.add_object(TextObject(x, y, str(year), font, size, color, "center"))
    

def draw_title(Sheet, month):
    font = MT_CORSIVA
    size = TITLE_SIZE
    color = 'black'

    x = PAGE_W/2
    y = ORI_Y + TITLE_H - 5

    Sheet.add_object(TextObject(x, y, month_name[month]+" "+str(year), font, size, color, "center"))



def draw_column_headers(Sheet):
    font = MT_CORSIVA
    size = LARGE
    color = 'black'
    int = 1
    width = .1

    for wday in range(0,7):
        # Weekday names
        x = COL_HDR_X + wday*(TILE_W + TILE_SP_W) + 0.5*TILE_W
        y = COL_HDR_Y + 0.5*TILE_H
        Sheet.add_object(TextObject(x, y, weekday_name[wday], font, size, color, "center"))

        # Line
        x = COL_HDR_X + wday*(TILE_W + TILE_SP_W)
        y = COL_HDR_Y + COL_HDR_H
        Sheet.add_object(PathObject([x, TILE_W], [y, 0], color, int, width))


def draw_tile(Sheet, col, row, day):
    color = "black"
    int = 1
    width = 0.1

    x_tile = TILE_X + col*(TILE_SP_W + TILE_W)
    y_tile = TILE_Y + row*(TILE_SP_H + TILE_H) + TILE_SP_H

#Print events and symbols
    font = TAHOMA
    size = PICO

    x_event = x_tile + EVENT_OFFS_X

    event_row = 0
    symbol_count = 0
    for event in day.events:
#        print event.name
        if event.name == "date_color": continue

        if (row == 5 and day.date.day > 29):
            #lower half of shared cell
            y_event = y_tile - 0.5*TILE_H - TILE_SP_H + EVENT_OFFS_Y + event_row*EVENT_SPACING_Y
            y_symbol = y_tile - 0.5*TILE_H - TILE_SP_H + SYMB_OFFS_Y
        else:
            y_event = y_tile + EVENT_OFFS_Y + event_row*EVENT_SPACING_Y
            y_symbol = y_tile + SYMB_OFFS_Y

        if not event.text_color == '*':
            if len(event.content) > 22:
                print event.content + " > 22 chars"
                string = event.content.rsplit(None, 1)
                print string
                Sheet.add_object(TextObject(x_event, y_event, string[0], font, size, event.text_color, "left"))
                event_row +=1
                y_event = y_tile + EVENT_OFFS_Y + event_row*EVENT_SPACING_Y
                Sheet.add_object(TextObject(x_event, y_event, string[1], font, size, event.text_color, "left"))
#Fulhack för att få plats med "Johanes Döparens Dag" tillsammans med flagga 2017
	    elif day.date.year == 201 and day.date.month == 6 and day.date.day == 24 and len(event.content) > 18:
		print "FULHACK!!" + str(len(event.content))
                print event.content + " > 18 chars"
                string = event.content.split(None, 1)
                print string
                Sheet.add_object(TextObject(x_event, y_event, string[0], font, size, event.text_color, "left"))
                event_row +=1
                y_event = y_tile + EVENT_OFFS_Y + event_row*EVENT_SPACING_Y
                Sheet.add_object(TextObject(x_event, y_event, string[1], font, size, event.text_color, "left"))
#--------------------------------------------------------------------------
            else:
                Sheet.add_object(TextObject(x_event, y_event, event.content, font, size, event.text_color, "left"))
            event_row += 1

        if not event.symbol == '*':
            x_symbol = x_tile + SYMB_OFFS_X + symbol_count*SYMB_SPACING_X
            Sheet.add_object(EPSObject(x_symbol, y_symbol, event.symbol))
            symbol_count += 1
            
            
#Date and guide line 1
    x_date = x_tile + DATE_OFFS_X
    y_date = y_tile + DATE_OFFS_Y
    color_date = "black"
    x_line = x_tile
    y_line = y_tile + 2*TILE_H/5
    color_line = "gray"
    int = 0.1

    draw_guide_lines = 1
    print_date = 1
    draw_frame = 1

    color = day.get_event_by_name("date_color")
#    print type(color), color
    if not color == False: color_date = color.text_color


    if (row == 4 and calendar.monthrange(year, day.date.month)[1] - day.date.day > 6 and day.date.day > 22):
        #upper half of shared cell
        size = LARGE
        #no guide lines
        draw_guide_lines = 0
#        y_date = y_tile + TILE_H/3
        y_date = y_tile + DATE_OFFS_Y
#        y_line = y_tile + TILE_H/2
        y_line = y_tile + TILE_H*5/11
        y_event = y_date
        color_line = "black"
        Sheet.add_object(PathObject([x_line, TILE_W], [y_line, 0], color_line, int, width))

    elif (row == 5 and day.date.day > 29):
        #lower half of shared cell
        size = LARGE
        #no guide lines
        draw_guide_lines = 0
        draw_frame = 0
        y_tile = y_tile - 0.5*TILE_H - TILE_SP_H 
#        y_date = y_tile + TILE_H/3
        y_date = y_tile + DATE_OFFS_Y
        y_event = y_date

    elif (row == 5 and day.date.day < 7): #cell that should not be printed
        draw_guide_lines = 0
        print_date = 0
        draw_frame = 0

    elif (row == 0 and day.date.day > 8) or (row == 4 and day.date.day < 7): #filling day
        size = SMALL
        #long line
        Sheet.add_object(PathObject([x_line, TILE_W], [y_line, 0], color_line, int, width))

    elif col == 6: #sunday
        size = LARGE
        #short line
        if event_row < 3: Sheet.add_object(PathObject([x_line + EVENT_OFFS_X , TILE_W - EVENT_OFFS_X], [y_line, 0], color_line, int, width))
#        Sheet.add_object(PathObject([x_line + EVENT_OFFS_X , TILE_W - EVENT_OFFS_X], [y_line, 0], color_line, int, width))
        color_date = "red"

    else: #weekday
        size = LARGE
        #short line
        if event_row < 3: Sheet.add_object(PathObject([x_line + EVENT_OFFS_X , TILE_W- EVENT_OFFS_X], [y_line, 0], color_line, int, width))
#        Sheet.add_object(PathObject([x_line + EVENT_OFFS_X , TILE_W- EVENT_OFFS_X], [y_line, 0], color_line, int, width))

#Print date
    if print_date:
        font = MT_CORSIVA
        Sheet.add_object(TextObject(x_date, y_date, str(day.date.day), font, size, color_date, "center"))


#Draw tile frame
    if draw_frame:
        color = "black"

        x_frame = [x_tile, TILE_W, 0]
        y_frame = [y_tile + TILE_H, 0, TILE_H]
        Sheet.add_object(PathObject(x_frame, y_frame, color, int, width))


#Guide lines 2 and 3 (long)
    if draw_guide_lines:
        color = "gray"

        y_line = y_tile + 3*TILE_H/5
        Sheet.add_object(PathObject([x_line, TILE_W], [y_line, 0], color, int, width))

        y_line = y_tile + 4*TILE_H/5
        Sheet.add_object(PathObject([x_line, TILE_W], [y_line, 0], color, int, width))




def draw_week(Sheet, week, row):
    font = MT_CORSIVA
    size = SMALL
    color = "black"

    x = ORI_X
    y = ORI_Y + TITLE_H + COL_HDR_H + (1+row)*TILE_SP_H + (0.5+row)*TILE_H

    #Draw week number
    if row < 5: Sheet.add_object(TextObject(x, y, str(week.week_nr), font, size, color, "center"))

    #Draw tiles
    for weekday in range(0, 7):
        draw_tile(Sheet, weekday, row, week.get_day_by_nr(weekday))


def draw_sheet(Sheet, month):
    #Draw title
    draw_title(Sheet, month.month_nr)

    #Draw column headers
    draw_column_headers(Sheet)

    #Draw weeks
    row = 0
    for week in month.weeks:
        draw_week(Sheet, week, row)
        row += 1


def print_sheet(Sheet):
    seq = []
    for object in Sheet.objects:
        if isinstance(object, TextObject):
            seq.append(PS_print_text(object))
        elif isinstance(object, PathObject):
            seq.append(PS_draw_path(object))
        elif isinstance(object, EPSObject):
            seq.append(PS_draw_EPSObject(object))
    return ''.join(seq)


def embed_fonts():
    seq = []

    font_file = open("MTCORSVA.TTF.pfa",'r')
    seq.append(''.join(font_file.readlines()))
    font_file.close()

    font_file = open("tahoma.pfa",'r')
    seq.append(''.join(font_file.readlines()))
    font_file.close()

    return ''.join(seq)


def write_document_header():
    seq = []

    seq.append("%!PS\n")
    #seq.append("%%Creator: (my_calendar)\n%%CreationDate: (Tue Nov 4 15:42:04 2008)\n%%Title: (kalender 2009)\n%%Pages: (atend)\n%%PageOrder: Ascend\n%%EndComments\n")
    seq.append("%%DocumentPaperSizes: a4\n")
    seq.append("%%Orientation: Landscape\n")
    seq.append("%%Pages: 12\n")
    return ''.join(seq)


def write_page_header(page_nr):
    seq = []

    seq.append("gsave\n")
#    seq.append("%%Page:" + str(page_nr) + "\n")
    seq.append("%%Page:\n")
    return ''.join(seq)


def write_page_footer():
    seq = []

    seq.append("showpage\n")
    seq.append("grestore\n")
    return ''.join(seq)


def write_document_footer():
    seq = []

    #o_footer = ["showpage\n"]
    #o_footer.append("%%PageTrailer\n\n%%Trailer\n%%BoundingBox: 0 0 210 297\n%%Pages: 1\n%%EOF")
    #o_file.writelines(o_footer)
    return ''.join(seq)
    


print "Reading calendar data from file..."
cal_file = file("mycalendar.cal")
my_calendar = pickle.load(cal_file)
cal_file.close()
print "Done."

calendar_name = my_calendar.name
year = my_calendar.year
print "Calendar title: " + calendar_name
print "Year: " + str(year)

#Open output file
print "Writing calendar to file my_calendar.ps ..."
o_file = open("my_calendar.ps",'w')

seq = []

#Write document header
seq.append(write_document_header())
seq = ''.join(seq)
seq = seq.encode('latin1')
o_file.write(seq)

seq = []
#Embed fonts
#seq.append(embed_fonts())

font_file = open("MTCORSVA.TTF.pfa",'r')
o_file.writelines(font_file.readlines())
font_file.close()

font_file = open("tahoma.pfa",'r')
o_file.writelines(font_file.readlines())
font_file.close()


#Set page orientation and scaling
#seq.append("gsave\n")
seq.append("90 rotate\n")
seq.append("2.83464567 2.83464567 scale\n")

#Draw and print title page
seq.append(write_page_header(1))
Sheet = CalendarSheet("title_page")
draw_title_page(Sheet, calendar_name, year)
seq.append(print_sheet(Sheet))
seq.append(write_page_footer())

#Draw sheets
for month in my_calendar.months:
    seq.append(write_page_header(month.month_nr + 1))
#    if month.month_nr > 1: continue # Uncomment to only print t¸he first month.
#    if month.month_nr > 2: continue # Uncomment to only print the first two month.
#    if not month.month_nr == 11: continue # Uncomment to only print month number 11
    Sheet = CalendarSheet(str(month_name[month.month_nr]))

#    seq.append("newpage\n")
    draw_sheet(Sheet, month)
    seq.append(print_sheet(Sheet))
    seq.append(write_page_footer())

#Write PS footer
seq.append(write_document_footer())

seq = ''.join(seq)
#seq = seq.encode('utf-8')
#seq = translate(seq)
seq = seq.encode('latin1')
o_file.write(seq)
#sys.exit()


#Close output file
o_file.close()
print "Done."


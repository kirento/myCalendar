#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#import sys
import datetime

weekdays = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday':7}

def Flaggdagar(year):
    flaggdagar = {'Nyårsdagen': Nyarsdagen(year),
                  'Konungens namnsdag': KonungensNamnsdag(year),
                  'Kronprinsessans namnsdag': KronprinsessansNamnsdag(year),
                  'Påskdagen': Paskdagen(year),
                  'Konungens födelsedag': KonungensFodelsedag(year),
                  'Första maj': ForstaMaj(year),
                  'Pingstdagen': Pingstdagen(year),
                  'Sveriges nationaldag': SverigesNationaldag(year),
                  'Midsommardagen': Midsommardagen(year),
                  'Kronprinsessans födelsedag': KronprinsessansFodelsedag(year),
                  'Drottningens namnsdag': DrottningensNamnsdag(year),
                  'Riksdagsval': Riksdagsval(year),
                  'FN-dagen': FNdagen(year),
                  'Gustav Adofsdagen': GustavAdolfsdagen(year),
                  'Nobeldagen': Nobeldagen(year),
                  'Drottningens födelsedag': DrottningensFodelsedag(year),
                  'Juldagen': Juldagen(year)
              }
    return flaggdagar


def Helgdagar(year):
    helgdagar = {'Nyårsdagen': Nyarsdagen(year),
                 'Trettondedag jul': TrettondedagJul(year),
                 'Långfredagen': Langfredagen(year),
                 'Påskdagen': Paskdagen(year),
                 'Annandag påsk': AnnandagPask(year),
                 'Första maj': ForstaMaj(year),
                 'Kristi himmelsfärdsdag': KristiHimmelsfardsdag(year),
                 'Pingstdagen': Pingstdagen(year),
                 'Sveriges nationaldag': SverigesNationaldag(year),
                 'Midsommardagen': Midsommardagen(year),
                 'Alla helgons dag': AllaHelgonsDag(year),
                 'Juldagen': Juldagen(year),
                 'Annandag jul': AnnandagJul(year)
             }
    return helgdagar


def SvartaDagar(year):
    svarta_dagar = {'Vårdagjämningen': Vardagjamningen(year),
                    'Sommarsolståndet': Sommarsolstandet(year),
                    'Höstdagjämningen':	Hostdagjamningen(year),
                    'Vintersolståndet':	Vintersolstandet(year),
                    'Fettisdagen': Fettisdagen(year),
                    'Annandag pingst': AnnandagPingst(year),
                    'Mårtensafton': Martensafton(year),
                    'Värnlösa barns dag': VarnlosaBarnsDag(year),
                    'Luciadagen': Luciadagen(year),
                    'Tjugondedag jul': TjugondedagJul(year),
                    'Trettondagsafton':	Trettondagsafton(year),
                    'Skärtorsdag': Skartorsdag(year),
                    'Påskafton': Paskafton(year),
                    'Valborgsmässoafton': Valborgsmassoafton(year),
                    'Pingstafton': Pingstafton(year),
                    'Midsommarafton': Midsommarafton(year),
                    'Julafton': Julafton(year),
                    'Nyårsafton': Nyarsafton(year),
                    'Alla hjärtans dag': AllaHjartansDag(year),
                    'Gustav Adolfsdagen': GustavAdolfsdagen(year),
                    'Nobeldagen': Nobeldagen(year),
                    'Våffeldagen': Vaffeldagen(year),
                    'Sommartid börjar': SommartidBorjar(year),
                    'Allmän självdeklaration': AllmanSjalvdeklaration(year),
                    'Sommartid slutar':	SommartidSlutar(year),
                    'Konungens namnsdag': KonungensNamnsdag(year),
                    'Internationella kvinnodagen': InternationellaKvinnodagen(year),
                    'Kronprinsessans namnsdag':	KronprinsessansNamnsdag(year),
                    'Konungens födelsedag': KonungensFodelsedag(year),
                    'Mors dag':	MorsDag(year),
                    'Kronprinsessans födelsedag': KronprinsessansFodelsedag(year),
                    'Drottningens namnsdag': DrottningensNamnsdag(year),
                    'Kanelbullens dag':	KanelbullensDag(year),
                    'Internationela barndagen':	InternationelaBarndagen(year),
                    'FN-dagen':	FN-dagen(year),
                    'Fars dag':	FarsDag(year),
                    'Drottningens födelsedag': DrottningensFodelsedag(year)
    }
    return svarta_dagar


# =================================
def GaussEasterAlgorithm(year):
    a = year % 19
    b = year % 4
    c = year % 7

    k = floor(year/100)
    p = floor((13 + 8*k)/25)
    q = floor(k/4)
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7

    d = (19*a + M) % 30
    e = (2*b + 4*c + 6*d + N) % 7

    # Gregorian Easter is 22 + d + e March or d + e − 9 April
    # if d = 29 and e = 6, replace 26 April with 19 April
    # if d = 28, e = 6, and (11M + 11) mod 30 < 19, replace 25 April with 18 April

    day = 22 + d + e
    month = 3
    if day > 31:
        day = d + e - 9
        month = 4
    if d == 29 and e == 6 and day == 26 and month == 4:
        day = 19
    if d == 28 and e == 6 and (11*M + 11) % 30 < 19 and day == 25 and month == 4:
        day = 18
    return year, month, day


def IanTaylorEasterJscr(year): #From Wikipedia
    a = year % 19
    b = year >> 2
    c = b // 25 + 1
    d = (c * 3) >> 2
    e = ((a * 19) - ((c * 8 + 5) // 25) + d + 15) % 30
    e += (29578 - a - e * 32) >> 10
    e -= ((year % 7) + b - d + e + 2) % 7
    d = e >> 5
    day = e - d * 31
    month = d + 3
    return year, month, day


def Easter(year):
    return IanTaylorEasterJscr(year)

# =================================


# =========== RELIGIOUS ===========
# Trettondedag jul
def TrettondedagJul(year):
    day = 6
    month = 1
    return datetime.date(year, month, day)

#Påskdagen
def Paskdagen(year):
    return Easter(year)

#Annandag påsk
def AnnandagPask(year):
    return Easter(year) + datetime.timedelta(days=1)

#Påskafton
def Paskafton(year):
    return Easter(year) + datetime.timedelta(days=-1)

#Långfredagen
def Langfredagen(year):
    return Easter(year) + datetime.timedelta(days=-2)

#Skärtorsdagen
def Skartorsdagen(year):
    return Easter(year) + datetime.timedelta(days=-3)

#Fettisdagen
def Fettisdagen(year):
    date = Easter(year) + datetime.timedelta(days=-40)
    date = date + datetime.timedelta(((date.isoweekday() - weekdays['tuesday'] - 1) % 7) + 1) #Tuesday 40 days before easter

#Kristi himmelsfärdsdag
def KristiHimmelsfardsdag(year):
    return Easter(year) + datetime.timedelta(days=39) #6th Thursday after easter (5*7+4=39 days)

#Pingstafton
def Pingstafton(year):
    return Easter(year) + datetime.timedelta(days=48)

#Pingstdagen
def Pingstdagen(year):
    return datetime.date(Easter(year)) + datetime.timedelta(days=49) #7th Sunday after easter (7*7=49 days)

#Annandag pingst
def AnnandagPingst(year):
    return Easter(year) + datetime.timedelta(days=50)

#Alla helgons dag
def AllaHelgonsDag(year):
    day = 31
    month = 10
    date = datetime.date(year, month, year)
    date = date + datetime.timedelta((weekdays['saturday'] - date.isoweekday()) % 7) #1st Saturday after 'October 31'
    return date

#Julafton
def Julafton(year):
    day = 24
    month = 12
    return datetime.date(year, month, day)
    
#Juldagen
def Juldagen(year):
    day = 25
    month = 12
    return datetime.date(year, month, day)

#Annandag jul
def AnnandagJul(year):
    day = 26
    month = 12
    return datetime.date(year, month, day)

#Värnlösa barns dag
def VarnlosaBarnsDag(year):
    day = 28
    month = 12
    return datetime.date(year, month, day)
# =================================


# =========== CULTURAL ============
#Nyårsdagen
def Nyarsdagen(year):
    day = 1
    month = 1
    return datetime.date(year, month, day)

#Tjugondedag jul
def TjugondedagJul(year):
    day = 13
    month = 1
    return datetime.date(year, month, day)

#Konungens namnsdag
def KonungensNamnsdag(year):
    day = 28
    month = 1
    return datetime.date(year, month, day)

#Alla hjärtans dag
def AllaHjartansDag(year):
    day = 14
    month = 2
    return datetime.date(year, month, day)

#Våffeldagen
def Vaffeldagen(year):
    day = 25
    month = 3
    return datetime.date(year, month, day)

#Internationella kvinnodagen
def InternationellaKvinnodagen(year):
    day = 8
    month = 3
    return datetime.date(year, month, day)

#KronprinsessansNamnsdag
def KronprinsessansNamnsdag(year):
    day = 8
    month = 3
    return datetime.date(year, month, day)

#Konungens födelsedag
def KonungensFodelsedag(year):
    day = 30
    month = 3
    return datetime.date(year, month, day)

#Sommartid börjar
def SommartidBorjar(year):
    day = 31
    month = 3
    date = datetime.date(year, month, year)
    date = date - datetime.timedelta(((date.isoweekday() - weekdays['sunday'] - 1) % 7) + 1) #Last Sunday of March
    return date

#Valborgsmässoafton
def Valborgsmassoafton(year):
    day = 30
    month = 4
    return datetime.date(year, month, day)

#Första maj
def ForstaMaj(year):
    day = 1
    month = 5
    return datetime.date(year, month, day)

#Allmän självdeklaration
def AllmanSjalvdeklaration(year):
    day = 1
    month = 5
    date = datetime.date(year, month, year)
    DateFound = False
    while not DateFound:
        date = date + datetime.timedelta(1)
        if weekday[monday] <= date.isoweekday() <= weekday[friday] and not KristiHimmelsfardsdag(date.year) == date: #1st weekday of May not being a holiday
            DateFound = True
    return date

#Mors dag
def MorsDag(year):
    day = 31
    month = 5
    date = datetime.date(year, month, year)
    date = date - datetime.timedelta(((date.isoweekday() - weekdays['sunday'] - 1) % 7) + 1) #Last Sunday of May
    return date

#Sveriges nationaldag
def SverigesNationaldag(year):
    day = 6
    month = 6
    return datetime.date(year, month, day)

#Midsommar
def Midsommar(year):
    day = 20
    month = 6
    date = datetime.date(year, month, year)
    date = date + datetime.timedelta((weekdays['saturday'] + 7 - date.isoweekday()) % 7) #1st Saturday after 'June 20'
    return date

#Kronprinsessans födelsedag
def KronprinsessansFodelsedag(year):
    day = 14
    month = 7
    return datetime.date(year, month, day)

#Drottningens namnsdag
def DrottningnensNamnsdag(year):
    day = 8
    month = 8
    return datetime.date(year, month, day)

#Riksdagsval
def Riksdagsval(year):
    day = 1
    month = 9
    date = datetime.date(year, month, year)
    date = date + datetime.timedelta(((weekdays['saturday'] + 7 - date.isoweekday()) % 7) + 7) #2nd Saturday of September
    if (year - 2000) % 4 == 0:
        return date
    else:
        return Null

#Kanelbullens dag
def KanelbullensDag(year):
    day = 4
    month = 10
    return datetime.date(year, month, day)

#Internationella barndagen
def InternationellaBarndagen(year):
    day = 5
    month = 10
    return datetime.date(year, month, day)

#FN-dagen
def FNdagen(year):
    day = 24
    month = 10
    return datetime.date(year, month, day)

#Sommartid slutar
def SommartidSlutar(year):
    day = 31
    month = 10
    date = datetime.date(year, month, year)
    date = date - datetime.timedelta(((date.isoweekday() - weekdays['sunday'] - 1) % 7) + 1) #Last Sunday of October
    return date

#Gustaf Adolfsdagen
def GustafAdofsdagen(year):
    day = 6
    month = 11
    return datetime.date(year, month, day)

#Mårtensafton
def Martensafton(year):
    day = 10
    month = 11
    return datetime.date(year, month, day)

#Fars dag
def FarsDag(year):
    day = 1
    month = 11
    date = datetime.date(year, month, year)
    date = date + datetime.timedelta(((weekdays['saturday'] + 7 - date.isoweekday()) % 7) + 7) #2nd Saturday of November
    return date

#Nobeldagen
def Nobeldagen(year):
    day = 10
    month = 12
    return datetime.date(year, month, day)

#Luciadagen
def Luciadagen(year):
    day = 13
    month = 12
    return datetime.date(year, month, day)

#Drottningens födelsedag
def DrottningnensFodelsedag(year):
    day = 23
    month = 12
    return datetime.date(year, month, day)
# =================================


# ========= ASTRONOMICAL ==========
#Vårdagjämning
def Vardagjamning(year):
    spring_equinox = {2010:datetime(2010,3,20),
                      2011:datetime(2011,3,20),
                      2012:datetime(2012,3,20),
                      2013:datetime(2013,3,20),
                      2014:datetime(2014,3,20),
                      2015:datetime(2015,3,20),
                      2016:datetime(2016,3,20),
                      2017:datetime(2017,3,20),
                      2018:datetime(2018,3,20),
                      2019:datetime(2019,3,20),
                      2020:datetime(2020,3,20)}
    return spring_equinox[year]

#Sommarsolståndet
def Sommarsolstandet(year):
    summer_solstice = {2010:datetime(2010,6,21),
                       2011:datetime(2011,6,21),
                       2012:datetime(2012,6,20),
                       2013:datetime(2013,6,21),
                       2014:datetime(2014,6,21),
                       2015:datetime(2015,6,21),
                       2016:datetime(2016,6,20),
                       2017:datetime(2017,6,21),
                       2018:datetime(2018,6,21),
                       2019:datetime(2019,6,21),
                       2020:datetime(2020,6,20)}
    return summer_solstice[year]

#Höstdagjämning
def Hostdagjamning(year):
    fall_equinox = {2010:datetime(2010,9,23),
                    2011:datetime(2011,9,23),
                    2012:datetime(2012,9,22),
                    2013:datetime(2013,9,22),
                    2014:datetime(2014,9,23),
                    2015:datetime(2015,9,23),
                    2016:datetime(2016,9,22),
                    2017:datetime(2017,9,22),
                    2018:datetime(2018,9,23),
                    2019:datetime(2019,9,23),
                    2020:datetime(2020,9,22)}
    return fall_equinox[year]

#Vintersolståndet
def Vintersolstandet(year):
    winter_solstice = {2010:datetime(2010,12,21),
                       2011:datetime(2011,12,22),
                       2012:datetime(2012,12,21),
                       2013:datetime(2013,12,21),
                       2014:datetime(2014,12,21),
                       2015:datetime(2015,12,22),
                       2016:datetime(2016,12,21),
                       2017:datetime(2017,12,21),
                       2018:datetime(2018,12,21),
                       2019:datetime(2019,12,22),
                       2020:datetime(2020,12,21)}
    return winter_solstice[year]
# =================================

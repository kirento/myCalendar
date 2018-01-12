#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import datetime

weekdays = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}


def flaggdagar(year):
	flaggdagar = {'Nyårsdagen': nyarsdagen(year),
	              'Konungens namnsdag': konungens_namnsdag(year),
	              'Kronprinsessans namnsdag': kronprinsessans_namnsdag(year),
	              'Påskdagen': paskdagen(year),
	              'Konungens födelsedag': konungens_fodelsedag(year),
	              'Första maj': forsta_maj(year),
	              'Pingstdagen': pingstdagen(year),
	              'Sveriges nationaldag': sveriges_nationaldag(year),
	              'Midsommardagen': midsommardagen(year),
	              'Kronprinsessans födelsedag': kronprinsessans_fodelsedag(year),
	              'Drottningens namnsdag': drottningens_namnsdag(year),
	              'Riksdagsval': riksdagsval(year),
	              'FN-dagen': fn_dagen(year),
	              'Gustaf Adofsdagen': gustaf_adolfsdagen(year),
	              'Nobeldagen': nobeldagen(year),
	              'Drottningens födelsedag': drottningens_fodelsedag(year),
	              'Juldagen': juldagen(year)
	              }
	return flaggdagar


def helgdagar(year):
	helgdagar = {'Nyårsdagen': nyarsdagen(year),
	             'Trettondedag jul': trettondedag_jul(year),
	             'Långfredagen': langfredagen(year),
	             'Påskdagen': paskdagen(year),
	             'Annandag påsk': annandag_pask(year),
	             'Första maj': forsta_maj(year),
	             'Kristi himmelsfärdsdag': kristi_himmelsfardsdag(year),
	             'Pingstdagen': pingstdagen(year),
	             'Sveriges nationaldag': sveriges_nationaldag(year),
	             'Midsommardagen': midsommardagen(year),
	             'Alla helgons dag': alla_helgons_dag(year),
	             'Juldagen': juldagen(year),
	             'Annandag jul': annandag_jul(year)
	             }
	return helgdagar


def svarta_dagar(year):
	svarta_dagar = {'Vårdagjämningen': vardagjamningen(year),
	                'Sommarsolståndet': sommarsolstandet(year),
	                'Höstdagjämningen': hostdagjamningen(year),
	                'Vintersolståndet': vintersolstandet(year),
	                'Fettisdagen': fettisdagen(year),
	                'Annandag pingst': annandag_pingst(year),
	                'Mårtensafton': martensafton(year),
	                'Värnlösa barns dag': varnlosa_barns_dag(year),
	                'Luciadagen': luciadagen(year),
	                'Tjugondedag jul': tjugondedag_jul(year),
	                'Trettondagsafton': trettondagsafton(year),
	                'Skärtorsdag': skartorsdagen(year),
	                'Påskafton': paskafton(year),
	                'Valborgsmässoafton': valborgsmassoafton(year),
	                'Pingstafton': pingstafton(year),
	                'Midsommarafton': midsommarafton(year),
	                'Julafton': julafton(year),
	                'Nyårsafton': nyarsafton(year),
	                'Alla hjärtans dag': alla_hjartans_dag(year),
	                'Gustaf Adolfsdagen': gustaf_adolfsdagen(year),
	                'Nobeldagen': nobeldagen(year),
	                'Våffeldagen': vaffeldagen(year),
	                'Sommartid börjar': sommartid_borjar(year),
	                'Allmän självdeklaration': allman_sjalvdeklaration(year),
	                'Sommartid slutar': sommartid_slutar(year),
	                'Konungens namnsdag': konungens_namnsdag(year),
	                'Internationella kvinnodagen': internationella_kvinnodagen(year),
	                'Kronprinsessans namnsdag': kronprinsessans_namnsdag(year),
	                'Konungens födelsedag': konungens_fodelsedag(year),
	                'Mors dag': mors_dag(year),
	                'Kronprinsessans födelsedag': kronprinsessans_fodelsedag(year),
	                'Drottningens namnsdag': drottningens_namnsdag(year),
	                'Kanelbullens dag': kanelbullens_dag(year),
	                'Internationella barndagen': internationella_barndagen(year),
	                'FN-dagen': fn_dagen(year),
	                'Fars dag': fars_dag(year),
	                'Drottningens födelsedag': drottningens_fodelsedag(year)
	                }
	return svarta_dagar


# =================================
def gauss_easter_algorithm(year):
	a = year % 19
	b = year % 4
	c = year % 7

	k = year // 100
	p = (13 + 8 * k) // 25
	q = k // 4
	# k = math.floor(year / 100)
	# p = math.floor((13 + 8 * k) / 25)
	# q = math.floor(k / 4)
	m = (15 - p + k - q) % 30
	n = (4 + k - q) % 7

	d = (19 * a + m) % 30
	e = (2 * b + 4 * c + 6 * d + n) % 7

	# Gregorian Easter is 22 + d + e March or d + e − 9 April
	# if d = 29 and e = 6, replace 26 April with 19 April
	# if d = 28, e = 6, and (11m + 11) mod 30 < 19, replace 25 April with 18 April

	day = 22 + d + e
	month = 3
	if day > 31:
		day = d + e - 9
		month = 4
	if d == 29 and e == 6 and day == 26 and month == 4:
		day = 19
	if d == 28 and e == 6 and (11 * m + 11) % 30 < 19 and day == 25 and month == 4:
		day = 18
	return year, month, day


def ian_taylor_easter_jscr(year):  # From Wikipedia
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


def easter(year):
	return ian_taylor_easter_jscr(year)
# =================================


# =========== RELIGIOUS ===========
# Trettondagsafton
def trettondagsafton(year):
	day = 5
	month = 1
	return datetime.date(year, month, day)


# Trettondedag jul
def trettondedag_jul(year):
	day = 6
	month = 1
	return datetime.date(year, month, day)


# Påskdagen
def paskdagen(year):
	return easter(year)


# Annandag påsk
def annandag_pask(year):
	return easter(year) + datetime.timedelta(days=1)


# Påskafton
def paskafton(year):
	return easter(year) + datetime.timedelta(days=-1)


# Långfredagen
def langfredagen(year):
	return easter(year) + datetime.timedelta(days=-2)


# Skärtorsdagen
def skartorsdagen(year):
	return easter(year) + datetime.timedelta(days=-3)


# Fettisdagen
def fettisdagen(year):
	return easter(year) + datetime.timedelta(days=-47)  # Tuesday 40 days before easter


# Kristi himmelsfärdsdag
def kristi_himmelsfardsdag(year):
	return easter(year) + datetime.timedelta(days=39)  # 6th Thursday after easter (5*7+4=39 days)


# Pingstafton
def pingstafton(year):
	return easter(year) + datetime.timedelta(days=48)


# Pingstdagen
def pingstdagen(year):
	return easter(year) + datetime.timedelta(days=49)  # 7th Sunday after easter (7*7=49 days)


# Annandag pingst
def annandag_pingst(year):
	return easter(year) + datetime.timedelta(days=50)


# Alla helgons dag
def alla_helgons_dag(year):
	day = 31
	month = 10
	date = datetime.date(year, month, day)
	date = date + datetime.timedelta((weekdays['saturday'] - date.isoweekday()) % 7)  # 1st Saturday after 'October 31'
	return date


# Julafton
def julafton(year):
	day = 24
	month = 12
	return datetime.date(year, month, day)


# Juldagen
def juldagen(year):
	day = 25
	month = 12
	return datetime.date(year, month, day)


# Annandag jul
def annandag_jul(year):
	day = 26
	month = 12
	return datetime.date(year, month, day)


# Värnlösa barns dag
def varnlosa_barns_dag(year):
	day = 28
	month = 12
	return datetime.date(year, month, day)
# =================================


# =========== CULTURAL ============
# Nyårsdagen
def nyarsdagen(year):
	day = 1
	month = 1
	return datetime.date(year, month, day)


# Tjugondedag jul
def tjugondedag_jul(year):
	day = 13
	month = 1
	return datetime.date(year, month, day)


# Konungens namnsdag
def konungens_namnsdag(year):
	day = 28
	month = 1
	return datetime.date(year, month, day)


# Alla hjärtans dag
def alla_hjartans_dag(year):
	day = 14
	month = 2
	return datetime.date(year, month, day)


# Våffeldagen
def vaffeldagen(year):
	day = 25
	month = 3
	return datetime.date(year, month, day)


# Internationella kvinnodagen
def internationella_kvinnodagen(year):
	day = 8
	month = 3
	return datetime.date(year, month, day)


# KronprinsessansNamnsdag
def kronprinsessans_namnsdag(year):
	day = 8
	month = 3
	return datetime.date(year, month, day)


# Konungens födelsedag
def konungens_fodelsedag(year):
	day = 30
	month = 3
	return datetime.date(year, month, day)


# Sommartid börjar
def sommartid_borjar(year):
	day = 31
	month = 3
	date = datetime.date(year, month, day)
	date = date - datetime.timedelta(((date.isoweekday() - weekdays['sunday'] - 1) % 7) + 1)  # Last Sunday of March
	return date


# Valborgsmässoafton
def valborgsmassoafton(year):
	day = 30
	month = 4
	return datetime.date(year, month, day)


# Första maj
def forsta_maj(year):
	day = 1
	month = 5
	return datetime.date(year, month, day)


# Allmän självdeklaration
def allman_sjalvdeklaration(year):
	day = 1
	month = 5
	date = datetime.date(year, month, day)
	date_found = False
	while not date_found:
		date = date + datetime.timedelta(1)
		if weekdays['monday'] <= date.isoweekday() <= weekdays['friday'] and not kristi_himmelsfardsdag(
				date.year) == date:  # 1st weekday of May not being a holiday
			date_found = True
	return date


# Mors dag
def mors_dag(year):
	day = 31
	month = 5
	date = datetime.date(year, month, day)
	date = date - datetime.timedelta(((date.isoweekday() - weekdays['sunday'] - 1) % 7) + 1)  # Last Sunday of May
	return date


# Sveriges nationaldag
def sveriges_nationaldag(year):
	day = 6
	month = 6
	return datetime.date(year, month, day)


# Midsommarafton
def midsommarafton(year):
	day = 20
	month = 6
	date = datetime.date(year, month, day)
	date = date + datetime.timedelta((weekdays['saturday'] + 7 - date.isoweekday()) % 7)  # 1st Saturday after 'June 20'
	return date


# Midsommardagen
def midsommardagen(year):
	day = 20
	month = 6
	date = datetime.date(year, month, day)
	date = date + datetime.timedelta((weekdays['sunday'] + 7 - date.isoweekday()) % 7)  # 1st Sunday after 'June 20'
	return date


# Kronprinsessans födelsedag
def kronprinsessans_fodelsedag(year):
	day = 14
	month = 7
	return datetime.date(year, month, day)


# Drottningens namnsdag
def drottningens_namnsdag(year):
	day = 8
	month = 8
	return datetime.date(year, month, day)


# Riksdagsval
def riksdagsval(year):
	day = 1
	month = 9
	date = datetime.date(year, month, day)
	date = date + datetime.timedelta(
		((weekdays['saturday'] + 7 - date.isoweekday()) % 7) + 7)  # 2nd Saturday of September
	if (year - 2000) % 4 == 0:
		return date
	else:
		return None


# Kanelbullens dag
def kanelbullens_dag(year):
	day = 4
	month = 10
	return datetime.date(year, month, day)


# Internationella barndagen
def internationella_barndagen(year):
	day = 5
	month = 10
	return datetime.date(year, month, day)


# FN-dagen
def fn_dagen(year):
	day = 24
	month = 10
	return datetime.date(year, month, day)


# Sommartid slutar
def sommartid_slutar(year):
	day = 31
	month = 10
	date = datetime.date(year, month, day)
	date = date - datetime.timedelta(((date.isoweekday() - weekdays['sunday'] - 1) % 7) + 1)  # Last Sunday of October
	return date


# Gustaf Adolfsdagen
def gustaf_adolfsdagen(year):
	day = 6
	month = 11
	return datetime.date(year, month, day)


# Mårtensafton
def martensafton(year):
	day = 10
	month = 11
	return datetime.date(year, month, day)


# Fars dag
def fars_dag(year):
	day = 1
	month = 11
	date = datetime.date(year, month, day)
	date = date + datetime.timedelta(
		((weekdays['saturday'] + 7 - date.isoweekday()) % 7) + 7)  # 2nd Saturday of November
	return date


# Nobeldagen
def nobeldagen(year):
	day = 10
	month = 12
	return datetime.date(year, month, day)


# Luciadagen
def luciadagen(year):
	day = 13
	month = 12
	return datetime.date(year, month, day)


# Drottningens födelsedag
def drottningens_fodelsedag(year):
	day = 23
	month = 12
	return datetime.date(year, month, day)


# Nyårsafton
def nyarsafton(year):
	day = 31
	month = 12
	return datetime.date(year, month, day)
# =================================


# ========= ASTRONOMICAL ==========
# Vårdagjämning
def vardagjamningen(year):
	spring_equinox = {2010: datetime.date(2010, 3, 20),
	                  2011: datetime.date(2011, 3, 20),
	                  2012: datetime.date(2012, 3, 20),
	                  2013: datetime.date(2013, 3, 20),
	                  2014: datetime.date(2014, 3, 20),
	                  2015: datetime.date(2015, 3, 20),
	                  2016: datetime.date(2016, 3, 20),
	                  2017: datetime.date(2017, 3, 20),
	                  2018: datetime.date(2018, 3, 20),
	                  2019: datetime.date(2019, 3, 20),
	                  2020: datetime.date(2020, 3, 20)}
	return spring_equinox[year]


# Sommarsolståndet
def sommarsolstandet(year):
	summer_solstice = {2010: datetime.date(2010, 6, 21),
	                   2011: datetime.date(2011, 6, 21),
	                   2012: datetime.date(2012, 6, 20),
	                   2013: datetime.date(2013, 6, 21),
	                   2014: datetime.date(2014, 6, 21),
	                   2015: datetime.date(2015, 6, 21),
	                   2016: datetime.date(2016, 6, 20),
	                   2017: datetime.date(2017, 6, 21),
	                   2018: datetime.date(2018, 6, 21),
	                   2019: datetime.date(2019, 6, 21),
	                   2020: datetime.date(2020, 6, 20)}
	return summer_solstice[year]


# Höstdagjämning
def hostdagjamningen(year):
	fall_equinox = {2010: datetime.date(2010, 9, 23),
	                2011: datetime.date(2011, 9, 23),
	                2012: datetime.date(2012, 9, 22),
	                2013: datetime.date(2013, 9, 22),
	                2014: datetime.date(2014, 9, 23),
	                2015: datetime.date(2015, 9, 23),
	                2016: datetime.date(2016, 9, 22),
	                2017: datetime.date(2017, 9, 22),
	                2018: datetime.date(2018, 9, 23),
	                2019: datetime.date(2019, 9, 23),
	                2020: datetime.date(2020, 9, 22)}
	return fall_equinox[year]


# Vintersolståndet
def vintersolstandet(year):
	winter_solstice = {2010: datetime.date(2010, 12, 21),
	                   2011: datetime.date(2011, 12, 22),
	                   2012: datetime.date(2012, 12, 21),
	                   2013: datetime.date(2013, 12, 21),
	                   2014: datetime.date(2014, 12, 21),
	                   2015: datetime.date(2015, 12, 22),
	                   2016: datetime.date(2016, 12, 21),
	                   2017: datetime.date(2017, 12, 21),
	                   2018: datetime.date(2018, 12, 21),
	                   2019: datetime.date(2019, 12, 22),
	                   2020: datetime.date(2020, 12, 21)}
	return winter_solstice[year]

# =================================

# Author: Eric Oropezaelwood
#
"""
Given a year, return the century it is in. The first century spans from year 1 up
to and including year 100. The second is from the year 101 up to and including year 200.
"""

def centuryFromYear(year):
    year = year/100
    if year == int(year):
        return year
    else:
        return int(year) + 1

# A terminal program to view deadlines. http://navid.io/dead
import argparse
import csv
from datetime import datetime
from operator import itemgetter
from prettytable import PrettyTable

# TODO
# Hours and minutes flag

# Argument handling
parser = argparse.ArgumentParser()
parser.add_argument("deadlines", help="File containing deadline data")
args = parser.parse_args()

# Get file
f = open(args.deadlines, 'r')
csv.register_dialect('skipspaces', skipinitialspace=True)
reader = csv.reader(f, dialect='skipspaces')

# Read in deadlines, format their dates, calculate time remaining
deadlines = []
timeNow = datetime.now()
for deadline in reader:
	# Get datetime object from date string
	deadline[1] = datetime.strptime(deadline[1], "%d/%m/%y %H:%M")
	# Calculate time reamining and inject 
	timeRemaining = deadline[1] - timeNow
	deadline.insert(2, timeRemaining)
	deadlines.append(deadline)
f.close()

# Sort deadlines
deadlines.sort(key=itemgetter(1))

# Create table
table = PrettyTable(["Module", "Due date", "Time remaining", "Description"])
for deadline in deadlines:
	# Format the time remaining
	weeks = deadline[2].days // 7
	days = deadline[2].days % 7
	weekText = " week, " if weeks == 1 else " weeks, "
	deadline[2] = str(weeks) + weekText + str(days) + " days"
	table.add_row(deadline)

print table

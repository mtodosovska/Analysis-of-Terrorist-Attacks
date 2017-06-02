from numpy import *
import matplotlib.pyplot as plt
from csv import DictReader

data = reader = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

events = {}
i = 0
for row in data:
    if i == 0:
        i+=1
    else:
        eventId = row["eventid"]
        year = int(row["iyear"])
        if year in events.keys():
            events[year].append(eventId)
        else:
            events[year] = []
            events[year].append(eventId)

number = []

for year in events.keys():
    print(year, len(events[year]))
    number.append(len(events[year]))

fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(events)), number, width=width)
ax.set_xticks(arange(len(events)) + width/2)
ax.set_xticklabels(events, rotation=90, fontsize=6)
ax.set_title("Number of attacks per year")


plt.show()


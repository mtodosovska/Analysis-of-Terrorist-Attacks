from numpy import *
import matplotlib.pyplot as plt
from csv import DictReader
# -*- Visualise and show a trend about the location of the attacks carried out by ISIS. -*-

data = reader = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

attacks = {}
for row in data:
    if row["gname"] == "Islamic State of Iraq (ISI)":
        eventId = row["eventid"]
        target = row["country_txt"]
        if target in attacks.keys():
            attacks[target].append(eventId)
        else:
            attacks[target] = []
            attacks[target].append(eventId)

number = []

for target in attacks.keys():
    print(target, len(attacks[target]))
    number.append(len(attacks[target]))

fig = plt.figure()
ax = plt.subplot(111)
ax.bar(range(len(attacks)), number, width=0.55)
ax.set_xticks(arange(len(attacks)))
ax.set_xticklabels(attacks)
ax.set_title("Countries attacked by ISI")


plt.show()
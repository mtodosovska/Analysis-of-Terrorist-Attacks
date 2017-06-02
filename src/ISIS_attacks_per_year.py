from numpy import *
import matplotlib.pyplot as plt
from csv import DictReader

data = reader = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

attacks = {}
for row in data:
    if row["gname"] == "Islamic State of Iraq and the Levant (ISIL)":
        eventId = row["eventid"]
        year = int(row["iyear"])
        if year in attacks.keys():
            attacks[year].append(eventId)
        else:
            attacks[year] = []
            attacks[year].append(eventId)

number = []

for year in attacks.keys():
    print(year, len(attacks[year]))
    number.append(len(attacks[year]))

fig = plt.figure()
ax = plt.subplot(111)
ax.bar(range(len(attacks)), number, width=0.55)
ax.set_xticks(arange(len(attacks)))
ax.set_xticklabels(attacks)
ax.set_title("Number of attacks by ISIL per year")


plt.show()
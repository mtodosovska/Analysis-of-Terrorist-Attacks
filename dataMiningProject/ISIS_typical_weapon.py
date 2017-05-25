from numpy import *
import matplotlib.pyplot as plt
from csv import DictReader
# -*- Visualise and show a trend about the the typical weapon used by ISIS. -*-

data = reader = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

attacks = {}
for row in data:
    if row["gname"] == "Islamic State of Iraq and the Levant (ISIL)":
        eventId = row["eventid"]
        weapon = row["weaptype1_txt"]
        if weapon in attacks.keys():
            attacks[weapon].append(eventId)
        else:
            attacks[weapon] = []
            attacks[weapon].append(eventId)

number = []

for weapon in attacks.keys():
    print(weapon, len(attacks[weapon]))
    number.append(len(attacks[weapon]))

fig = plt.figure()
ax = plt.subplot(111)
ax.bar(range(len(attacks)), number, width=0.55)
ax.set_xticks(arange(len(attacks)))
ax.set_xticklabels(attacks, rotation=55)
ax.set_title("Weapons used by ISIL")


plt.show()
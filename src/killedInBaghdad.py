import numpy as np
from csv import DictReader

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

citizensBaghdad = 7665000
citizensKarachi = 9339023
citizensLima = 8894412
citizensBelfast = 672522
citizensSantiago = 7000000

partsOfDay = 96
attacksPerDayBaghdad = {}
killedPerDayBaghdad = {}
attacksPerDayKarachi = {}
killedPerDayKarachi = {}
attacksPerDayLima = {}
killedPerDayLima = {}
attacksPerDayBelfast = {}
killedPerDayBelfast = {}
attacksPerDaySantiago = {}
killedPerDaySantiago = {}

i = 0
for row in data:
    if i == 0:
        i += 1
    else:
        city = row["city"]
        day = row["iday"]
        month = row["imonth"]
        year = row["iyear"]
        killed = row["nkill"]

        if city == "Baghdad":
            if day != 0 and month != 0 and killed != "-9":
                key = day + month + year
                if key in attacksPerDayBaghdad:
                    attacksPerDayBaghdad[key] += 1
                    killedPerDayBaghdad[key] += float(killed)
                else:
                    attacksPerDayBaghdad[key] = 1
                    killedPerDayBaghdad[key] = float(killed)

        if city == "Karachi":
            if day != 0 and month != 0 and killed != "-9":
                key = day + month + year
                if key in attacksPerDayKarachi:
                    attacksPerDayKarachi[key] += 1
                    killedPerDayKarachi[key] += float(killed)
                else:
                    attacksPerDayKarachi[key] = 1
                    killedPerDayKarachi[key] = float(killed)

        if city == "Lima":
            if day != 0 and month != 0 and killed != "-9":
                key = day + month + year
                if key in attacksPerDayLima:
                    attacksPerDayLima[key] += 1
                    killedPerDayLima[key] += float(killed)
                else:
                    attacksPerDayLima[key] = 1
                    killedPerDayLima[key] = float(killed)

        if city == "Belfast":
            if day != 0 and month != 0 and killed != "-9":
                key = day + month + year
                if key in attacksPerDayBelfast:
                    attacksPerDayBelfast[key] += 1
                    killedPerDayBelfast[key] += float(killed)
                else:
                    attacksPerDayBelfast[key] = 1
                    killedPerDayBelfast[key] = float(killed)

        if city == "Santiago":
            if day != 0 and month != 0 and killed != "-9":
                key = day + month + year
                if key in attacksPerDaySantiago:
                    attacksPerDaySantiago[key] += 1
                    killedPerDaySantiago[key] += float(killed)
                else:
                    attacksPerDaySantiago[key] = 1
                    killedPerDaySantiago[key] = float(killed)

averageBaghdad = np.mean(list(attacksPerDayBaghdad.values()))
avgKilledBaghdad = np.mean(list(killedPerDayBaghdad.values()))
p_attackedBaghdad = averageBaghdad / partsOfDay
p_killedBaghdad = avgKilledBaghdad / citizensBaghdad
print("Chances of being attacked in Baghdad:", p_attackedBaghdad)
print("Chances of being killed in an attack in Baghdad:", p_killedBaghdad)

averageKarachi = np.mean(list(attacksPerDayKarachi.values()))
avgKilledKarachi = np.mean(list(killedPerDayKarachi.values()))
p_attackedKarachi = averageKarachi / partsOfDay
p_killedKarachi = avgKilledKarachi / citizensKarachi
print("Chances of being attacked in Karachi:", p_attackedKarachi)
print("Chances of being killed in an attack in Karachi:", p_killedKarachi)

averageLima = np.mean(list(attacksPerDayLima.values()))
avgKilledLima = np.mean(list(killedPerDayLima.values()))
p_attackedLima = averageLima / partsOfDay
p_killedLima = avgKilledLima / citizensLima
print("Chances of being attacked in Lima:", p_attackedLima)
print("Chances of being killed in an attack in Lima:", p_killedLima)

averageBelfast = np.mean(list(attacksPerDayBelfast.values()))
avgKilledBelfast = np.mean(list(killedPerDayBelfast.values()))
p_attackedBelfast = averageBelfast / partsOfDay
p_killedBelfast = avgKilledBelfast / citizensBelfast
print("Chances of being attacked in Belfast:", p_attackedBelfast)
print("Chances of being killed in an attack in Belfast:", p_killedBelfast)

averageSantiago = np.mean(list(attacksPerDaySantiago.values()))
avgKilledSantiago = np.mean(list(killedPerDaySantiago.values()))
p_attackedSantiago = averageSantiago / partsOfDay
p_killedSantiago = avgKilledSantiago / citizensSantiago
print("Chances of being attacked in Santiago:", p_attackedSantiago)
print("Chances of being killed in an attack in Santiago:", p_killedSantiago)
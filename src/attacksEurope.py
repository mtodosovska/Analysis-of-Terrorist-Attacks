from csv import DictReader

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

attacksE = {}
killingsE = {}
attacksW = {}
killingsW = {}
inE = {}
inW = {}

i = 0

for row in data:
    if i == 0:
        i+=1
    else:
        year = row["iyear"]
        region = row["region_txt"]
        killings = float(row["nkill"])
        wounded = float(row["nwound"])

        if region == "Western Europe":

            if year not in inW:
                inW[year] = 0
            if year not in attacksW:
                attacksW[year] = 0
            if year not in killingsW:
                killingsW[year] = 0

            if year in attacksW:
                attacksW[year] += 1

            if killings != -9:
                if year in killingsW:
                    killingsW[year] += killings

                if year in inW:
                    inW[year] += killings

            if wounded != -9:
                if year in inW:
                    inW[year] += wounded

        if region == "Eastern Europe":

            if year not in inE:
                inE[year] = 0
            if year not in attacksE:
                attacksE[year] = 0
            if year not in killingsE:
                killingsE[year] = 0

            if year in attacksE:
                attacksE[year] += 1

            if year not in inE:
                inE[year] = 0

            if killings != -9:
                if year in killingsE:
                    killingsE[year] += killings

                if year in inE:
                    inE[year] += killings

            if wounded != -9:
                if year in inE:
                    inE[year] += wounded

population = 743100000
populationW = 397500000
populationE = population - populationW
deathRateW = 10.2
deathRateE = 10
deathYearW = (populationW/1000)*deathRateW
deathYearE = (populationE/1000)*deathRateE

pAttackedE = {}
pAttackedW = {}
pDieInAttackE = {}
pDieInAttackW = {}
pDieE = {}
pDieW = {}


for year in inE.keys():
    pAttackedE[year] = inE[year]/populationE

for year in inW.keys():
    pAttackedW[year] = inW[year]/populationW

for year in inE.keys():
    pDieInAttackE[year] = killingsE[year]/deathYearE

for year in inW.keys():
    pDieInAttackW[year] = killingsW[year] / deathYearW

for year in inE.keys():
    pDieE[year] = deathYearE/populationE

for year in inW.keys():
    pDieW[year] = deathYearW/populationW

pKilledAttackW = {}
pKilledAttackE = {}

for year in inW.keys():
    if pAttackedW[year] == 0:
        pKilledAttackW[year] = 0
    else:
        pKilledAttackW[year] = (pDieInAttackW[year] * pDieW[year])/pAttackedW[year]

for year in inE.keys():
    if pAttackedE[year] == 0:
        pKilledAttackE[year] = 0
    else:
        pKilledAttackE[year] = (pDieInAttackE[year] * pDieE[year])/pAttackedE[year]
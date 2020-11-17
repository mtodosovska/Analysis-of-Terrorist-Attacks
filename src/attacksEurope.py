from csv import DictReader

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

attacksE = {}
killingsE = {}
attacksW = {}
killingsW = {}
inE = {}
inW = {}

i = 0

def get_for_east_west(year, inWE, attacks, killingsWE, killings, wounded):
    if year not in inWE:
        inWE[year] = 0
    if year not in attacks:
        attacks[year] = 0
    if year not in killingsWE:
        killingsWE[year] = 0

    if year in attacks:
        attacks[year] += 1

    if killings != -9:
        if year in killingsWE:
            killingsWE[year] += killings

        if year in inWE:
            inWE[year] += killings

    if wounded != -9:
        if year in inWE:
            inWE[year] += wounded

    return attacks, killings


for row in data:
    if i == 0:
        i+=1
    else:
        year = row["iyear"]
        region = row["region_txt"]
        killings = float(row["nkill"])
        wounded = float(row["nwound"])

        if region == "Western Europe":
            attacksW, killingsW = get_for_east_west(year, inW, attacksW, killingsW, killings, wounded)

        if region == "Eastern Europe":
            attacksE, killingsE = get_for_east_west(year, inE, attacksE, killingsE, killings, wounded)

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


def get_percent(dict, population, res_dict):
    for year in dict.keys():
        res_dict[year] = dict[year]/population
        return res_dict


pAttackedE = get_percent(inE, populationE, pAttackedE)
pAttackedW = get_percent(inW, populationW, pAttackedW)
pDieInAttackE = get_percent(killingsE, deathYearE, pDieInAttackE)
pDieInAttackW = get_percent(killingsW, deathYearW, pDieInAttackW)
pDieE = get_percent(deathYearE, populationE, pDieE)
pDieW = get_percent(deathYearW, populationW, pDieW)


def get_percent_attacked(inWE, pAttacked, pKilledAttack, pDieInAttack, pDie):

    for year in inWE.keys():
        if pAttacked[year] == 0:
            pKilledAttack[year] = 0
        else:
            pKilledAttack[year] = (pDieInAttack[year] * pDie[year])/pAttacked[year]
    return pKilledAttack


pKilledAttackW = {}
pKilledAttackE = {}

pKilledAttackW = get_percent_attacked(inW, pAttackedW, pKilledAttackW, pDieInAttackW, pDieW)
pKilledAttackE = get_percent_attacked(inE, pAttackedE, pKilledAttackE, pDieInAttackE, pDieE)

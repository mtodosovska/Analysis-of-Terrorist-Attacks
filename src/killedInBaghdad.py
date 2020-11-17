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

attacks = {
    'Baghdad': attacksPerDayBaghdad,
    'Karachi': attacksPerDayKarachi,
    'Lima': attacksPerDayLima,
    'Belfast': attacksPerDayBelfast,
    'Santiago': attacksPerDaySantiago
}

killed = {
    'Baghdad': killedPerDayBaghdad,
    'Karachi': killedPerDayKarachi,
    'Lima': killedPerDayLima,
    'Belfast': killedPerDayBelfast,
    'Santiago': killedPerDaySantiago
}

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

        if day != 0 and month != 0 and killed != "-9":
            key = day + month + year
            if key in  attacks[city]:
                attacks[city][key] += 1
                killed[city][key] += float(killed)
            else:
                attacks[city][key] = 1
                killed[city][key] = float(killed)

average_attacks = {}
average_killed = {}
p_attacked = {}
p_killed = {}
for city in attacks.keys():
    average_attacks[city] = np.mean(list(attacks[city].values()))
    average_killed[city] = np.mean(list(killed[city].values()))

    p_attacked[city] = average_attacks[city] / partsOfDay
    p_killed[city] = average_killed[city] / citizensBaghdad
    print("Chances of being attacked in Baghdad:", p_attacked[city])
    print("Chances of being killed in an attack in Baghdad:", p_killed[city])

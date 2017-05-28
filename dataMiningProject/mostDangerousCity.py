from numpy import *
import operator
import matplotlib.pyplot as plt
from csv import DictReader

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

cityKilled = {}
countryKilled = {}
regionKilled = {}
professionKilled = {}
weaponKilled = {}
attackKilled = {}
groupKilled = {}

cityAttacks = {}
countryAttacks = {}
regionAttacks = {}
professionAttacks = {}
weaponAttacks = {}
attackAttacks = {}
groupAttacks = {}
ny = 0
lima = 0
belfast = 0
santiago = 0
unknownLima = 0
unbelfast = 0
unsantiago = 0
deadliest = []
i = 0
for row in data:
    if i == 0:
        i += 1
    else:
        idd = row["eventid"]
        killed = row["nkill"]
        city = row["city"]
        country = row["country_txt"]
        region = row["region_txt"]
        profession = row["targtype1_txt"]
        weapon = row["weaptype1_txt"]
        attack = row["attacktype1_txt"]
        group = row["gname"]
        if city == "New York City":
            ny += 1
        if city == "Lima":
            if float(killed) == -9:
                unknownLima += 1
            else:
                lima += float(killed)
        deadliest.append(float(killed))
        if city == "Belfast":
            if float(killed) == -9:
                unbelfast += 1
            else:
                belfast += float(killed)
        if city == "Santiago":
            if float(killed) == -9:
                unsantiago += 1
            else:
                santiago += float(killed)


        if killed == "-9":
            if city in cityAttacks.keys():
                cityAttacks[city] += 1
            else:
                cityAttacks[city] = 1
            if country in countryAttacks.keys():
                countryAttacks[country] += 1
            else:
                countryAttacks[country] = 1
            if region in regionAttacks.keys():
                regionAttacks[region] += 1
            else:
                regionAttacks[region] = 1
            if profession in professionAttacks.keys():
                professionAttacks[profession] += 1
            else:
                professionAttacks[profession] = 1

            if weapon in weaponAttacks.keys():
                weaponAttacks[weapon] += 1
            else:
                weaponAttacks[weapon] = 1

            if attack in attackAttacks.keys():
                attackAttacks[attack] += 1
            else:
                attackAttacks[attack] = 1

            if group in groupAttacks.keys():
                groupAttacks[group] += 1
            else:
                groupAttacks[group] = 1

        else:
            if city in cityAttacks.keys():
                cityAttacks[city] += 1
            else:
                cityAttacks[city] = 1

            if city in cityKilled.keys():
                cityKilled[city] += float(killed)
            else:
                cityKilled[city] = float(killed)

            if country in countryAttacks.keys():
                countryAttacks[country] += 1
            else:
                countryAttacks[country] = 1

            if country in countryKilled.keys():
                countryKilled[country] += float(killed)
            else:
                countryKilled[country] = float(killed)

            if region in regionAttacks.keys():
                regionAttacks[region] += 1
            else:
                regionAttacks[region] = 1

            if region in regionKilled.keys():
                regionKilled[region] += float(killed)
            else:
                regionKilled[region] = float(killed)

            if profession in professionAttacks.keys():
                professionAttacks[profession] += 1
            else:
                professionAttacks[profession] = 1

            if profession in professionKilled.keys():
                professionKilled[profession] += float(killed)
            else:
                professionKilled[profession] = float(killed)

            if weapon in weaponAttacks.keys():
                weaponAttacks[weapon] += 1
            else:
                weaponAttacks[weapon] = 1

            if weapon in weaponKilled.keys():
                weaponKilled[weapon] += float(killed)
            else:
                weaponKilled[weapon] = float(killed)

            if attack in attackAttacks.keys():
                attackAttacks[attack] += 1
            else:
                attackAttacks[attack] = 1

            if attack in attackKilled.keys():
                attackKilled[attack] += float(killed)
            else:
                attackKilled[attack] = float(killed)

            if group in groupAttacks.keys():
                groupAttacks[group] += 1
            else:
                groupAttacks[group] = 1

            if group in groupKilled.keys():
                groupKilled[group] += float(killed)
            else:
                groupKilled[group] = float(killed)


sorted_cityKilled = array(sorted(cityKilled.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_cityAttacked = array(sorted(cityAttacks.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_countryKilled = array(sorted(countryKilled.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_regionKilled = array(sorted(regionKilled.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_countryAttacked = array(sorted(countryAttacks.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_regionAttacked = array(sorted(regionAttacks.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_professionKilled = array(sorted(professionKilled.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_professionAttacked = array(sorted(professionAttacks.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_weaponKilled = array(sorted(weaponKilled.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_weaponAttacked = array(sorted(weaponAttacks.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_attackKilled = array(sorted(attackKilled.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_attackAttacked = array(sorted(attackAttacks.items(), key=operator.itemgetter(1))[::-1])[0:10]
sorted_groupKilled = array(sorted(groupKilled.items(), key=operator.itemgetter(1))[::-1])[0:20]
sorted_groupAttacked = array(sorted(groupAttacks.items(), key=operator.itemgetter(1))[::-1])[0:20]
sorted_deadliest = sorted(deadliest)[::-1]

ten = sorted_deadliest[0:10]
print(sorted_deadliest)
print(ten)
atWeap = []

data = reader = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))
i = 0
for row in data:
    if i == 0:
        i+= 1
    else:

        killed = float(row["nkill"])
        for one in ten:
            if killed == one:
                weap = row["weaptype1_txt"]
                atWeap.append(weap)

print(atWeap)
print("Number of attacks in New York:", ny)
print("Number of victims in Lima:", lima)
print("Number of attacks with unknown victims in Lima:", unknownLima)
print("Number of victims in Belfast:", belfast)
print("Number of attacks with unknown victims in Belfast:", unbelfast)
print("Number of victims in Santiago:", santiago)
print("Number of attacks with unknown victims in Santiago:", unsantiago)

print("City killed:", sorted_cityKilled)
print("City attacked:", sorted_cityAttacked)
print("Country killed:", sorted_countryKilled)
print("Country attacked:", sorted_countryAttacked)
print("Region killed:", sorted_regionKilled)
print("Region attacked:", sorted_regionAttacked)
print("Profession killed:", sorted_professionKilled)
print("Profession attacked:", sorted_professionAttacked)
print("Weapon killed:", sorted_weaponKilled)
print("Weapon attacked:", sorted_weaponAttacked)
print("Attack killed:", sorted_attackKilled)
print("Attack attacked:", sorted_attackAttacked)
print("Group killed:", sorted_groupKilled)
print("Group attacked:", sorted_groupAttacked)

sorted_cityKilled = array(sorted(cityKilled.items(), key=operator.itemgetter(1)))[0:10]
sorted_cityAttacked = array(sorted(cityAttacks.items(), key=operator.itemgetter(1)))[0:10]
sorted_countryKilled = array(sorted(countryKilled.items(), key=operator.itemgetter(1)))[0:10]
sorted_regionKilled = array(sorted(regionKilled.items(), key=operator.itemgetter(1)))[0:10]
sorted_countryAttacked = array(sorted(countryAttacks.items(), key=operator.itemgetter(1)))[0:10]
sorted_regionAttacked = array(sorted(regionAttacks.items(), key=operator.itemgetter(1)))[0:10]
print("City killed:", sorted_cityKilled)
print("City attacked:", sorted_cityAttacked)
print("Country killed:", sorted_countryKilled)
print("Country attacked:", sorted_countryAttacked)
print("Region killed:", sorted_regionKilled)
print("Region attacked:", sorted_regionAttacked)

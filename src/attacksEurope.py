import numpy as np
import operator
import matplotlib.pyplot as plt
from csv import DictReader
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error
from random import randint

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

'''
fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(attacksE)), attacksE.values(), width=width)
ax.set_xticks(np.arange(len(attacksE)) + width/2)
ax.set_xticklabels(attacksE, rotation=90, fontsize=6)
ax.set_title("Number of attacks per year -> Eastern Europe")


fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(attacksW)), attacksW.values(), width=width)
ax.set_xticks(np.arange(len(attacksW)) + width/2)
ax.set_xticklabels(attacksW, rotation=90, fontsize=6)
ax.set_title("Number of attacks per year -> Western Europe")


fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(killingsW)), killingsW.values(), width=width)
ax.set_xticks(np.arange(len(killingsW)) + width/2)
ax.set_xticklabels(killingsW, rotation=90, fontsize=6)
ax.set_title("Number of killings per year -> Western Europe")


fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(killingsE)), killingsE.values(), width=width)
ax.set_xticks(np.arange(len(killingsE)) + width/2)
ax.set_xticklabels(killingsE, rotation=90, fontsize=6)
ax.set_title("Number of killings per year -> Eastern Europe")

plt.show()

'''

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

'''
fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(pKilledAttackE)), pKilledAttackE.values(), width=width)
ax.set_xticks(np.arange(len(pKilledAttackE)) + width/2)
ax.set_xticklabels(pKilledAttackE, rotation=90, fontsize=6)
ax.set_title("Chances of being killed if you have been in an attack -> Eastern Europe")

fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(pKilledAttackW)), pKilledAttackW.values(), width=width)
ax.set_xticks(np.arange(len(pKilledAttackW)) + width/2)
ax.set_xticklabels(pKilledAttackW, rotation=90, fontsize=6)
ax.set_title("Chances of being killed if you have been in an attack -> Western Europe")

fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(pAttackedE)), pAttackedE.values(), width=width)
ax.set_xticks(np.arange(len(pAttackedE)) + width/2)
ax.set_xticklabels(pAttackedE, rotation=90, fontsize=6)
ax.set_title("Chances of being in an attack -> Eastern Europe")


fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(pAttackedW)), pAttackedW.values(), width=width)
ax.set_xticks(np.arange(len(pAttackedW)) + width/2)
ax.set_xticklabels(pAttackedW, rotation=90, fontsize=6)
ax.set_title("Chances of being in an attack -> Western Europe")

plt.show()
'''

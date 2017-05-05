from numpy import *
import matplotlib.pyplot as plt
from csv import DictReader
import scipy as scipy

data = reader = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

members = {}
attacks = {}
killings = {}

i = 0
for row in data:
    if i == 0:
        i += 1
    else:

        killed = row["nkill"]
        group = row["gname"]
        member = row["ingroup"]
        if killed == "-9":

            if group in attacks.keys():
                attacks[group] += 1
            else:
                attacks[group] = 1

            if group not in members.keys():
                members[group] = float(member)

            if group in killings.keys():
                killings[group] += 0
            else:
                killings[group] = 0

        else:

            if group in attacks.keys():
                attacks[group] += 1
            else:
                attacks[group] = 1

            if group in killings.keys():
                killings[group] += float(killed)
            else:
                killings[group] = float(killed)

            if group not in members.keys():
                members[group] = float(member)


cAttacks = []
cMembers = []
cKillings = []

for group in attacks.keys():

    cAttacks.append(attacks[group])
    cMembers.append(members[group])

for group in killings.keys():
    cKillings.append(killings[group])

atMem = corrcoef(cAttacks, cMembers)
atKil = corrcoef(cAttacks, cKillings)
kilMem = corrcoef(cKillings, cMembers)

print("The Pearson correlation coefficient between the number of attacks and the members of is:", atMem[0][1])
print("The Pearson correlation coefficient between the number of attacks and the killings of is:", atKil[0][1])
print("The Pearson correlation coefficient between the number of killings and the members of is:", kilMem[0][1])

plt.figure()
x = cAttacks    # višina je stolpec na indeksu 2
y = cMembers    # teža   je stolpec na indeksu 3
plt.plot(x, y, "k.")
plt.xlabel("Attacks")
plt.ylabel("Members")

plt.figure()
x = cAttacks    # višina je stolpec na indeksu 2
y = cKillings    # teža   je stolpec na indeksu 3
plt.plot(x, y, "k.")
plt.xlabel("Attacks")
plt.ylabel("Killings")

plt.figure()
x = cKillings    # višina je stolpec na indeksu 2
y = cMembers    # teža   je stolpec na indeksu 3
plt.plot(x, y, "k.")
plt.xlabel("Killings")
plt.ylabel("Members")

plt.show()
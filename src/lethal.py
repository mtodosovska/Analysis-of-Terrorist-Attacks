from numpy import *
import matplotlib.pyplot as plt
from csv import DictReader

data = reader = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))
lethal = 0
nonlethal = 0
unknown = 0
i = 0
for row in data:
    if i == 0:
        i+=1
    else:
        killed = row["nkill"]
        print(killed)
        if killed == "0":
            nonlethal += 1
        elif killed == "-9":
            unknown += 1
        else:
            lethal += 1


print("Number of lethal attacks:", lethal)
print("Number of nonlethal attacks:", nonlethal)
print("Number of attacks where the number of victims is unknown:", unknown)

fig = plt.figure()
ax = fig.add_subplot(111)
width = 0.5
#plt.hist([lethal, nonlethal, unknown], bins=[1, 2, 3])
xTickMarks = ["lethal", "nonlethal", "unknown"]
ind = arange(3)
ax.set_xticks(ind + width)
ax.bar(width, lethal)
ax.bar(3*width, nonlethal)
ax.bar(5*width, unknown)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=10)


plt.show()


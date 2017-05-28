import numpy as np
import operator
import matplotlib.pyplot as plt
from csv import DictReader

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

citizensBaghdad = 7665000

attacksPerDay = {}

i = 0
for row in data:
    if i == 0:
        i += 1
    else:
        city = row["city"]
        day = row["iday"]
        month = row["imonth"]
        year = row["iyear"]

        if city == "Baghdad":
            if day != 0 and month != 0:
                key = day + month + year
                if key in attacksPerDay:
                    attacksPerDay[key] += 1
                else:
                    attacksPerDay[key] = 1


average = np.mean(list(attacksPerDay.values()))
print(average)
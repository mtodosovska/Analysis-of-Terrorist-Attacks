import numpy as np
import operator
import matplotlib.pyplot as plt
from csv import DictReader
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error
from random import randint

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

attacks = {}
i = 0

for row in data:
    if i == 0:
        i+=1
    else:
        year = row["iyear"]
        month = row["imonth"]
        region = row["region_txt"]

        if "Europe" in region:
            if month + year not in attacks:
                attacks[month + year] = 0
            else:
                attacks[month + year] += 1


X_learning = []
Y_learning = []
X_testing = []
Y_check = []
d = 8
i = -1
for key in attacks:
    i += 1
    temp = []
    for j in range(0, d):
        temp.append(i ** j)
    X_learning.append(temp)
    tempi = []
    tempi.append(1)
    tempi.append(attacks[key])
    Y_learning.append(tempi)

for z in range(i+1, i+61):
    temp = []
    for j in range(0, d):
        temp.append(z ** j)
    X_testing.append(temp)


model = Lasso(alpha=1.5)
model.fit(X_learning, Y_learning)
Y_testing = model.predict(X_testing)

print(X_testing)

result = []
for row in Y_testing:
    result.append(row[1])


print(result)

result = []
i = 1
summ = 0
for row in Y_testing:
    if i == 12:
        i = 1
        summ += row[1]
        result.append(summ)
        summ = 0
    else:
        summ += row[1]
        i += 1

print(result)

fig = plt.figure()
ax = plt.subplot(111)
width = 0.55
ax.bar(range(len(result)), result, width=width)
ax.set_xticks(np.arange(len(result)) + width/2)
ax.set_xticklabels(result, rotation=90, fontsize=6)
ax.set_title("Prediction of the number of attacks in the next 5 years in Europe")


plt.show()
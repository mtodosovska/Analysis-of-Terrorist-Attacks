import numpy as np
import matplotlib.pyplot as plt
from csv import DictReader

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

numTalibans = {}
numISIS = {}
numAlQaida = {}
numBokoHaram = {}

i = 0

for row in data:
    if i == 0:
        i += 1
    else:
        group = row["gname"]
        year = row["iyear"]

        if group == "Taliban":
            if year in numTalibans.keys():
                numTalibans[year] += 1
            else:
                numTalibans[year] = 1

        if group == "Islamic State of Iraq and the Levant (ISIL)":
            if year in numISIS.keys():
                numISIS[year] += 1
            else:
                numISIS[year] = 1

        if group == "Boko Haram":
            if year in numBokoHaram.keys():
                numBokoHaram[year] += 1
            else:
                numBokoHaram[year] = 1

        if "Al-Qaida" in group:
            if year in numAlQaida.keys():
                numAlQaida[year] += 1
            else:
                numAlQaida[year] = 1


print("Taliban", numTalibans)
print("ISIS", numISIS)
print("Boko Haram", numBokoHaram)
print("Al-Qaida", numAlQaida)

def draw_graph(num, name_num):
    fig = plt.figure()
    ax = plt.subplot(111)
    width = 0.55
    ax.bar(range(len(num)), num.values(), width=width)
    ax.set_xticks(np.arange(len(num)) + width/2)
    ax.set_xticklabels(num, rotation=90, fontsize=6)
    ax.set_title(f"Number of attacks per year -> {name_num}")


draw_graph(numTalibans, 'Talibans')
draw_graph(numISIS, 'ISIS')
draw_graph(numBokoHaram, 'Boko Haram')
draw_graph(numAlQaida, 'Al-Qaida')


plt.show()


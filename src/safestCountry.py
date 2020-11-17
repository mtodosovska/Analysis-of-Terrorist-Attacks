from csv import DictReader
import matplotlib.pyplot as plt
import numpy as np

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

attacks15 = {}
killings15 = {}
in15 = {}


i = 0
for row in data:
    if i == 0:
        i += 1
    else:
        year = row["iyear"]
        region = row["region_txt"]
        if year == "2015" and "Europe" in region:

            country = row["country_txt"]
            killings = float(row["nkill"])
            wounded = float(row["nwound"])
            if country not in attacks15:
                attacks15[country] = 1
            else:
                attacks15[country] += 1

            if killings == -9:
                killings = 0
            if wounded == -9:
                wounded = 0

            if country not in killings15:
                killings15[country] = killings
            else:
                killings15[country] += killings

            if country not in in15:
                in15[country] = killings + wounded
            else:
                in15[country] += killings + wounded

population = DictReader(open("countries.csv", "rt", encoding="utf-8"))

people = {}

for row in population:
    country = row["Country (en)"]
    num = row["Population"]
    people[country] = num

print("Populations:", people)
deathRate = 10.2

danger = {}
dangerA = {}

for country in attacks15:
    cit = float(people[country])
    deathYear = ((cit)/1000)*deathRate
    p_die = deathYear/cit
    p_attacked = in15[country]/cit
    p_dieAtt = killings15[country]/deathYear
    if p_attacked == 0:
        p_dieInAttack = 0
    else:
        p_dieInAttack = (p_dieAtt*p_die)/p_attacked
    danger[country] = p_dieInAttack
    dangerA[country] = p_attacked

print(danger)
print(dangerA)


def draw_graph(danger, sentence):
    fig = plt.figure()
    ax = plt.subplot(111)
    width = 0.55
    ax.bar(range(len(danger)), danger.values(), width=width)
    ax.set_xticks(np.arange(len(danger)) + width/2)
    ax.set_xticklabels(danger, rotation=90, fontsize=6)
    ax.set_title(sentence)

draw_graph(dangerA, 'Chances of being in an attack -> Europe (2015)')
draw_graph(danger, 'Chances of being killed in an attack -> Europe (2015)')

plt.show()


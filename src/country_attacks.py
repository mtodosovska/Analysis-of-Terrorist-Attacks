from csv import DictReader

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))
country_attacks = dict()
for row in data:
    country = row["country_txt"]
    if country in country_attacks.keys():
        country_attacks[country] += 1
    else:
        country_attacks[country] = 1

for x in country_attacks.keys():
    print(x," ",country_attacks[x])


#for x in country_attacks.keys():
#    if country_attacks[x] >2000:
#        print(x," ",country_attacks[x])
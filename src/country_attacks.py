from csv import DictReader

data = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))
country_attacks = dict()
for row in data:
    country = row["country_txt"]
    if country in country_attacks.keys():
        country_attacks[country] += 1
    else:
        country_attacks[country] = 1

s = [(k, country_attacks[k]) for k in sorted(country_attacks, key=country_attacks.get)]
for k, v in s:
    print(k,v)
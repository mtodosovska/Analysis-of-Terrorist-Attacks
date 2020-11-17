from numpy import *
import operator
import matplotlib.pyplot as plt
from csv import DictReader

data = reader = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

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

dicts = {
    'city': [cityAttacks, cityKilled],
    'country_txt': [countryAttacks, countryKilled],
    'region_txt': [regionAttacks, regionKilled],
    'targtype1_txt': [professionAttacks, professionKilled],
    'weaptype1_txt': [weaponAttacks, weaponKilled],
    'attacktype1_txt': [attackAttacks, attackKilled],
    'gname': [groupAttacks, groupKilled]

}

i = 0

killed = 'nkill'
keywords = ['city', 'country_txt', 'region_txt', 'targtype1_txt', 'weaptype1_txt', 'attacktype1_txt', 'gname']

for row in data:
    if i == 0:
        i += 1
    else:
        for keyword in keywords:
            attacks = row[keyword]

            if killed != "-9":
                if attacks in dicts[keyword][1].keys():
                    dicts[keyword][1][attacks] += float(killed)
                else:
                    dicts[keyword][1] = float(killed)

            if attacks in dicts[keyword][0].keys():
                dicts[keyword][0][attacks] += 1
            else:
                dicts[keyword][0] = 1

            sorted_a = array(sorted(dicts[keyword][0].items(), key=operator.itemgetter(1))[::-1])[0:10]
            sorted_k = array(sorted(dicts[keyword][1].items(), key=operator.itemgetter(1))[::-1])[0:10]

            print(f'{keyword} killed:', sorted_k)
            print(f'{keyword} attacked:', sorted_a)

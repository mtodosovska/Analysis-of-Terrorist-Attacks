from numpy import *
import matplotlib.pyplot as plt
from csv import DictReader

data = reader = DictReader(open("globalterrorismdb_0616dist.csv", "rt", encoding="ISO-8859-1"))

suiSuc = 0
sui = 0
total = 0
suc = 0

i = 0
for row in data:
    if i == 0:
        i+=1
    else:
        suicide = row["suicide"]
        success = row["success"]
        if suicide == "1" and success == "1":
            sui += 1
            suiSuc += 1
            total += 1
            suc += 1
        elif suicide == "1":
            sui += 1
            total += 1
        elif success == "1":
            suc += 1
            total += 1
        else:
            total += 1

p_ss = suiSuc / total
p_s = sui/ total
p = p_ss / p_s
print("P(Success|Suicide)=", p)

p_sns = suc / total
p_ns = (total - sui) / total
p_n = p_sns / p_ns
print("P(Success|not Suicide)=", p_n)

p_suc = suc / total

p_in = p_s * p_suc
print("P(Success * Suicide)=", p_ss)
print("P(Suicide)P(Success)=", p_in)
if p_ss == p_in:
    print("The success of the attack is independent of whether the attack was a suicide.")
else:
    print("The success of the attack is dependent of whether the attack was a suicide.")


# 26. Find the second-largest distinct value in a dictionary.

d = {"Sam" : 1101,
     "Vam" : 20,
     "Tam" : 45,
     "Ram" : 541
    }

lie = []
for value in d.values(): # ye meko value lake dega
    lie.append(value) # ab un values ko apan empty list me append karege
lie.sort()           # sort se hum hamari list ko shai order me laege
print(lie[len(lie)-2]) # iska mtb ki hum last ke do element hata dege ye automatically second largest dedega

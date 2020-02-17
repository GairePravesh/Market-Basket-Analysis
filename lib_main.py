from apyori import apriori

transcations = []

with open("data.csv", "r") as file:
    for line in file:
        transcations.append([x.replace('\n', '') for x in line.split(',')])

results = list(apriori(transcations, min_support=0.15,min_confidence=0.5,min_lift=1.0,min_length=2))
for r in results: 
    print(r, end="\n\n")


#Apriori Implementation in Python
import csv 
from itertools import combinations, chain
import pprint
import sys

statistics = []
SupportRecord = {}

class Transaction(object):

    def __init__(self, transaction):
        self.itemsTable = {}
        self.items = []
        self.transactionCount = 0
        for itemSets in transaction:
            self.add_transaction(itemSets)

    def getItems(self):
        return [frozenset([item]) for item in self.items]
        
    def add_transaction(self, itemSets):
        for item in itemSets:
            if item not in self.itemsTable:
                self.items.append(item)
                self.itemsTable[item] = set()
            self.itemsTable[item].add(self.transactionCount)
        self.transactionCount += 1

    def calculateSupport(self, candidates):
        if not candidates:
            return 1.0
        totalIndexes = None
        for candidate in candidates:
            indexes = self.itemsTable.get(candidate)
            if indexes is None:
                return 0.0
            if totalIndexes is None:
                totalIndexes = indexes
            else:   
                totalIndexes = totalIndexes.intersection(indexes)
        return float(len(totalIndexes)/self.transactionCount)

def loadData(filepath):
    with open(filepath) as csvFile:
        trans = csv.reader(csvFile, delimiter=",")
        for row in trans:
            yield row if row else ['']

def nextCandidates(prevCandidates, k):
    items = sorted(frozenset(chain.from_iterable(prevCandidates)))
    tmp_candidates = (frozenset(x) for x in combinations(items, k))
    if k < 3: return tmp_candidates 

    next_candidates = [
                candidate for candidate in tmp_candidates
                if all(
                    frozenset(x) in prevCandidates
                    for x in combinations(candidate, k - 1))
            ]   
    return next_candidates    

def Support(transaction, min_support):
    candidates = transaction.getItems()
    k = 1
    while candidates:
        supportedRelations = set()
        for candidate in candidates:
            support = transaction.calculateSupport(candidate)
            if support < min_support:
                continue
            supportedRelations.add(candidate)
            SupportRecord[candidate] = support
        k += 1
        candidates = nextCandidates(supportedRelations, k)

def constraintsCalculation(transaction, record, min_confidence, min_lift):
    items = record
    for index in range(len(items)):
        for item in combinations(items, index):
            confidence = SupportRecord[record] / transaction.calculateSupport(item)
            if confidence < min_confidence: continue
            lift = confidence / transaction.calculateSupport(items.difference(item))
            if lift < min_lift: continue
            statistics.append([item, items.difference(item), confidence, lift])

def apriori(descendent=None, support=0.2, confidence=0.5, lift=1.0):
    min_support = support
    min_confidence = confidence
    min_lift = lift
    transacObj = loadData("data.csv")
    transaction = Transaction(transacObj)
    Support(transaction, min_support)
    for record in SupportRecord:
        constraintsCalculation(transaction, record, min_confidence, min_lift)
    
    results = []

    print("{:20}{:20}{:20}{}".format("antecedents","descendants","confidence","lift"))
    print(65*"#")
    for result in statistics:
        if descendent:
            if descendent in result[1]:
                results.append(result)
                print("{:20}{:20}{:.2f}{:20.2f}".format(', '.join(result[0]),', '.join(result[1]), result[2], result[3]))
        else:
            print("{:20}{:20}{:.2f}{:20.2f}".format(', '.join(result[0]),', '.join(result[1]), result[2], result[3]))
            results.append(result)


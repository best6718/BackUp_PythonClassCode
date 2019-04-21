"""
Karena Huang
CS80K Python
4/16/19
tuple_to_dict.py
"""
import operator
theTuple = (('a',33), ('b', 2), ('c', 13))
theDict = dict(theTuple)
print("This is the tuple as a dictionary: ")
print(theDict)
theList = list(theDict.items())
print("This is the dictionary converted into a list of tuples: ")
print(theList)
theList.sort(key = operator.itemgetter(1))
print("This is the list sorted: ")
print(theList)


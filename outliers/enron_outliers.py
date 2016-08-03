#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL",0)

for person in data_dict:
    if ((data_dict[person]["salary"]>1000000) & (data_dict[person]["salary"]!="NaN") & (data_dict[person]["bonus"]>5*10**6) & (data_dict[person]["bonus"]!="NaN")):# & (data_dict[person]["bonus"]>5*10**6)):
        print "Outlier:",person


features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    if (salary>2.5*10**7):
        print salary

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

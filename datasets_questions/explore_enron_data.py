#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
number = 0

print enron_data

for employess in enron_data:
    if enron_data[employess]["poi"] == 1:
        print employess
        number += 1

print "number of employess with POI:",number
print "The total value of stocks owned by Prentice James:",enron_data["PRENTICE JAMES"]["total_stock_value"]
print "The total # of messages from Wesley Colwell to POI:",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Stock options exercised by SKILLING JEFFREY K:",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Total Payments SKILLING JEFFREY K:",enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Total Payments LAY KENNETH L:",enron_data["LAY KENNETH L"]["total_payments"]
print "Total Payments FASTOW ANDREW S:",enron_data["FASTOW ANDREW S"]["total_payments"]

quantifyableSalary=0
for employess in enron_data:
    if enron_data[employess]["salary"] != "NaN":
        quantifyableSalary += 1

print "# of people with quantifyable salary:",quantifyableSalary

knownEmailAdd=0

for employess in enron_data:
    if enron_data[employess]["email_address"] != "NaN":
        knownEmailAdd += 1

print "# of people with known email address:",knownEmailAdd

totalPaymentsNan=0

for employess in enron_data:
    if enron_data[employess]["total_payments"] == "NaN":
        totalPaymentsNan += 1

print "# of people with NaN total payments:",totalPaymentsNan
print "# of entries in dictionary:",len(enron_data)
#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
#c: 10: 0.616040955631; 100: 0.616040955631; 10:0.821387940842; 10000: 0.892491467577

def classifysvm(features_train, labels_train):
    from sklearn import svm
    clf = svm.SVC(kernel="rbf",C=10000)
    clf.fit(features_train, labels_train)
    return clf

t0=time()
clf = classifysvm(features_train, labels_train)
print "training time:",round(time()-t0,3),"s"

from sklearn.metrics import accuracy_score
t1=time()

pred=clf.predict(features_test)

### Counter
### We can decipher the number of occurences of each element in array using Counter
import collections
counter = collections.Counter(pred)
### end

print "prediction time:",round(time()-t1,3),"s"
print "predicted value:",counter
#print accuracy_score(labels_test,pred)


#########################################################



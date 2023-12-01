import scipy.io
import glob
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearnex import patch_sklearn 
import matplotlib.pyplot as plt
patch_sklearn()

def svm_train(train_data, test_data, train_target, test_target, gamma_value):
    accuracy = []
    precision = []
    recall = []

#     testing_range = np.linspace(0.1,1,10)

#     for gamma_value in testing_range:
#     cls = svm.SVC(kernel='rbf', gamma=0.3, C=1, verbose=1)
  
    cls = svm.SVC(kernel='rbf', gamma=gamma_value, C=1, verbose=1)
    cls.fit(train_data, train_target)
    pred = cls.predict(test_data)
    # accuracy.append(metrics.accuracy_score(test_target,pred))
    # precision.append(metrics.precision_score(test_target,pred))
    # recall.append(metrics.recall_score(test_target,pred))

    print("accuracy:", metrics.accuracy_score(test_target,pred))
    print()
    print("precision:", metrics.precision_score(test_target,pred))
    print()
    print("recall:", metrics.recall_score(test_target,pred))
    print()
    print(metrics.classification_report(test_target,pred))

  
    # plt.figure(figsize=(12, 8))
    # plt.plot(accuracy, color='r', label='accuracy')
    # plt.plot(precision, color='g', label='precision')
    # plt.plot(recall, color='b', label='recall')
    # plt.xlabel("RBF Kernel Value")
    # plt.ylabel("Metrics Report")
    # plt.title("Testing Various RBF Values")
    # plt.legend()
# !/usr/bin/python3 
import time
from data_set import DataSet
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

gnb = GaussianNB()
dtc = DecisionTreeClassifier(criterion ="entropy", max_depth = 4)
rfst = RandomForestClassifier(n_estimators = 30)
svc = SVC(gamma = 'scale')


""" model """
class model:
    """ initial(construct) """
    def __init__(self):
        self.dataset = DataSet()
        self.dataset.load_dataset(0, 2)
        self.dataset.pre_process()
        self.X_train, self.X_test, self.y_train, self.y_test = self.dataset.split_train_test()


    def start(self, name="Gaussian Naive Bayes Model", model=gnb):
        print("--------- " + name + " ----------")
        # Training
        start_time = time.time()
        model.fit(self.X_train, self.y_train.values.ravel())
        end_time = time.time()
        print("Training time: ", end_time - start_time)

        #Testing
        start_time = time.time()
        y_test_pred = model.predict(self.X_train)
        end_time = time.time()
        print("Testing time: ", end_time - start_time)

        # Test and train scores
        print("Train score is:", model.score(self.X_train, self.y_train))
        print("Test score is:", model.score(self.X_test, self.y_test))

    
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from config import config


""" The path to store the kdd dataset """
kddcup_99_data_path = [
    "../dataset/kddcup.data_10_percent.gz",
    "../dataset/kddcup.data.gz"
]


"""  dataset """
class DataSet:
    """ initial(construct) """
    def __init__(self):
        self.columns = []
        self.dataset = None
    

    """ load dataset """
    def load_dataset(self, index):
        for c in config.cols.split(','):
            if (c.strip()):
                self.columns.append(c.strip())
        self.columns.append('target')
        self.dataset = pd.read_csv(kddcup_99_data_path[index], names = self.columns)

    
    """ preprocessing """
    def pre_process(self):
        self.dataset['Attack_Type'] = self.dataset.target.apply(lambda r:config.attacks_types[r[:-1]])
        # Drop columns with NaN
        self.dataset.dropna(axis='columns')
        # Keep columns where there are more than 1 unique values
        self.dataset = self.dataset[[col for col in self.dataset if self.dataset[col].nunique() > 1]]
        # Drop highly correlated variables as these should be ignored for learning
        self.dataset.drop('num_root',axis = 1,inplace = True)
        self.dataset.drop('srv_serror_rate',axis = 1,inplace = True)
        self.dataset.drop('srv_rerror_rate',axis = 1, inplace=True)
        self.dataset.drop('dst_host_srv_serror_rate',axis = 1, inplace=True)
        self.dataset.drop('dst_host_serror_rate',axis = 1, inplace=True)
        self.dataset.drop('dst_host_rerror_rate',axis = 1, inplace=True)
        self.dataset.drop('dst_host_srv_rerror_rate',axis = 1, inplace=True)
        self.dataset.drop('dst_host_same_srv_rate',axis = 1, inplace=True)
        # Drop 'service' since provides no useful information for learning
        self.dataset.drop('service',axis = 1, inplace=True)
        # Convert protocol values
        self.dataset['protocol_type'] = self.dataset['protocol_type'].map(config.pmap)
        self.dataset['flag'] = self.dataset['flag'].map(config.fmap)


    def split_train_test(self, t_size, r_state):
        self.dataset = self.dataset.drop(['target', ], axis=1)
        y = self.dataset[['Attack_Type']]
        X = self.dataset.drop(['Attack_Type', ], axis=1)
        min_max_sc = MinMaxScaler()
        X = min_max_sc.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                    test_size=t_size, random_state=r_state)
        return X_train, X_test, y_train, y_test


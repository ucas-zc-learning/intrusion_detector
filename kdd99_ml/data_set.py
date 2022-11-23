import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from config import config


""" The path to store the kdd dataset """
kddcup_99_data_path = [
    "../dataset/kddcup.data_10_percent.gz",
    "../dataset/kddcup.data.gz",
    "../dataset/corrected.gz"
]


"""  dataset """
class DataSet:
    """ initial(construct) """
    def __init__(self):
        self.columns = []
        self.dataset = None
        self.test_dataset = None
    

    """ load dataset """
    def load_dataset(self, train_index, test_index):
        for c in config.cols.split(','):
            if (c.strip()):
                self.columns.append(c.strip())
        self.columns.append('target')
        self.dataset = pd.read_csv(kddcup_99_data_path[train_index], names = self.columns)
        self.test_dataset = pd.read_csv(kddcup_99_data_path[test_index], names = self.columns)
        print(self.dataset.columns)
        print(self.test_dataset.columns)

    
    """ preprocessing """
    def pre_process(self):
        self.dataset = self.__preprocessing(self.dataset)
        self.test_dataset = self.__preprocessing(self.test_dataset)


    def __preprocessing(self, dataset):
        _dataset = dataset.copy()
        _dataset['Attack_Type'] = _dataset.target.apply(lambda r:config.attacks_types[r[:-1]])
        # Drop columns with NaN
        _dataset.dropna(axis='columns')
        print(len(_dataset.columns))
        # Keep columns where there are more than 1 unique values
        #_dataset = _dataset[[col for col in _dataset if _dataset[col].nunique() > 1]]
        print(len(_dataset.columns))
        # Drop highly correlated variables as these should be ignored for learning
        _dataset.drop('num_root', axis = 1, inplace = True)
        _dataset.drop('srv_serror_rate', axis = 1, inplace = True)
        _dataset.drop('srv_rerror_rate', axis = 1, inplace=True)
        _dataset.drop('dst_host_srv_serror_rate', axis = 1, inplace=True)
        _dataset.drop('dst_host_serror_rate', axis = 1, inplace=True)
        _dataset.drop('dst_host_rerror_rate', axis = 1, inplace=True)
        _dataset.drop('dst_host_srv_rerror_rate', axis = 1, inplace=True)
        _dataset.drop('dst_host_same_srv_rate', axis = 1, inplace=True)
        # Drop 'service' since provides no useful information for learning
        _dataset.drop('service', axis = 1, inplace=True)
        # Convert protocol values
        _dataset['protocol_type'] = _dataset['protocol_type'].map(config.pmap)
        _dataset['flag'] = _dataset['flag'].map(config.fmap)
        _dataset['Attack_Type'] = _dataset['Attack_Type'].map(config.amap)
        print(len(_dataset.columns))
        return _dataset


    def split_train_test(self):
        self.dataset = self.dataset.drop(['target', ], axis=1)
        self.test_dataset = self.test_dataset.drop(['target', ], axis=1)
        #self.test_dataset = self.test_dataset.drop(['is_host_login', ], axis=1)
        y_train = self.dataset[['Attack_Type']]
        y_test = self.test_dataset[['Attack_Type']]
        X_train = self.dataset.drop(['Attack_Type', ], axis=1)
        X_test = self.test_dataset.drop(['Attack_Type', ], axis=1)
        min_max_sc = MinMaxScaler()
        X_train = min_max_sc.fit_transform(X_train)
        X_test = min_max_sc.fit_transform(X_test)
        return X_train, X_test, y_train, y_test


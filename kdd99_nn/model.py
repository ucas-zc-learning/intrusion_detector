# !/usr/bin/python3

from data_set import DataSet
from keras.models import Sequential
from keras.layers import Dense, Conv1D, MaxPooling1D, Flatten, Dropout

shallow_model = Sequential([
    Dense(1024, input_dim = 30, activation='relu'),
    Dropout(0.01),
    Dense(5, activation='softmax')
])

deep_model = Sequential([
    Dense(1024, input_dim=30, activation='relu'),
    Dropout(0.01),
    Dense(768, activation='relu'),
    Dropout(0.01),
    Dense(512, activation='relu'),
    Dropout(0.01),
    Dense(256, activation='relu'),
    Dropout(0.01),
    Dense(128, activation='relu'),
    Dropout(0.01),
    Dense(5, activation='softmax')
])

cnn_model = Sequential([
    Conv1D(64, 3, padding="same", activation="relu", input_shape=(30,1)),
    MaxPooling1D(pool_size=(2)),
    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(5, activation="softmax")
])


class model:
    def __init__(self):
        self.dataset = DataSet()
        self.dataset.load_dataset(0, 2)
        self.dataset.pre_process()
        self.X_train, self.X_test, self.y_train, self.y_test = self.dataset.split_train_test()


    def start(self, name="shallow neural network", model=shallow_model):
        print("---------- " + name + " -----------")
        model.compile(loss ='sparse_categorical_crossentropy', 
                        optimizer = 'adam', metrics = ['accuracy'])
        model.fit(self.X_train, self.y_train.values.ravel(), epochs=10, batch_size=32)
        
        
import numpy as np
import os
import sys
import pandas as pd
import keras



try:
    #Loading Dataset
    (X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()

    X_test_flattened = (X_test.reshape(len(X_test),28*28))/255
    X_train_flattened = (X_train.reshape(len(X_train),28*28))/255


    #Training the model
    model = keras.Sequential([
        keras.layers.Dense(300, input_shape=(784,), activation = 'relu'),
        keras.layers.Dense(10,activation='sigmoid')
    ])

    opt = keras.optimizers.Adam()
    model.compile(optimizer = opt, loss = 'sparse_categorical_crossentropy', metrics = 'sparse_categorical_accuracy')
    model.fit(X_train_flattened,y_train, epochs = 5)

    #save the pickle file
    save_directory = 'artifacts/'
    os.makedirs(save_directory, exist_ok=True)
    nnmodel = 'nn.h5'
    file_path = os.path.join(save_directory, nnmodel)

    model.save(file_path)

except Exception as e:
    print(f"Error occurred at model.py --> {e}")
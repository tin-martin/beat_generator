import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten 
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten,MaxPooling2D,MaxPooling1D,Conv1D
import pickle
import numpy as np
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
import bz2
import pickle 
import _pickle as cPickle
import math
from keras import backend as K
import matplotlib.pyplot as plt
import os
#x = pickle.load(open("x.pickle","rb"))
#y = pickle.load(open("y.pickle","rb"))
from keras.models import load_model
import numpy as np


def decompress_pickle(file):
	data = bz2.BZ2File(file,'rb')
	data = cPickle.load(data)
	return data

specgrams1 = np.loadtxt("/Users/martintin/Desktop/beat_generator/pickle_data/specgrams1a.txt")
specgrams2 = np.loadtxt("/Users/martintin/Desktop/beat_generator/pickle_data/specgrams2a.txt")
specgrams3 = np.loadtxt("/Users/martintin/Desktop/beat_generator/pickle_data/specgrams3a.txt")

onsets = decompress_pickle("/Users/martintin/Desktop/beat_generator/pickle_data/onsets(5).pbz2")

specgrams = np.concatenate((specgrams1,specgrams2,specgrams3),axis=0)
specgrams = specgrams.reshape(-1,24,5,1)



X_train = []
X_test = []

len_train = math.trunc(len(onsets)*0.70)
len_test = len(onsets) - len_train

print(len_train,len_test)

X_train, X_test = specgrams[:len_train],specgrams[len_train:]
print(X_train.shape,X_test.shape)

Y_train, Y_test = np.asarray(onsets[:len_train]), np.asarray(onsets[len_train:])
print(Y_train.shape,Y_test.shape)

X_train = X_train.reshape(len_train,24,5,1)
X_test = X_test.reshape(len_test,24,5,1)
Y_train = Y_train.reshape(len_train,1)
Y_test = Y_test.reshape(len_test,1)


print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
ones =[]
for i in range(len(ons)):
	for c in range(len(specgrams[0])):
		
			print(specgrams[i][c][x])
			print(type(specgrams[i][c][x]))
			if specgrams[i][c][x] == 1:
				ones+=1

#create model
model = Sequential()
#add model layers
model.add(Conv2D(32,kernel_size=2,input_shape=(24,5,1)))  
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=2,strides=2,padding='same'))  

model.add(Conv2D(64, kernel_size=2,padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=2,strides=2,padding='same'))

model.add(Conv2D(128, kernel_size=2,padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=2,strides=2,padding='same'))

model.add(Conv2D(256, kernel_size=2,padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=2,strides=2,padding='same'))


model.add(Flatten())
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.5))

model.add(Dense(1, activation='softmax'))

#model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

K.set_value(model.optimizer.learning_rate, 0.0001)
history = model.fit(x=X_train, y=Y_train, validation_data=(X_test, Y_test), epochs=40)

model.save('/Users/martintin/Desktop/beat_generator/model.h5')
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


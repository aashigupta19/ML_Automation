#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import Sequential
from keras.layers import MaxPool2D, Conv2D, Flatten, Dense, Dropout
from keras.datasets import fashion_mnist
from keras.callbacks import Callback
from keras.utils import np_utils
from sklearn.metrics import accuracy_score
import numpy as np

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()


# In[2]:


x_train.shape


# In[3]:


print("shape of training X", x_train.shape)
print("shape of training Y", y_train.shape)
print("shape of testing X", x_test.shape)
print("shape of testing Y", y_test.shape)


# In[4]:


x_train_new = x_train.reshape(60000, 28, 28, 1)
x_train_new = x_train_new.astype('float32')
x_train_new = x_train_new/255.0

x_test_new = x_test.reshape(10000, 28, 28, 1)
x_test_new = x_test_new.astype('float32')
x_test_new = x_test_new/255.0


# In[5]:


y_train.shape


# In[6]:


y_train_new = np_utils.to_categorical(y_train)
y_test_new = np_utils.to_categorical(y_test)


# In[7]:


print("shape of training X after processing", x_train_new.shape)
print("shape of training Y after processing", y_train_new.shape)
print("shape of testing X after processing", x_test_new.shape)
print("shape of testing Y after processing", y_test_new.shape)


# In[8]:


#model creation
model = Sequential()

model.add(Conv2D(32, (3,3), activation = 'relu', input_shape = (28,28,1) ))
model.add(MaxPool2D(pool_size=(2, 2) ))
model.add(Flatten())
model.add(Dense(128, activation = 'relu'))
model.add(Dense(10,  activation = 'softmax'))          


# In[9]:


model.summary()


# In[14]:


class myCallback(Callback):
      def on_epoch_end(self, epoch, logs={}):
          
            file='/root/accuracy.txt' 
            var=logs.get('accuracy')
            with open(file, 'w') as filetowrite:
                filetowrite.write(np.array2string(var))




callbacks = myCallback()


# In[15]:


model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'] )


# In[16]:


epochs = 10
history = model.fit(x_train_new, y_train, epochs=epochs, callbacks=[callbacks])


# In[ ]:


#end of code :))))) 


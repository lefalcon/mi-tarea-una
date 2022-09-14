# link:
# https://machinelearningmastery.com/image-augmentation-deep-learning-keras/

# another useful link:
# https://towardsdatascience.com/exploring-image-data-augmentation-with-keras-and-tensorflow-a8162d89b844 

# Example to apply Transformations to images like Shift, Zoom in and out, Rotations
# Standarization
# ZCA standardization
# Rotation
# Shifts
# Shear
# Flips


#import cv2

#path = "/home/lefalcon/Pictures/"
#img = cv2.imread(path + "lena.png")
#cv2.imshow("image", img)
#cv2.waitKey()

# MNIST Data Augemntation example....

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from keras.datasets import mnist
from matplotlib import pyplot


# loading data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# create a grid of 3x3 images:
for k in range(0,9):
   pyplot.subplot(330+1+k)
   pyplot.imshow(X_train[k], cmap=pyplot.get_cmap('gray'))

# show the plot:
pyplot.show()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Feature Standarization:
from keras.preprocessing.image import ImageDataGenerator

# Reshape the images to be [samples][width][height][channels]
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))

# convert from int to float:
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# define data preparation:
# FEATURE STANDARDIZATION +++++++++++++++++++++++++++++++++++++++
# something is not working with this one... check later..
#datagen = ImageDataGenerator(featurewise_center=True, featurewise_std_normalization=True)

# ZCA WHITENING +++++++++++++++++++++++++++++++++++++++++++++++++
#datagen = ImageDataGenerator(zca_whitening=True)

# RANDOM ROTATIONS ++++++++++++++++++++++++++++++++++++++++++++++
# rotations to left and right up to a limit of 90 degrees:
datagen = ImageDataGenerator(rotation_range=90)

# RANDOM SHIFTS +++++++++++++++++++++++++++++++++++++++++++++++++
# Objects in your images may not be centered in the frame.
# You can train your DL network to expect and currently
# handle off-center objects by artificially creating 
# shifted versions of your training data.
#shift = 0.2
#datagen = ImageDataGenerator(width_shift_range=shift, height_shift_range=shift)

# RANDOM FLIPS ++++++++++++++++++++++++++++++++++++++++++++++++++
#datagen = ImageDataGenerator(horizontal_flip=True, vertical_flip=True)

# Activating the default characteristics ... what are those???:
# I think that this one is only the standardization option...
#datagen = ImageDataGenerator()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SAVING IAMGES:
import os
# The following line must be used only the first time, because it will create the directory:
#os.makedirs('aug_images')

# fit parameters from data:
datagen.fit(X_train)


# configure batch size and retrive one batch of images:
for X_batch, y_batch in datagen.flow(X_train, y_train, batch_size=9):
#for X_batch, y_batch in datagen.flow(X_train, y_train, batch_size=9, save_to_dir='aug_images', save_prefix='aug', save_format='png'):
   for k in range(0,9):
      pyplot.subplot(330+1+k)
      pyplot.imshow(X_batch[k].reshape(28,28), cmap=pyplot.get_cmap('gray'))

   pyplot.show()
   break






















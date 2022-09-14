
# From de Book-2, Chapter 2, of Adrian Rosebrock

# ver tambien link:
# https://towardsdatascience.com/exploring-image-data-augmentation-with-keras-and-tensorflow-a8162d89b844 

#  SINGLE IMAGE - DATA AUGMENTATION

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from matplotlib import pyplot
from matplotlib.pyplot import imread, imshow, subplots, show
import numpy as np

# Load a single Image:
path = "/home/lefalcon/Pictures/"
img = load_img(path+"lena.png")
imshow(img)
show()
img = img_to_array(img)
img = np.expand_dims(img, axis=0)


# initializing the ImageDataGenerator:

aug = ImageDataGenerator(
         rotation_range=45,
         zoom_range=[0.5,1.5], #0.15,
         width_shift_range=0.2,
         height_shift_range=0.1,
         shear_range=0.15,
         horizontal_flip=True,
         vertical_flip=True,
         brightness_range=(0.7,0.9),
         channel_shift_range=150.0,
         fill_mode="nearest")  # Options:"nearest", "reflect", "wrap", "constant" with cval=constante.


pathdir = "/home/lefalcon/Pictures/output"
imgGen = aug.flow(img, batch_size=1, 
                       save_to_dir=pathdir, 
                       save_prefix="aug", 
                       save_format="png")


total = 0
for img in imgGen:
   imgs = img.reshape((img.shape[1], img.shape[2], 3))
   pyplot.subplot(330+1+total)
   imshow(imgs.astype('uint8'))

   total += 1

   if total==9:
      break
show()






















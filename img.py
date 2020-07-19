from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math


def imshow(img):
   """ tuple[list[PixelType],int,int] -> NoneType
       affiche une image scalaire ou RGB
   """
   ImageFile = 'bak.jpg'
   img = Image.open(ImageFile)
   data,x,y=img
   if type(data[0]) is tuple:
      plt.imshow(np.array(data).reshape(y,x,len(data[0])) / 255)
   elif type(data[0]) is float:
      plt.imshow(np.array(data).reshape(y,x),cmap='gray')
   else:
      plt.imshow(np.array(data).reshape(y,x),vmin=0,vmax=255,cmap='gray')
      plt.show()

def pil2img(pil):
   """ PIL.Image -> tuple[list[PixelType],int,int]
       convertit une image PIL vers notre format interne d'image
   """
   return (list(pil.getdata()),pil.width,pil.height)

import glob

for file in glob.glob('img/*.*'):
  img = Image.open(img)
  L=list(img.getdata())
  print ('image:',file,'format: ', img.format, 'mode:', img.mode,
         'dimensions:', img.size,'val 1er pixel:',L[0])
  imshow(pil2img(img))
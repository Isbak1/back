import sys
from scipy import misc
import matplotlib.pyplot as plt
# ouverture du fichier image
ImageFile = 'bak.jpg'
try:
  img = misc.imread(ImageFile)
except IOError:
  print('Erreur sur ouverture du fichier ' + ImageFile)
  sys.exit(1)
# affichage des caractéristiques de l'image
print(img.shape)
# affichage de l'image
plt.imshow(img)
plt.axis('off')
plt.show()
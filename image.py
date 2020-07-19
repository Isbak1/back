import sys
from PIL import Image
# ouverture du fichier image
from numpy import size

ImageFile = 'bak.jpg'


def importation(filename, degre=0, contrast=1):
    try:
        img = Image.open(filename)
        img = img.rotate(degre)

    except IOError:
        print('Erreur sur ouverture du fichier ' + img)
        sys.exit( 1 )
    # affichage des caractéristiques de l'image
    print( img.format, img.size, img.mode )
    # affichage de l'image

    from PIL import ImageEnhance
    enh = ImageEnhance.Contrast(img)
    print(filename)
    enh.enhance(contrast).save(filename)
    # fermeture du fichier image
    img.close()
    return filename

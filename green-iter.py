import numpy as np
import cv2


img = 'D:/pr/chromaKay/chromaKey/image1/whithoutBG/DSCF7680.JPG'


def add_black(img):
    image = cv2.imread(img)
    print(image.shape)
    height = image.shape[0]
    h = 0
    width = image.shape[1]
    w = 0
    fon = '/imagehash.png'
    fon
    fon = cv2.resize(fon, (width, height))

    cv2.imshow('resDark', image)
    cv2.imshow('f', fon)

    cv2.waitKey(0)
add_black(img)
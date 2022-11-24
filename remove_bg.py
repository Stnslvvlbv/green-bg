from rembg.bg import remove
from rembg import remove
import cv2
import numpy as np
input_path = 'D:/pr/chromaKay/chromaKey/image1/wb6.png'
output_path = 'D:/pr/chromaKay/chromaKey/image1/wb6cb.png'


def black_bg(input_image, output_image):

    input = cv2.imread(input_image)
    output = remove(input)

    convert = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    result = cv2.cvtColor(convert, cv2.COLOR_BGR2RGB)

    cv2.imshow('resDk', result)

    cv2.waitKey(0)
    cv2.imwrite(output_image, result)

black_bg(input_path, output_path)
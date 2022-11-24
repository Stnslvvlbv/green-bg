import numpy as np
import cv2


img = 'D:/pr/chromaKay/chromaKey/images/wb6.png'


def mask(frame, downGreen, upGreen):
    """
    :param frame: Изображение после форматирования размера
    :param downGreen: самый темный оттенок зеленого
    :param upGreen:  самый светлый оттенок зеленого
    :return: область для вырезания
    """
    mask = cv2.inRange(frame, downGreen, upGreen)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    frame = frame - res
    contours2, hierarchy2 = cv2.findContours(image=mask, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image=frame, contours=contours2, contourIdx=-9, color=(0, 0, 0), thickness=0,
                     lineType=cv2.LINE_AA)

    cv2.imshow('resDark', res)
    cv2.imshow('f', frame)

    cv2.waitKey(0)
    return frame


def green_cut(img):
    """"""
    fon = cv2.imread('fon.jpg')
    image = cv2.imread(img)

    greenFrame = [
        [[0, 130, 0], [90, 255, 90]],
        [[0, 110, 0], [80, 150, 80]],
        [[0, 100, 0], [70, 150, 70]],
        [[0, 90, 0], [60, 150, 60]],
        [[0, 80, 0], [55, 150, 55]],
        [[0, 70, 0], [40, 130, 40]],
        [[0, 60, 0], [40, 120, 35]],
        [[0, 50, 0], [30, 120, 20]],
        [[0, 40, 0], [25, 100, 15]],
        [[0, 30, 0], [15, 100, 15]],
    ]

    frame = cv2.resize(image, (1000, 700))
    fon = cv2.resize(fon, (1000, 700))
    for colors in greenFrame:
        frame = mask(frame, np.array(colors[0]), np.array(colors[1]))

    # f = frame - res1 - resDark

    cv2.imshow('f', frame)
    # cv2.imshow('res1', res1)
    # cv2.imshow('resDark', resDark)

    cv2.waitKey(0)


def green_pixel(img, output_path):

    # Green color in BGR
    color = (0, 0, 0)
    radius = 2
    step = 10
    # Line thickness of 9 px
    thickness = -1

    image = cv2.imread(img)
    height = image.shape[0]
    h = 0
    width = image.shape[1]
    w = 0

    frame = image
    while h < height:
        while w < width:
            (b, g, r) = image[h, w]
            if g < 230:
                if (g - 40) > b or (g - 40) > r:
                    start = [w, h]
                    cv2.circle(frame, start, radius, color, thickness)
            elif g < 90:
                if (g - 30) > b or (g - 30) > r:
                    start = [w, h]
                    cv2.circle(frame, start, radius, color, thickness)
            elif g < 70:
                if (g - 25) > b or (g - 25) > r:
                    start = [w, h]
                    cv2.circle(frame, start, radius, color, thickness)
            elif g < 50:
                if (g - 20) > b or (g - 20) > r:
                    start = [w, h]
                    cv2.circle(frame, start, radius, color, thickness)
            elif g < 30:
                if (g - 15) > b or (g - 15) > r:
                    start = [w, h]
                    cv2.circle(frame, start, 0, color, thickness)

            w = w + step
        h = h + step
        w = 0

    cv2.imshow('f', frame)

    cv2.waitKey(0)
    # cv2.imwrite(output_path, frame)
green_pixel(img, 0)
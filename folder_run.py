from rembg.bg import remove
import os
import cv2


dir_load = 'D:/pr/chromaKay/chromaKey/image1'


def black_bg(input_image, output_image):
    with open(input_image, 'rb') as i:
        with open(output_image, 'wb') as o:
            input_img = i.read()
            output_img = remove(input_img)
            o.write(output_img)


def green_pixel(input_image, output_image):
    """
    попиксельное удаление оттенков зеленого
    :param input_image: адрес фото для обработки
    :param output_image: адрес для сохранения обрезанного фото
    :return:
    """
    # Green color in BGR
    COLOR = (0, 0, 0)
    RADIUS = 2
    STEP = 1
    THICKNESS = -1

    image = cv2.imread(input_image)
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
                    cv2.circle(frame, start, RADIUS, COLOR, THICKNESS)
            elif g < 90:
                if (g - 30) > b or (g - 30) > r:
                    start = [w, h]
                    cv2.circle(frame, start, RADIUS, COLOR, THICKNESS)
            elif g < 70:
                if (g - 25) > b or (g - 25) > r:
                    start = [w, h]
                    cv2.circle(frame, start, RADIUS, COLOR, THICKNESS)
            elif g < 50:
                if (g - 20) > b or (g - 20) > r:
                    start = [w, h]
                    cv2.circle(frame, start, RADIUS, COLOR, THICKNESS)
            elif g < 30:
                if (g - 15) > b or (g - 15) > r:
                    start = [w, h]
                    cv2.circle(frame, start, 0, COLOR, THICKNESS)

            w = w + STEP
        h = h + STEP
        w = 0

    # cv2.imshow('f', frame)
    # cv2.waitKey(0)
    cv2.imwrite(output_image, frame)


def folder_run(dir, green=False):
    dir_remove_bg = dir + "/whithoutBG"
    try:
        os.mkdir(dir_remove_bg)
    except:
        pass

    image_load = []
    count = 0

    print('Поиск изоброжений в папке...')
    for filename in os.listdir(dir):
        if filename[filename.rfind(".")+1:] in ['jpg', 'JPG', 'jpeg', 'png', 'gif']:
            count += 1
            print(filename)
            image_load.append(filename)

    print("В папке найдено изображений:", count)
    print("Запущенно удаление фона...")

    count_bg = 0
    for img in image_load:
        count_bg += 1
        input_image = dir + '/' + img
        output_image = dir_remove_bg +'/' + img
        print("обработка фотографии", count_bg, "из", count)
        if green:
            green_pixel(input_image, output_image)
        else:
            black_bg(input_image, output_image)


folder_run(dir_load, green=False)
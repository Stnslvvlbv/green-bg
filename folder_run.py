from rembg.bg import remove
import os
import cv2


dir_load = 'D:/pr/chromaKay/chromaKey/image1'


def black_bg(input_image, output_image):
    """
    Матирует прозрачным любой фон
    :param input_image: адрес фото для обработки
    :param output_image: адрес для сохранения обрезанного фото
    :return:
    """

    image = cv2.imread(input_image)
    output = remove(image)

    convert = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    result = cv2.cvtColor(convert, cv2.COLOR_BGR2RGB)

    # cv2.imshow('resDk', result)

    cv2.waitKey(0)
    cv2.imwrite(output_image, result)


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


def folder_run(folder, green=False):
    """
    По указанной папке ищет изоброжения и передает в обработку функции в зависимости от фона:
    green=False (По умолчанию) библиотекой remBG
    green=True пиксельное перекрашивание оттенков черного
    создает папку /withoutBG и отправляет адрес для сохранения в функцию обработки фото
    :param folder: Адрес папки для обработки
    :param green: Использовать ли пиксельное удаление оттенков зеленого или определить фон нейронной сетью
    :return:
    """
    dir_remove_bg = folder + "/withoutBG"
    try:
        os.mkdir(dir_remove_bg)
        print("В указанной папке создана директория '/withoutBG' для сохранения обработанных фотографий")
    except:
        print("Папка для сохранения обработанных фотографий уже существует")

    image_load = []
    count = 0

    print('Поиск изоброжений в папке...')
    for filename in os.listdir(folder):
        if filename[filename.rfind(".")+1:] in ['jpg', 'JPG', 'jpeg', 'png', 'gif']:
            count += 1
            print(filename)
            image_load.append(filename)

    print("В папке найдено изображений:", count)
    print("Запущенно удаление фона...")

    count_bg = 0
    for img in image_load:
        count_bg += 1
        input_image = folder + '/' + img
        output_image = dir_remove_bg +'/' + img
        print("обработка фотографии", count_bg, "из", count)
        if green:
            green_pixel(input_image, output_image)
        else:
            black_bg(input_image, output_image)


# folder_run(dir_load, green=False)

if __name__ == "__main__":
    url = ''
    while url != 'exit':
        print('Для выхода введите "exit"')
        print("Для продолжения введите абсолютный адресс папки с фотографиями для удаления фона:")
        url = input()
        dir_load = (r"" + url).replace('\\', '/')
        if os.path.exists(dir_load):
            folder_run(dir_load)
            print("Обработка найденных фотографий окончена")
        elif url != 'exit':
            print("По указанному адресу папка не найдена")
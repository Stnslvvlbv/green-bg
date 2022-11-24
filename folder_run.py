import os, sys


dir_load = 'D:/pr/chromaKay/chromaKey/image1'


def folder_run(dir, green=True):
    dir_remove_bg = dir + "/whithoutBG"
    try:
        os.mkdir(dir_remove_bg)
    except:
        pass

    image_load = []
    image_notbg = []
    count = 0

    print('Поиск изоброжений в папке...')
    for filename in os.listdir(dir):
        if filename[filename.rfind(".")+1:] in ['jpg', 'JPG', 'jpeg', 'png', 'gif']:
            count += 1
            print(filename)
            image_load.append(filename)

    print("В папке найдено изображений:", count)


folder_run(dir_load)
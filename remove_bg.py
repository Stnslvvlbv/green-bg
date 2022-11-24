from rembg.bg import remove

input_path = 'D:/pr/chromaKay/chromaKey/image1/wb6.png'
output_path = 'D:/pr/chromaKay/chromaKey/image1/wb6bg.png'


def black_bg(input_path, output_path):
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            inputi = i.read()
            outputi = remove(inputi)
            o.write(outputi)

black_bg(input_path, output_path)
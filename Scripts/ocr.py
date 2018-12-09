from wand.image import Image
import pytesseract as ocr
from PIL import Image
import datetime
import numpy
import cv2
import os


class ImageRec(object):

    @staticmethod
    def openFiles():
        file = []
        os.chdir(r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/Medias')
        for filename in os.listdir(os.getcwd()):
            file.append(filename)

        return file

    @staticmethod
    def vectorize(file):
        npImage = []
        for i in range(len(file)):
            # reading the image
            image = Image.open(r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/Medias/{}'.format(file[i])).convert('RGB')

            # image to editable numpy array convertion
            npImage.append(numpy.asarray(image).astype(numpy.uint8))

        return npImage

    @staticmethod
    def imageCleaning(npImage):
        # crop
        # npImage = npImage[2400:8800, 400:6500]

        # dilate
        # kernel = numpy.ones((5,5), numpy.uint8)
        # im = cv2.dilate(npImage, kernel, iterations = 1)

        # erode
        # kernel = numpy.ones((5,5), numpy.uint8)
        # im = cv2.erode(npImage, kernel, iterations = 1)

        # noise reduction
        npImage[:, :, 0] = 0
        npImage[:, :, 2] = 0

        # image serialisation
        img = cv2.cvtColor(npImage, cv2.COLOR_RGB2GRAY)

        # color intensity below 127 - 0 (black)
        # color intensity above 127 - 255 (white)
        ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # tresh image in a PIL.Image object array
        return Image.fromarray(thresh)

    @staticmethod
    def creatingPhrase(binImage):
        # setting the tesseract-ocr PATH
        ocr.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

        # Tesseract-OCR wrapper
        return ocr.image_to_string(binImage, lang='spa')

    @staticmethod
    def writer(phrase, files):
        file = open(r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/Outputs/{}.txt'.format(files), 'w')
        file.write(phrase)
        file.close()


if __name__ == '__main__':

    iTime = datetime.datetime.now()
    print('Begin {}'.format(iTime))

    im = ImageRec()

    file = im.openFiles()
    npImage = im.vectorize(file)

    print('Just opened the JPG files {}'.format(datetime.datetime.now()))

    binImage = []
    phrase = []
    for i in range(len(npImage)):
        binImage.append(im.imageCleaning(npImage[i]))
        print('Image Cleaning Finalized {}'.format(datetime.datetime.now()))
        phrase.append(im.creatingPhrase(binImage[i]))
        print('Generating texts {}'.format(datetime.datetime.now()))
        im.writer(phrase[i], file[i][:-4])

    print('Execution Time: {}'.format(datetime.datetime.now() - iTime))
from Scripts.pdfConverter import pdfConverter
from Scripts.classifier import Reader
from Scripts.scraper import Bolsar
from Scripts.ocr import ImageRec
import time


if __name__ == "__main__":
    p = Bolsar()
    p.search()
    time.sleep(3)
    p.close()

    pdf = pdfConverter()
    pdf.pdfConv()

    im = ImageRec()

    file = im.openFiles()
    npImage = im.vectorize(file)

    binImage = []
    phrase = []
    for i in range(len(npImage)):
        binImage.append(im.imageCleaning(npImage[i]))
        phrase.append(im.creatingPhrase(binImage[i]))
        im.writer(phrase[i], file[i][:-4])

    cls1 = Reader()
    cls1.main()

from wand.image import Image
import os


class pdfConverter(object):

    @staticmethod
    def pdfConv():
        pdf = []
        os.chdir(r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/PDFs')
        for filename in os.listdir(os.getcwd()):
            pdf.append(filename)

        string = []

        for i in range(len(pdf)):
            string.append(r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/PDFs/{}'.format(pdf[i]))

            with Image(filename=string[i], resolution=850) as img:
                with img.convert('jpg') as converted:
                    converted.save(
                        filename=r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/Medias/{}.jpg'.format(pdf[i][:-4]))


if __name__ == '__main__':
    pdf = pdfConverter()
    pdf.pdfConv()

import pandas
import os


class Reader:
    def __init__(self):
        self.file = []
        self.files = []

        self.list_ = []
        self.output = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/Final_Update/output.xlsx'
        self.path = r'file:///Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/PDFs/{}.pdf'

    def openFiles(self):
        os.chdir(r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/Outputs')
        for filename in os.listdir(os.getcwd()):
            self.file.append(filename)

    def search(self):
        for i in range(len(self.file)):
            with open(self.file[i]) as file:
                content = file.read()

            if 'A determinar en fecha de pago' in content:
                self.list_.append('Estimated')
            else:
                self.list_.append('Finalized')

            f = self.file[i].split('.')
            string = r'=HYPERLINK("{}", "{}")'.format(self.path.format(f[0]), f[0])
            self.files.append(string)

    def writer(self):
        df = pandas.DataFrame({
            'file link': self.files,
            'status': self.list_
        })

        writer = pandas.ExcelWriter(self.output, engine='xlsxwriter')
        df.to_excel(writer, ' ')

        writer.save()

    def main(self):
        self.openFiles()
        self.search()
        self.writer()


if __name__ == '__main__':
    cls1 = Reader()
    cls1.main()

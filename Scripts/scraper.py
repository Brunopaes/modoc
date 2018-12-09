from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import datetime
import time


class Bolsar(object):

    def __init__(self):
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Drivers/chromedriver'
        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {'download.default_directory': r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Mooncake/Data/PDFs'}
        self.chrome_options.add_experimental_option('prefs', self.prefs)
        self.driver = webdriver.Chrome(self.path, chrome_options=self.chrome_options)

    def search(self):
        self.driver.get("https://www.bolsar.com/Vistas/Noticias/InformacionesRelevantes.aspx")

        firstDay = self.firstDay()
        firstDay = '0{}/{}/{}'.format(firstDay.day, firstDay.month, firstDay.year)

        elements = [
            'ctl00$ctl00$ContentPlaceHolder1$tablaContenidoFiltro$txbReferencia',
            'ctl00$ctl00$ContentPlaceHolder1$tablaContenidoFiltro$txbFechaDesde'
        ]

        text = [
            'CEDEAR',
            firstDay
        ]

        for i in range(len(elements)):
            cedear = self.driver.find_element_by_name(elements[i])
            cedear.clear()
            cedear.send_keys(text[i])

        select = Select(self.driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$GrillaListado$dataGridListado$ctl14$cboPages'))
        select.select_by_index(3)
        cedear.send_keys(Keys.RETURN)

        time.sleep(2)
        self.download()

    def download(self):
        table = self.driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_GrillaListado_dataGridListado')
        rows = table.find_elements_by_tag_name('tr')

        lenght = []
        for row in rows:
            lenght.append(row)

        for i in range(2, (len(lenght) + 22)):
            string = '//*[@id="ctl00_ctl00_ContentPlaceHolder1_GrillaListado_dataGridListado"]/tbody/tr[{}]/td[5]/a'.format(i)

            cedear = self.driver.find_element_by_xpath(string)
            action = ActionChains(self.driver)
            action.click(cedear).perform()

    def close(self):
        self.driver.close()

    @staticmethod
    def firstDay(date=''):
        if date == '':
            date = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        return date.replace(day=1)


if __name__ == "__main__":
    p = Bolsar()
    p.search()
    time.sleep(3)
    p.close()

import requests
from bs4 import BeautifulSoup
import io
import time


class Program():
    # init self list here
    def __init__(self):
        self.marka = []
        self.model = []
        self.year = []
        self.course = []
        self.capacity = []
        self.power = []
        self.type = []
        self.price = []

    # main function of program
    def main(self):
        for r in range(460):
            try:
                k = r + 1
                # link to otomoto page
                link = 'https://www.otomoto.pl/motocykle-i-quady/?search%5Border%5D=created_at%3Adesc&page=' + str(k)
                z = self.collect_links(link)
                for i in z:
                    data = self.collect_data(i)
                    print(data)
                    self.marka.append(data[0])
                    self.model.append(data[1])
                    self.year.append(data[2])
                    self.course.append(data[3])
                    self.capacity.append(data[4])
                    self.power.append(data[5])
                    self.type.append(data[6])
                    self.price.append(data[7])
                print(self.marka)
            except:
                pass
        # Save to files
        with io.open('marka.txt', 'w+', encoding='utf-8') as file:
            for i in self.marka:
                file.write(str(i) + '\n')
        with io.open('model.txt', 'w+', encoding='utf-8') as file:
            for i in self.model:
                file.write(str(i) + '\n')
        with io.open('year.txt', 'w+', encoding='utf-8') as file:
            for i in self.year:
                file.write(str(i) + '\n')
        with io.open('course.txt', 'w+', encoding='utf-8') as file:
            for i in self.course:
                file.write(str(i) + '\n')
        with io.open('capacity.txt', 'w+', encoding='utf-8') as file:
            for i in self.capacity:
                file.write(str(i) + '\n')
        with io.open('power.txt', 'w+', encoding='utf-8') as file:
            for i in self.power:
                file.write(str(i) + '\n')
        with io.open('type.txt', 'w+', encoding='utf-8') as file:
            for i in self.marka:
                file.write(str(i) + '\n')
        with io.open('price.txt', 'w+', encoding='utf-8') as file:
            for i in self.price:
                file.write(str(i) + '\n')

    # From one page collect all notice as links
    def collect_links(self, link):
        try:
            self.list = []
            self.lista = []
            self.final = []
            site = requests.get(link)
            soup = BeautifulSoup(site.content, 'html.parser')
            soup = soup.find_all(class_='offer-title__link')
            soup1 = str(soup)
            soup1 = soup1.split('href')
            for i in soup1:
                self.list.append(i.split('title'))
            for i in self.list:
                self.lista.append(i[0])
            for i in self.lista:
                self.final.append(i[2:-2])
            self.final.pop(0)
            return self.final
        except:
            pass

    # Uses links collected in previous method and scrap all necessary things about motorcycle
    def collect_data(self, list):
        self.finall = []
        try:
            time.sleep(1)
            # preparing BeautifulSoup for values
            listaa = [10, 14, 18, 21, 24, 27, 34]
            self.final = []
            site = requests.get(list)
            soup = BeautifulSoup(site.content, 'html.parser')
            soup_price = BeautifulSoup(site.content, 'html.parser')
            # preparing BeautifulSoup for price
            soup_price = soup.find_all(class_='offer-price__number')
            soup_price = str(soup_price)
            soup_price = soup_price.split(">")
            another_list = []
            # starting colectin values
            soup1 = soup.find_all(class_="offer-params__value")
            html = str(soup1)
            html = html.split("       ")
            for i in listaa:
                self.final.append(html[int(i)])
            for i in self.final:
                self.finall.append(i[2:])
            # staring colecting price
            for i in soup_price[1][:10]:
                if i != " ":
                    another_list.append(i)
            price = ''.join(another_list)
            self.finall.append(price)
            print(self.finall[7])
            return self.finall
        except:
            return self.finall


prog = Program()
prog.main()

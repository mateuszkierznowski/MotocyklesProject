import requests
from bs4 import BeautifulSoup
import io
import time
import pandas as pd


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
        self.df = pd.DataFrame(columns=['marka', 'model', 'year', 'course', 'capacity', 'price'])

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
                    self.df = self.df.append({'marka': data[0], 'model': data[1], 'year': data[2], 'course': data[3], 'capacity': data[4], 'price': data[5]}, ignore_index=True)
                print(self.marka)

                print(self.df)
            except:
                pass
        # Save to files
        self.df.to_csv('csv/proba.csv')

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


#imports
import io
import csv

#crete lists to create DataFrame
marks = []
capacity = []
course = []
model = []
power = []
price = []
type = []
year = []

#read from file an append to lists
with io.open('marka.txt', 'r', encoding='utf-8') as file:
    z = 1
    for i in file.readlines():
        marks.append(i[:-1])
with io.open('capacity.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        capacity.append(i[:-1])
with io.open('course.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        course.append(i[:-1])
with io.open('model.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        model.append(i[:-1])
with io.open('power.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        power.append(i[:-1])
with io.open('price.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        price.append(i[:-1])
with io.open('type.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        type.append(i[:-1])
with io.open('year.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines():
        year.append(i[:-1])
#make an csv
with open('motocykles_otomoto.csv','w',newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['price','marka','model','pojemnosc','przebieg','moc','year'])
    for i in range(len(year)):
        thewriter.writerow([price[i], marks[i], model[i], capacity[i], course[i], power[i], year[i]])






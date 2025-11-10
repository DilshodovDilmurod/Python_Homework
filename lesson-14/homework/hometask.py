1 write a Python script that reads the students.jon JSON file and prints details of each student.
import json
student_js={
    'sudents':[
        {
            'name':'Sarvar',
            'lastname':'sattorov',
            'age':22,
            'dagree': 'junior',
            'adress': 'xorazm',
        },
        {
            'name':'ahmet',
            'lastname':'qobulov',
            'age':32,
            'dagree': 'junior',
            'adress': 'nokis',
        },
        {
            'name':'john',
            'lastname':'simth',
            'age':20,
            'dagree': 'senior',
            'adress': 'toshkent',
        },
        {
            'name':'tom',
            'lastname':'mark',
            'age':36,
            'dagree': 'middle',
            'adress': 'andijon',
        }
    ]

}
with open('students.json', 'w') as f:
    json.dump(student_js, f, indent = 4) 

with open('students.json', 'r') as f:
    result = json.load(f) 
    for key in result:
        for key2 in result[key]:
            for k, v in key2.items():
                print(f'{k}: {v}')
            print()
2 Task: Weather API
Use this url : https://openweathermap.org/
Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://openweathermap.org/city/1512473'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')
city = soup.select_one('h2[data-v-3e6e9f12]')

temp = soup.find('span', class_ = 'heading')

feels_temp = soup.find('div', class_ = 'bold')

wind = soup.find('div', class_='wind-line')
humidity = soup.select_one('span[data-v-3208ab85]')

print(f'''Bugun {city.text} da obhavo malumotlari:
          temperatura:{temp.text} va {feels_temp.text},
           shamol tezligi: {wind.text}''')


driver.quit()


3 Task: JSON Modification
Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
# add
# update
# delete
import json
with open ('data.json', 'w') as f:
    f.write("[]")

# 1 add book 
while True:
    book_title = input('write name of book')
    description = input('wtite description of book')
    book = {
        'title':book_title.title(),
        'description':description.title()
    }
    with open('data.json', 'a') as f:
        json.dump(book, f, indent=4)
        print(f'{book['title'].title()} file ga qoshildi')

    skil = input('Yanma kitob qoshasizmi?(ha/yoq)')
    if skil == 'yoq':
        break

with open('data.json', 'r') as f:
    results = json.load(f) 
    print(results)
     
    

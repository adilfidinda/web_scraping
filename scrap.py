from bs4 import BeautifulSoup
import requests
import json
url = "http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/"
web = requests.get(url)
out = BeautifulSoup(web.content, 'html.parser')

a= []
for i in out.findAll("strong"):
    if i.text[0:2].isdigit():
        a.append(i.text)

hero = a[:34]
monster = a[34:]

new_hero = []
for j in hero :
    new_hero.append(j.split(" ",1))

new_monster = []
for j in monster :
    new_monster.append(j.split(" ",1))

data = [{'Ultraman': new_hero,
         'Monster': new_monster
       }]

with open('ultra_json.json','w') as file:
    json.dump(data, file, indent=1)
print('Success!')

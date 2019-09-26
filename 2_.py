from bs4 import BeautifulSoup
import requests
import json

req = requests.get('http://digidb.io/digimon-list/')
soup = BeautifulSoup(req.content, 'html.parser')

data = soup.find('tbody')
data = data.find_all('tr')
# .b.text.replace(u'\xa0', '')
digimon_list = []
for i in data:
    no = i.find('td', width='5%').b.text
    digimon = i.a.text
    img = i.img['src']
    stage = i.center.text
    tipe = i.find('td', width='7%').text
    attrib = i.find('td', width='7%').find_next_sibling().text
    memory = i.find('td', width='7%').find_next_sibling().find_next_sibling().text
    equip = i.find('td', width='8%').text
    fitur = i.find_all('td', width=False)
    # print(fitur)
    fitur_list = []
    for i in fitur:
        fitur_list.append(i.string)
    # print(fitur_list)
    x = {
        'no': int(no),
        'digimon': digimon,
        'image': img,
        "stage": stage,
        'type': tipe,
        'attribute': attrib,
        'memory': int(memory),
        'equip slots': int(equip),
        "hp": int(fitur_list[0]),
        "sp": int(fitur_list[1]),
        "atk":int(fitur_list[2]),
        "def":int(fitur_list[3]),
        "int":int(fitur_list[4]),
        "spd":int(fitur_list[5])
        }
    digimon_list.append(x)
# print(x)
with open('digimon.json', 'w') as z:
    json.dump(digimon_list, z)
import requests
import winsound
import time
from bs4 import BeautifulSoup

def check(cat, max_num):
    teams = []
    
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    tree = requests.get(r'https://www.runcity.org/ru/events/2019/status/' + cat + r'/', headers=headers)
    ps = BeautifulSoup(tree.content, 'html.parser')

    for res in ps.find_all("div", {"title": "Место свободно"}):
        try:
            num = int(res.find("div", {"class": "addteam"})["snumber"])
            if num <= max_num:
                teams.append(num)
        except:
            teams.append(res)

    return teams

if __name__ == '__main__':
    fl = False
    while True:
        try:
            if check("sphynx-middle", 60):
                fl = True
                break
            time.sleep(180)
        except Exception as e:
            print(e)

    if fl:
        while True:
            winsound.Beep(2500, 1000)
            time.sleep(5)

    

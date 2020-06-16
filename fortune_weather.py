import requests
from bs4 import BeautifulSoup
def fortune() :
    #tenki.jpの目的の地域のページのURL（茨城県つくば市）
    url = 'https://fortune.yahoo.co.jp/12astro/virgo'

    #HTTPリクエスト
    r = requests.get(url)

    #HTMLの解析
    fortune = BeautifulSoup(r.content, "html.parser")

    #今日の占い
    today = fortune.find(class_="wr mg10t")
    kyou = str(today.p.string)
    kyou = kyou[5:]
    #print(kyou)

    #12正座占い
    otomeza = today.find("table")
    otomeza = str(otomeza.strong.text)
    otome = otomeza[3:]
    number = otomeza[0:2]
    otomeza_number = "{} : {}".format(otome,number)

    #総合運
    unsei = today.find("table")
    unsei = unsei.find_all("td")
    un = unsei[1].find_all("img")

    #name
    mono = today.find("table")
    mono = mono.find_all("a")
    mono = mono[1:5]

    ans = ""
    ans = ans + kyou + "\n"
    ans = ans + otomeza_number + "\n"
    for i in range(0,len(mono)) :
        if i == 0 :
            k = str(un[i])
            k = k[10:18]
            j = str(mono[i].string)
            ans = ans + j + " : " + k + "\n"
        else :    
            k = str(un[i])
            j = str(mono[i].string)
            k = k[10:16]
            ans = ans + j + " : " + k + "\n"
    return ans
a = fortune()
print(a)

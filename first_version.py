import requests
import time
from bs4 import BeautifulSoup
head = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36'}
basliq=[]
class deneme():

    def __init__(self):
        self.s = requests.Session()

    def login(self,login,sifre):
        url = 'https://www.azstat.org/evtesg/index.jsp'
        url2 = 'https://www.azstat.org/evtesg/body.jsp'
        ##url = 'https://0c2bdebdec3972a29c05bfd4cded89f3.m.pipedream.net' ##deneme url
        data = {'KODINTERVYUER': login, 'PASS': sifre}
        self.s.post(url, data=data, headers=head) #login olur
        time.sleep(1)
        html=self.s.post(url2,data=data,headers=head).content #body.jpdan datalari alir
        soup = BeautifulSoup(html, "html.parser")
        for i in soup.find_all("input"):
            a=i.get("value")
            basliq.append(a)
        time.sleep(1)
        urlad = 'https://www.azstat.org/evtesg/profile.jsp?id=' + login
        html = requests.post(urlad, headers=head).content
        soup = BeautifulSoup(html, "html.parser")
        ad = []
        for i in soup.find_all('input'):
            a = i.get("value")
            ad.append(a)
        print("\n{} firildaq isler gormeye gelib ;)".format(ad[0]))
        #return self.s.post(url, data=data, headers=head) #artiq pos getmemesi ucun cixardim
    def get(self,rub,aileno):
        url = 'https://www.azstat.org/evtesg/load.jsp'
        ##url = 'https://0c2bdebdec3972a29c05bfd4cded89f3.m.pipedream.net' ## deneme url
        data = {'AREAL': basliq[2], 'DOVR': rub, 'HHNUMBER': aileno, 'IL': '2020', 'INTERVYUER': basliq[3], 'KODARAZI': basliq[0],
                'KODZONA': basliq[1], 'button': 'D2', 'metod': '0'}
        return self.s.post(url, data=data, headers=head)

    def parcala(self):


        with open("hk.txt", 'r') as file:
            file.seek(3)
            self.dica = list()
            print("Daxil olacaq mehsullar :\n")
            for i in file:
                i = i.split()
                i[4]=float(i[4])
                if (i[4]==1 or i[4]==3 or i[4]==4):
                    data = {'LINE': i[0], 'CODE': i[1], 'WHERE1': i[2], 'QUANT': i[3], 'MEASURE': i[4], 'AMOUNT': i[5],
                            'FROWHOM': i[6], 'd2_8': 'Yaz'}
                    self.dica.append(data)

                else:
                    i[5]=str(i[4])
                    i[4]=str("")
                    i[6]='1'
                    data = {'LINE': i[0], 'CODE': i[1], 'WHERE1': i[2], 'QUANT': i[3], 'MEASURE': i[4], 'AMOUNT': i[5],
                            'FROWHOM': i[6], 'd2_8': 'Yaz'}
                    self.dica.append(data)
                print(i[:7])
        print("Kodlara goz gezdir problem varsa 2, yoxsa yazmaga baslamaq ucun 1'i bas....\n")
        return self.dica
    def add(self):
        url = 'https://www.azstat.org/evtesg/d2.jsp?metod=1'
        ##url = 'https://enmjezaa2bznd.x.pipedream.net/' ## deneme url

        print(
            """
            ************************************************

            Aytekin qiziniz tabele qol cekib ise basladi....

            ************************************************\n
            Cay filan basinizi qatin, yazacam :) 
            """
        )
        i = 0
        while True:

            if (i > (len(self.dica) - 1)):
                print("Aytekin qiziniz {} mehsul yazdi ve yoruldu :)".format(i))
                break
            else:
                self.s.post(url, data=self.dica[i], headers=head)
                print("Qiziniz {}'cu mehsulu daxil eledi".format(i))
                time.sleep(2)
            i += 1


a=deneme()
print(
    """
    ---------------------------------------------
    Vay anam, vayy babam kimler gelmis  bele :)

    Aytekin stat v1.1 botu  sizi salamlayir.... 
    ----------------------------------------------
    """
)
mkodu=input("Meslehetci kodu:")
msifre=input("Sifre :")
a.login(mkodu,msifre)
time.sleep(2)
while True:
    rub=input("Rub:")
    ailenom = input("Aile nomresi:")
    a.parcala()
    d = input("1 ya 2 : ")
    if (d=="1"):
        a.get(rub,ailenom)
        print("D2'e kecib, Aytekine verecey....")
        time.sleep(2)
        a.add()
        print("\n {}'cu ailenin mehsullari yazildi, davam elemek ucun hk.txt'e duzelis edin sonra, rubu ve novbeti ailenin melumatlarin qeyd edin \n  ".format(ailenom))
        time.sleep(2)
    elif (d=="2"):
        print("hk.txt filesini duzelt yaddasa sal yeniden yoxla....")
    else:
        break